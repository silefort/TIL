# Redirect stderr To stdout

## I/O streams numbers

Handle | Name   | Description
-------|--------|
0      | stdin  | Standard input
1      | stdout | Standard output
2      | stderr | Standard error

## Redirect stderr to stdout

    $ command-name 2>&1

## Redirecting the standard error (stderr) and stdout to file

    $ command-name &>file
