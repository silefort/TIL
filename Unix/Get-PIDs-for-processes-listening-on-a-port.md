# Get ONLY PIDs for processes listening on a port

    $ lsof -ti tcp:<port>

Easy to pipe it to xargs later:

    $ lsof -ti tcp:3000 | xargs kill
