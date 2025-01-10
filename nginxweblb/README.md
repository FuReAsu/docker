This sets up an nginx environment with one lb and four webserver.
 There will be two website pools on the lb with 2 webservers each. 
 The webservers are separeted from the public network and only the lb will be reachable from the public network.
 There are two backend networks for the webservers and one frontend for lb.

 The frontend network is ipvlan type. Edit the docker-compose file to match the ip and interface perimeters with your network.
