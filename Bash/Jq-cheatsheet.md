# Jq cheatsheet

## Pretty print a json body

    $ curl https://mediashare.fr/api/posts | jq
    
## Get a specific value 

    $ curl https://mediashare.fr/api/posts | jq '.status'
    
## Navigate within a table

    $ curl https://mediashare.fr/api/posts | jq '.posts[0]'
    $ curl https://mediashare.fr/api/posts | jq '.posts[1,2]'
    $ curl https://mediashare.fr/api/posts | jq '.posts[0:10]'
    
## Get the value of an element within a table

    $ curl https://mediashare.fr/api/posts | jq '.posts[].id'
    $ curl https://mediashare.fr/api/posts | jq '.posts[].author'
    
## Create an object from an array 

    $ curl https://mediashare.fr/api/posts | jq '.posts[]|{"id": .id, "title": .title, "views": .views}'

## ... and sort it by views number

    $ curl https://mediashare.fr/api/posts | jq '[.posts[]|{"id": .id, "title": .title, "views": .views}] | sort_by(.views)'
