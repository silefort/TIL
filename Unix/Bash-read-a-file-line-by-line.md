# Bash Read a File Line By Line

    while IFS= read -r line; do COMMAND_on $line; done < input.file
