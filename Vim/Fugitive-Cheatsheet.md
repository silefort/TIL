# Fugitive Cheatsheet

## Basic Commands

    :Git [args] # does what you'd expect

## Working with the index

    :Gwrite   # add
    :Gread    # checkout
    :Gremove  # rm
    :Gmove    # mv

## Gstatus

    :Gstatus # launch a Gstatus buffer

    <CR>        |:Gedit|
    <C-n>/<C-p> moving around files
     -          |:Git| add        # both work in Visual mode too
     -          |:Git| reset (staged files)
     cc         |:Gcommit|
     D          |:Gdiff|
     p          |:Git| add --patch
     q          close status
     R          reload status
     U          Revert the file back to the index

## Diffs

    ]c and [c  # Navigate changes
