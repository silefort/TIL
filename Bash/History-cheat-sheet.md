# History command Cheat Sheet

    $ history # Show History
    $ history -d 42 # Remove an history line
    $ history -c # Clean all the history
    $ export HISTIMEFORMAT='%F %T ' # Show history formatted as 483 2017-12-27 11:22:00 ls
    $ export HISTIGNORE='ls -l:pwd:history' # Remove some lines from the history
    $ cat /home/USER/.bash_history # Show the history of a specific user

## Play with arguments

    $ mv /path/to/rightfile !$ # !$ represents the last argument of the previous command line
    $ !:0 !:1 !:3 !:2          # !:n represents the nth argument of the previous command line
    $ egrep !:1-$              # !:1-$ represents all the arguments except the first one ( most probably the binary name )
    $ cd !$:h                  # !$:h tells to get the last argument and remove the filename to retrieve only the directory path
    $ cp bla !#:1.bak          # !#:1 refers to the 1st argument of the current line
