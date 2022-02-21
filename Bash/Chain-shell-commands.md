# Chain Shell commands

    # Execute commands on after another
    $ command1; command2; command3;
    
    # Execute commands only if previous command exits in success (output = 0)
    $ command1 && command2 && command 3
    
    # Execute commands only if previous command fails (output != 0)
    $ command1 || command2 || command3
