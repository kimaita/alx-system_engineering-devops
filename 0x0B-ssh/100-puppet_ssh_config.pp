# Configures SSH client settings
$config_file = '/etc/ssh/ssh_config'

Exec { path => '/usr/bin/' }

exec { 'password_deny':
  command => "sed -i 's/#   PasswordAuthentication yes/PasswordAuthentication no/g' ${config_file}"
}

exec { 'identity_file':
  command => "sed -i 's|#   IdentityFile ~/.ssh/id_rsa|IdentityFile ~/.ssh/school|g' ${config_file}"
}
