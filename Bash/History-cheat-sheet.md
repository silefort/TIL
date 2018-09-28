# History command Cheat Sheet

    $ history # Show History
    $ history -d 42 # Remove an history line
    $ history -c # Clean all the history
    $ export HISTIMEFORMAT='%F %T ' # Show history formatted as 483 2017-12-27 11:22:00 ls
    $ export HISTIGNORE='ls -l:pwd:history' # Remove some lines from the history
    $ cat /home/USER/.bash_history # Show the history of a specific user
