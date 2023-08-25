# install flask package from pip3 provider pip3 and version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
