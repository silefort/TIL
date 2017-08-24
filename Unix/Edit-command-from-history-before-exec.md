# Edit a command from your history before executing it

## Search your history:

    history | grep curl
    10256 curl www.google.com
    10500 curl www.amazon.com

## Edit the chosen command

    fc 10500

It will launch your favorite editor, save, quit and the edited command will be executed
