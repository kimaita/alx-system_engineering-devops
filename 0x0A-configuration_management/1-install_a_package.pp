# Installs flask (v2.1.0) from pip3.
$pkg = 'flask'

package { $pkg:
  ensure   => '2.1.0',
  provider => 'pip3'
}
