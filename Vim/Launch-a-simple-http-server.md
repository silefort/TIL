# Launch a simple HTTP Server

    #!/usr/bin/python

    import SocketServer
    import BaseHTTPServer
    import SimpleHTTPServer

    class ThreadingSimpleServer(SocketServer.ThreadingMixIn,
                       BaseHTTPServer.HTTPServer):
        pass

    import sys

    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000

    print "Listening on port: " + str(port)
    server = ThreadingSimpleServer(('', port), SimpleHTTPServer.SimpleHTTPRequestHandler)
    try:
        while 1:
            sys.stdout.flush()
            server.handle_request()
    except KeyboardInterrupt:
        print "Finished"
