# Show most modified files

  $ git log --format=format: --name-only --since=12.month \ | egrep -v '^$' \ | sort \ | uniq -c \ | sort -nr \ | head -50
