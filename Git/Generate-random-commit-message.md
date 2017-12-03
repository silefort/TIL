# Generate a random commit message

    $ curl -s http://whatthecommit.com/ | grep -A1 '"content"' | tail -1 | awk -F'>' '{ print $NF }'
