# Monitor ssl certificate expiration date

Use this script ( copied from here: https://michael.parienti.net/posts/2020/05/22/monitorer-des-certificats-avec-bash/ )

```
#!/bin/bash

get_date () {
    local host=$1
    local port=$2
    text_date=$(echo - | openssl s_client -ign_eof -showcerts -servername $host -connect $host:$port 2>/dev/null | openssl x509 -inform pem -noout -enddate|cut -f 2 -d =)
    echo $text_date
}

get_nb_days () {
    local date=$1
    now=$(date +"%s")
    expire=$(date --date="${date}" --utc +"%s")
    seconds_expire=$(($expire-$now))
    days_expire=$((${seconds_expire}/$((60*60*24))))
    echo $days_expire
}

main () {
    for var in "$@"
    do
        text_date=$(get_date ${var/:/ })
        nb_days=$(get_nb_days "$text_date")
        echo $var $nb_days
    done
}

main "$@"
```

It can then be used like this:

```
./script.sh google.com:443
```
