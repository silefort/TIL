# Exit ssh stuck sessions

## Exit automatically on network interruptions

Add the following lines to your .ssh/config file

    ServerAliveInterval 5
    ServerAliveCountMax 1

* ssh will check the connection by sending an echo to the remote host every ServerAliveInterval seconds.
* If more than ServerAliveCountMax echos are sent without a response, ssh will timeout and exit

## Break out of the session

* ssh includes the escape character `~` by default. 
* The command `~.` closes an open connection and brings you back to the terminal. (You can only enter escape sequences on a new line.) 
* `~?` lists all of the commands you can use during a session. 
* On international keyboards, you may need to press the `~` key twice to send the `~` character.
