# HTTPS SSL

Hyper Text Transfer Protocol Secure (HTTPS) is the secure version of HTTP. All communication between the browser and website is encrypted.

One of two protocols is used in the encryption:
- Secure Sockets Layer(SSL)
- Transport Layer Security(TLS)
Both use asymmetric encryption with a private and public key.
The server's public key is sent to browsers in a SSL certificate after which an _SSL handshake_ is iniated.
This is basically a step to establish a secure connection by sharing secrets.

In this project, we set up our website to use _SSL termination_ - traffic to the load balancer is SSL encrypted.

