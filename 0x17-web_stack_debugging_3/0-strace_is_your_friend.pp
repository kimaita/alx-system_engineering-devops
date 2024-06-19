# Fixes Wordpress configuration typo

Exec { path => '/bin/:/sbin/:/usr/bin/:/usr/sbin/' }

exec { 'fix_typo':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
}
