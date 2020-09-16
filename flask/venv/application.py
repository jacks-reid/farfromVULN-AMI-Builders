from flask import *
import json
import subprocess
application = Flask(__name__)

with open('instance_ips.txt', 'r') as ips_file:
    data = json.load(ips_file)
        
    vpn_ip = data['PiVPN'].get('value')
    kali_ip = data['Kali'].get('value')
    vulns = []

    # Find the vulnerable machine
    for machine_name in data:
        if machine_name != 'Kali' and machine_name != 'PiVPN':
            mini_list = [machine_name, data[machine_name].get('value')]
            vulns.append(mini_list)

if __name__ == '__main__':
    application.run(host='0.0.0.0')    

@application.route('/')
def index():
    return render_template('index_template.html', vpn_ip=vpn_ip, kali_ip=kali_ip, vulns=vulns)

@application.route('/images/<image>')
def get_image(image=None):
    return send_file('images/' + image, mimetype='png')

@application.route('/faq.html')
def get_faq():
    return send_file('faq.html')

@application.route('/<name>')
def get_vpn(name=None):
    cmd = "pivpn -a -n " + name + " nopass -d 1000"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    application.logger.debug(output)
    application.logger.warning(error)

    ovpn_file = send_from_directory('/home/ubuntu/ovpns/', filename = name + '.ovpn', as_attachment = True)
    return ovpn_file

