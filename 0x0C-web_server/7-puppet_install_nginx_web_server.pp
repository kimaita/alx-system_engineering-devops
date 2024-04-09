# Configures a web server with a custom root page and redirect
Exec { path => '/bin/:/sbin/:/usr/bin/:/usr/sbin/' }

package { 'nginx':
    ensure => installed
}

exec { 'configure_root':
  command => 'echo Hello World! > /var/www/html/index.html'
}

$search='server_name _;'
$redirect="\\\trewrite ^/redirect_me https://youtu.be/7GBlCinu9yg?si=XFRkIUkOZrTySvVb permanent;"

exec { 'configure_redirect':
  command => "sed -i \"/${search}/a ${redirect}\" /etc/nginx/sites-available/default"
}

service { 'nginx' :
    restart => 'reload'
}
