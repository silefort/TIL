# Send keys to another Pane

    $ tmux send -t 3 "vim" Enter

This will open vim on the Pane "3"
You can also use "-t -1" to send your command to the last pane available
