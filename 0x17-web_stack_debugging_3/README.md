# Webstack Debugging #3

Debugging an LAMP stack server for a Wordpress website. The server returns a `500` error.

```bash
$ curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Thu, 09 May 2024 12:04:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html
```

## Tools

- [strace](https://strace.io/)  
    > strace can monitor interactions between processes and the Linux kernel.

## Methodology

To debug, the apache pid is first obtained. `strace`  is then attached to apache using this pid. We then write the output to a file for analysis after trying a request.

```bash
$ ps -e | grep apache2
224 ?        00:00:00 apache2
$ strace -p 224 -o strace-apache
Process 224 attached

```

In another terminal, we send another request and then open the `strace-apache` file. (output truncated)

```bash
$ less strace-apache
...
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffe25428660) = -1 ENOENT (No such file or directory)
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffe25428530) = -1 ENOENT (No such file or directory)
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffe2542a760) = -1 ENOENT (No such file or directory)
open("/var/www/html/wp-includes/class-wp-locale.phpp", O_RDONLY) = -1 ENOENT (No such file or directory)
...
```

We find that the program fails because of a missing file. This clearly looks like a typo in the extension since the `/var/www/html/wp-includes/` directory contains a `class-wp-locale.php` file.

On checking the `wp-settings.php` file, we find the misconfiguration:

```
require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );
```

We resolve this by using `sed` to replace `.phpp` with `.php` using [puppet](./0-strace_is_your_friend.pp).
