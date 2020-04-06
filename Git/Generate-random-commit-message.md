# Generate random commit messages

whatthecommit.com display random messages that can be included in your commit

To use it, you can add a specific git alias:

    git config --global alias.rand '!git commit -m "$(curl -s whatthecommit.com/index.txt)"'

Then just use it:

    git rand
