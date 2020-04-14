# cp Template.md Git/List your most recently-used branches

    $ git branch --sort="-committerdate" --format="%(color:green)%(committerdate:relative)%(color:reset) %(refname:short)"
