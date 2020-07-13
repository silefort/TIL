# Fzf Cheasheet

By default fzf will launch interactive finder, read the list from STDIN, and write the selected item to STDOUT

## Open a file using fzf

$ vim $(fzf)

## Navigate the list

CTRL-N / CTRL-P : Move the cursor Down & Up
ENTER : Select the item
CTRL-C : Exit
TAB: : Select multipe items

## Use multi-select mode
$ fzf -m

## Use "top down" mode ( search bar on top)
$ fzf --reverse

## Set Default values
export FZF_DEFAULT_OPTS="--layout=reverse --inline-info --border"
