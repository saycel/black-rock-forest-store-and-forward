# Store And Forward App
## Getting Started

### Software Prerequisites

Once you have your Raspberry Pi or Server set up download the following (instructions below):
- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)
- [git](https://git-scm.com/)
- [mosquitto](https://mosquitto.org/)

### Install the software prerequisites

On your server or Raspberry Pi, run these commands:

`$ sudo apt-get update`

`$ curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh`

`$ sudo apt install python3-pip -y`

`$ sudo pip3 install docker-compose==1.12.0`

`$ sudo apt install git -y`

Follow these commands *only* if you are using a Raspberry Pi.

`$ sudo apt install mosquitto -y`

`$ sudo touch /etc/mosquitto/conf.d/bridge.conf`

`$ sudo nano /etc/mosquitto/conf.d/bridge.conf`

```
add the following:

connection bridge-central
address *CENTRAL-SERVER-IP*:1883
topic forest out 0
```

`$ sudo systemctl restart mosquitto`

### Development Environment Prerequisites

Make sure you have installed on your computer:
- [postman](https://www.getpostman.com/)
- [mqttbox](http://workswithweb.com/html/mqttbox/downloads.html)

## Running The App

### Getting The App Running (Raspberry Pi)

`$ git clone https://github.com/saycel/black-rock-forest-store-and-forward`

`$ cd black-forest`

Add the following to .env file
```
POSTGRES_PASSWORD=postgres
POSTGRES_DB=brfc
PYTHONPATH=/brfc
```

`$ sudo docker-compose -f docker-compose.raspberry.yml build`

`$ sudo docker-compose -f docker-compose.raspberry.yml up -d`

### Getting The App Running (Linux)

`$ git clone https://github.com/saycel/black-rock-forest-store-and-forward`

`$ cd black-forest`

Add the following to .env file
```
POSTGRES_PASSWORD=postgres
POSTGRES_DB=brfc
PYTHONPATH=/brfc
```

`$ sudo docker-compose build`

`$ sudo docker-compose up`

### Getting The App Running (Mac)

We recommend running the app in Vagrant if you are using a Mac.
Follow the steps to install and run the project:

`$ brew install vagrant`

`$ vagrant plugin install vagrant-docker-compose`

`$ cd black-forest`

`$ vagrant up`

Note: the ip of the VM is 192.168.33.10

### Updating The App

`$ cd black-forest`

`$ git pull `

`$ sudo docker-compose stop`

`$ sudo docker-compose build`

`$ sudo docker-compose up`

### Adding Your First User
To start using the platform you need to first add a user by sending a json post request to http://**SERVER-IP**:2323/user/register with a username and password.

```json 
{	
	"email": "avalid@email.com",
	"password": "4veryS4vePass!!"
}
```

### Login With The User You Just Created
Once you have added a user, to get a token send a post request to http://**SERVER-IP**:2323/user/register with the following json payload:

```json5
{	
	"email": "avalid@email.com",
	"password": "4veryS4vePass!!"
}
```

you will receive a response with a JWT token like this:

```json5
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RlckBnZXJtYW4uY29tIiwidmFsaWRfdW50aWwiOiIyMDIwLTAzLTE2IDE1OjMzOjQ2LjEwNDEyMCJ9._g1OMeiEoLaM7e3eiSjHcV5pKi05MaMzJVzNTMq8LL8"
}
```

### Test To See If The App Is Running
In order to know if the app's REST API is up and running,first make sure the the pc where you installed Postman and the Server or Raspberry Pi where the app is running are on the same LAN. Then follow these steps:

  1) Get the IP address of your Server or Raspberry Pi
  2) In Postman create a post request
     1) In the url textbox: http://**RPI-IP**:2323/login
     2) Click in the Authorization tab and choose Basic Auth type.
     3) The username and password are the same as the ones you added earlier.
     4) Click the send button next to url textbox.
     5) You should receive a json response:
         {"message": "success"}

### Add Data To The Database Using HTTP

Send a GET request using the following API format:

Generic:

http://**RPI-IP**:2323/sensor/collector/<app_key>/<net_key>/<device_id>/?chN=n

Example:

http://10.0.0.115:2323/sensor/collector/1234/abc/x1v3/?ch1=1&ch2=2

  1) open postman
  2) use http://**RPI-IP**:2323/<app_key>/<net_key>/<device_id>/?chN=n
  3) click the send button next to url textbox
  4) after send the request if everything goes ok, you will receive a success message


### Add Data To The Database Using MQTT

Send an MQTT request using the following format:

host:*CENTRAL-SERVER-IP*
port:1883
topic: forest
protocol: mqtt/tcp

Generic:
```json
     {
            "app_key": "application key",
            "device_id": "node unique identifier",
            "net_key": "network key",
            "channels": {
                "ch1": "float as string",
                "ch2": "float as string",
                "chN": "float as string"
            }
        }
```

Example:

```json
        {
            "app_key": "1",
            "device_id": "3",
            "net_key": "2",
            "channels": {
                "ch1": "1",
                "ch2": "2"
            }
        }
```

### Get All Database Records

Send a GET request using the following API format:

Generic:
    http://**RPI-IP**:2323/sensor/all

Example:  
    http://10.0.0.115:2323/sensor/all

Add the following request headers:

Authorization=**JWT-TOKEN-GENERATED-BEFORE**

  1) open postman
  2) use http://**RPI-IP**:2323/sensor/all
  3) click the send button next to url textbox
  4) In case you have records in the db you will receive a list of json   
  ```json5
    [
        {
            "app_key": "1",
            "channels": {
                "ch1": "1",
                "ch2": "2"
            },
            "device_id": "3",
            "net_key": "2"
        },
        {
            "app_key": "dd",
            "channels": {
                "ch1": "1",
                "ch2": "2"
            },
            "device_id": "ff",
            "net_key": "ff"
        }
    ]
```  

### Upload csv File

#### Required csv Format

The first row must have the names of the columns.
The second row must have the units of the columns.
From the third line on, you will have your data.
For example:
```csv
temperature, pressure
°C, hPa
12.0, 1000.0
```

The previous will be load in the database as

|id|app_key|net_key|device_id|value|created_at|field_name|unit_string|
|---|---|---|---|---|---|---|---|
|1|from_csv|from_csv|from_csv|12.0|2014-11-2800:00:00|temperature|°C|
|2|from_csv|from_csv|from_csv|1000.0|2014-11-2800:00:00|pressure|hPa|