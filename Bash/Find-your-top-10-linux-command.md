# Find your top 10 linux commands in your history

    cat ~/.bash_history | sort |uniq -c|sort -nr|head -n 10
