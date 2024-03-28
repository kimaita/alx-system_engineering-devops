# Installs flask (v2.1.0) from pip3.
$pkg = 'flask'
$pkg_dep = 'Werkzeug'

package { $pkg:
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package[$pkg_dep]
}

package { $pkg_dep:
  ensure   => '2.2.2',
  provider =>'pip3'
}
