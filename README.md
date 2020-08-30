# WebGPIO

A simple flask application to control your Raspberry Pi's gpio's from a website.

## Installation

First install some dependencies

`sudo apt install python3-pip apache2 libapache2-mod-wsgi-py3`

Install flask and the gpio stuff

`sudo pip3 install flask RPi.GPIO`

Download WebGPIO and configure apache2

```
cd /var/www/
sudo git clone https://github.com/pythonmaxi/WebGPIO.git
sudo chown www-data:www-data WebGPIO
sudo cp WebGPIO/WebGPIO.conf /etc/apache2/WebGPIO.conf
sudo a2ensite WebGPIO.conf
# remove default website if you havent
sudo a2dissite 000-default.conf
# add www-data user to gpio to allow acces to the gpio
sudo adduser www-data gpio
```

Generate your gpios.json file

```
cd WebGPIO
./genGPIO.py
#or
python3 genGPIO.py
```

Finally just restart apache2

`sudo service apache2 restart`

## Using WebGPIO

You can get to the WebGPIO interface by navigating in your browser to the ip of your Raspberry Pi `hostname -I` or to the host name directly `hostname` but adding a .local to the host name,
in both of the cases you need to be in the same network than the Pi.
