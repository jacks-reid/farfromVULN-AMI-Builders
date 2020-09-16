# farfromVULN-AMI-Builders
A collection of the files used to build the AMI's used in the farfromVULN project.

Currently only the PiVPN instance in farfromVULN uses a custom AMI. The purpose of creating a custom AMI is to provision an AMI that has the farfromVULN webapp up and running once an EC2 instance is deployed.

## Prerequisites
Packer is the tool used to build the AMI.

Packer installation can be found at https://learn.hashicorp.com/tutorials/packer/getting-started-install .

The AWS command line tool is required. You should have already configured your profile using `aws config`.

## Instructions
To built the PiVPN AMI for farfromVULN, use the following command:

```
packer build ffv_ubuntu.json
```

An AMI will be built and provisioned and uploaded to your AWS account. It will then be tagged with "Name:farfromVULN_VPN" and "Release:Latest". This AMI is used with the farfromVULN project.
