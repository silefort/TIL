# Ansible Vault Tips

Encrypt a variable:

    $ cat /tmp/variable | ansible-vault encrypt_string --ask-vault-pass --name 'variable_name'

Decrypt a variable:

    $ cat /tmp/variable | ansible-vault decrypt /dev/stdin --output=/dev/stderr > /dev/null 
