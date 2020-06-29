# use nginxui to modify your Nginx Conf through a nice UI

    $ docker run -d --restart=always --name nginxui -v /etc/nginx:/etc/nginx -p 8080:8080 schenkd/nginx-ui:latest

The repo is available here:

    https://github.com/schenkd/nginx-ui
