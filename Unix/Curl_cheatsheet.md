# Curl Cheatsheet

    $ curl foo.com    # Send a GET request
    $ curl -i foo.com # display the response headers
    $ curl -I foo.com # Do a HEAD request
    $ curl -d bli=bla foo.com # do a POST request
    $ curl -d @file foo.com # POST using the pload of file
    $ curl  foo.com --next bar.com # send 2 sequencials requests
    $ ls -l | curl -d @- foo.com -o saved # POST the output of ls -l and save the response to saved
    $ curl foo.com --trace-ascii # Max Verbose
    $ export SSLKEYLOGFILE=$HOME/tmp/tlskey to save the secrets that can be used by wireshark to decrypt encrypted traffic
    $ curl --http1.0 foo.com # 
    $ curl --http2 foo.com # request using h2
    $ curl foo.com --libcurl sourcecode.c && gcc sourcecode.c -lcurl -o ./myapp # Compile youre request into an application
    $ curl -# -O https://files.example.com/large/long_video.mp4 # Display a progress bar while downloading
