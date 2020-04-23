# POC custom Ansible callback plugin 
This callback plugin will update a slack channel on each playbook run.
This is just a quick and dirty hack, if you are looking for a more solid foundation, please use https://docs.ansible.com/ansible/latest/plugins/callback/slack.html

## Requirements

- pip3 install ansible
- vagrant
- a slack webhook in a $SLACK_WEBHOOK_URL environment variable

## Run
vagrant up
