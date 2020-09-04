# NetGPIO

A simple flask application to control your Raspberry Pi's gpio's from a website.

![Preview](https://raw.githubusercontent.com/pythonmaxi/NetGPIO/master/netgpio.png)

## Installation

First install some dependencies

`sudo apt install python3-pip apache2 libapache2-mod-wsgi-py3`

Install fpython dependencies

`sudo pip3 install flask RPi.GPIO tornado`

Download NetGPIO and configure apache2

```
cd /var/www/
sudo git clone https://github.com/pythonmaxi/NetGPIO.git
sudo chown www-data:www-data NetGPIO
sudo cp NetGPIO/NetGPIO.conf /etc/apache2/NetGPIO.conf
sudo a2ensite NetGPIO.conf
# remove default website if you havent
sudo a2dissite 000-default.conf
# add www-data user to gpio to allow acces to the gpio
sudo adduser www-data gpio
```

Generate your gpios.json file

```
cd NetGPIO
./genGPIO.py
#or
python3 genGPIO.py
```

Finally just restart apache2

`sudo service apache2 restart`

## Using NetGPIO

You can get to the NetGPIO interface by navigating in your browser to the ip of your Raspberry Pi `hostname -I` or to the host name directly `hostname` but adding a .local to the host name,
in both of the cases you need to be in the same network than the Pi.
