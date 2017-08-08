# Get my Lastfm last week top artists

For this you need to create an account and an API key on the last.fm website.
Then replace 'user' and 'api_key' with the right values

    curl -s "http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=<user>&api_key=<api_key>&format=json&period=7day&limit=3" | jq -c -r '.topartists.artist[] | { name: .name, playcount: .playcount }' | awk -F'"' '{ print $4, "("$8")" }'


