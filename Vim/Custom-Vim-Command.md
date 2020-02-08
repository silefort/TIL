# Custom Vim Commands

## Add a new command

  :command HelloWorld echo "hello world"

## Pass args to your command

  :command! -nargs=1 Say :echo "hello" <q-args>

  :Say world # output "hello world"
