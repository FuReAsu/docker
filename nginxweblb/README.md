This sets up an nginx environment with one lb and four webserver.
There will be two website pools on the lb with 2 webservers each. 
The webservers are separeted from the public network and only the lb will be reachable from the public network.
There are two backend networks for the webservers and one frontend for lb.
These two networks will be internal.

Frontend bridge network will be assigned to lb and lb will be assigned port 8000 (HTTP) and port 9000 (HTTPS) for external access.

To choose between http and http deployment, change the LoadBalancer's config file http-nginx.conf or https-nginx.conf.

Logs are stored in lb/log, web/web_green/log and web/web_blue/log
