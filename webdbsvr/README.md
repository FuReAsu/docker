Sample Web server and Database Server Deployment to test on docker.
Create an isolated network for the connection between the web server and the database server(backend).
Create a network that is accessible to and from the external network(frontend).
Connect the webserver to both the frontend and backend networks. Connect the database to only the backend network.

The  Web server includes a simple php code that can query a simple database in the database server and show its contents.
The purpose of this lab is to test the overall features in docker including volumes, networks, DockerFile and docker-compose.
