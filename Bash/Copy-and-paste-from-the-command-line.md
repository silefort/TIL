# Copy and Paste from the commande line

## Macos

    $ pbcopy < file.txt # Copy file to your clipboard
    $ pbpaste           # Paste from your clipboard to your terminal

## Linux

    $ xclip -sel clip file_name # Copy file_name to your clipboard
    $ tail -n 30 logfile.log | xclip -sel clip # use xclip with other commands
