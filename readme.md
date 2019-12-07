# Black Rock Forest Project

A store and forward server that records sensor data and passes it along to each node in the network until it arrives at the central server.

At one end of the network, are one or more sensors. Those sensors can connect to a Raspberry Pi or local server if connected to a LAN, or a remote server if connected to the Internet. All of our testing has been done with the ESP8266, DHT22, Raspberry Pi and Digital Ocean.

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
