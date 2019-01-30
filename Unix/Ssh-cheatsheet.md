# Ssh Cheatsheet

    ssh-copy-id user@host                       # Install your ssh key on a host
    ssh user@host.com -NfL 3333:localhost:8888  # open a remote server on your browser
    ssh user@host.com uname -a                  # Run a command & exit
    <Enter>~.                                   # Close the ssh connection (when hanging)
    ssh-agent                                   # Remember your ssh key passphrase
