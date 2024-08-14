# finding why Apache is returning a 500 error

exec { 'Fix wordpress site':
  command  => '/bin/sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => 'shell',
}

