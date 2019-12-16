# Black Rock Forest Store and Forward Node Project

The Black Rock Forest Store and Forward Node Project is a solution to provide network data loggers for enviornmental sensors that can be used in conjunction with the Black Rock Forest Wifi Mesh network.  

The Store and Forward nodes are data logging Raspberry Pi based servers that are located in the forest. These field base RPi Store and Forward nodes are developed to records sensor data, store locally on a database, and passes it along to each node in the network until it arrives at the Central Store and Forward server in the cloud. The system is configure to recieve sensor data from ESP8266 based chips.  For this documentation the ESP8266 sensor nodes use DHT22 temperature and humidity sensors.  

At one end of the network, are one or more sensors. Those sensors can connect to a Raspberry Pi or local server if connected to a LAN, or a remote server if connected to the Internet. The data is also avaliable to be visualized using Grafana, an application wich is also avaliable in the store and forward node deployment packages that are part of this repository. 
All of our testing has been done with:

- ESP8266 - WEMOS D2 
- DHT22 
- Raspberry Pi 3B+ 
- Digital Ocean Droplet - Ubuntu 18.04
- Grafana V.x

It is important to note that each of these layers are completely decoupled. They work via message passing, as you'll see in the documentation below. In other words, you don't need to use the sensors we used, nor do you need to use a Raspberry Pi, or even Digital Ocean. Any device that's at least as powerful as a Raspberry Pi 3 can host this code and serve as a store and forward node. Any device can send data to the store and forward nodes as well.

The directions below detail how we set up our network, and how you can follow along. 

## Getting Started

### Hardware and Server

[DHT8266](https://www.adafruit.com/product/385)

[ESP8266](http://esp8266.net/)

[Raspberry Pi](https://www.raspberrypi.org/)

[Digital Ocean](https://www.digitalocean.com/)

### How To Guides

[Sensor Guide](./docs/esp8266.md) using the ESP8266 and the DHT22.

[Main App Guide](./docs/main_app.md) to set up the main app as a store and forward server on either a Raspberry Pi or a Server.

[Add A Grafana Panel](./docs/grafana.md)

