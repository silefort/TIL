# Fx : json manipulation command line tool

    $ brew install fx # Install fx
    $ curl http://myapi | fx # Launch fx in interactive mode
    $ curl http://myapi | fx . # Pretty print a json body
    $ curl http://myapi | fx .films # Pretty print only a node of the body

## Interactive digger

    e : expand all fields
    Ctrl + e: collapse all fields
    .repositories.nodes[0].bla # Dig into a node (you can use the arrows to navigate)
    Ctrl + w: erase last path segment
    Ctrl + u: erase whole path
