# Play with the history command

## Set your history limit

    $ export HISTSIZE=3000

## Ignore commands starting with empty space

    $ export HISTCONTROL=$HISTCONTROL:ignorespace

## Avoid duplicate entries:

    $ export HISTCONTROL=$HISTCONTROL:ignoredups

## Ignore both spaces and duplicates:

    $ export HISTCONTROL=$HISTCONTROL:ignoreboth

## Remove an item from your history:

    $ history -d <itemNumber>

## Clear your entire session history:

    $ history -c
