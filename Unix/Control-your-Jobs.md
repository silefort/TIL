# Control your jobs ( backgrounding, foreground...)

Let's say you are editing a file in Vim, but you want to run a command outside, you can exit Vim, run your command and then resume. You can also use jobs

    $ Ctrl + z  # Backrounds any existing foreground task
    $ jobs      # List all the backgrounded jobs
    $ fg        # Bring the background job back to foreground
    $ fg 2      # Bring the second job in the jobs list to foreground ( if you have multiple jobs)
