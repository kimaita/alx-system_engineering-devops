# Web stack debugging #0

For this task, we set up Apache on a Docker container.
```bash
$ docker run -p 8080:80 -d -it holbertonschool/265-0
$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla

```

Before:
```bash
$ curl 0:8080
curl: (52) Empty reply from server
```
The server had no Apache server installed. All that was needed is a simple installation.

Fixed:
```bash
$ curl 0:8080
Hello Holberton
```
