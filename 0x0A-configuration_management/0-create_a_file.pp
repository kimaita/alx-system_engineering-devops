# This manifest creates a file `school` in /tmp with the text 'I love Puppet'
$doc_dir = '/tmp'

file { $doc_dir:
  ensure => 'directory'
}

file { "${doc_dir}/school":
  ensure  => 'present',
  content => 'I love Puppet',
  require => File[$doc_dir],
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
