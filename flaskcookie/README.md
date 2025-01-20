python flask web app setup to test session cookies and session persistence via cookies.
flask is configured to set session cookie upon fist visit.
Subsequent visits to the website will show the session cookie in the page.
Nginx LB is configured to perform hashing on the session cookie to always forward a client with a certain session to one upstream server.
There is only one frontend network that all the containers are in.
This is a one-armed load balancer setup where the load balancer and the upstream servers are in the same network.