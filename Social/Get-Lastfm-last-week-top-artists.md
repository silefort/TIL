# Get my Lastfm last week top artists

Quick & Dirty but it seems to work

    echo "Most listened Artists last week: " && curl -s https://www.last.fm/fr/user/bubububust/library/artists?date_preset=LAST_7_DAYS | grep -v '^\s*$' | grep 'title=\|scrobbles' | head -n6 | awk 'ORS=" "' | awk -F'"|<' '{ print $2 " ("$3")\n" $8 " ("$9")\n" $14 " ("$15")" }' | sed 's/  //g'


