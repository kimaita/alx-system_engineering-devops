# Kills a process named killmenow
$proc = 'killmenow'

exec { 'kill_process':
  command => "pkill ${proc}",
  path    => '/usr/bin/'
}
