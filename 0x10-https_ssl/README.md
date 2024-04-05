# HTTPS SSL

**Hyper Text Transfer Protocol Secure** (HTTPS) is the secure version of HTTP, the protocol over which data is sent between browsers and websites. The 'S' at the end of HTTPS stands for 'Secure' - meaning all communication between your browser and the website is encrypted.

HTTPS pages typically use one of two secure protocols to encrypt communications - **SSL (Secure Sockets Layer)** or **TLS (Transport Layer Security)**. Both the protocols use an _asymmetric_ Public Key Infrastructure (PKI) system. An asymmetric system uses two 'keys' to encrypt communications, a 'public' key and a 'private' key. Anything encrypted with the public key can only be decrypted by the private key and vice-versa.

When you request a HTTPS connection to a webpage, the website will initially send its SSL certificate to your browser. This certificate contains the public key needed to begin the secure session. Based on this initial exchange, your browser and the website then initiate the _SSL handshake_. The SSL handshake involves the generation of shared secrets to establish a uniquely secure connection between yourself and the website.
