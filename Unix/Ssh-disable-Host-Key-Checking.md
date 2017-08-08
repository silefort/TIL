# Disable Host Key Checking when using ssh

    ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no login@host
