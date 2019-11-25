# Before Start
Store and Forward Node uses 
Raspbian Buster Lite 
Version: September 2019
Release date: 2019-09-26

Make sure you have the following installed on your RPI:
- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)
- [git](https://git-scm.com/)

Before running the following commands, do:
`sudo apt-get update`

To install docker:
`curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh`

To install docker-compose:
`sudo apt install python3-pip -y`

`sudo pip3 install docker-compose==1.12.0`

To install git:
`sudo apt install git -y`

To install mosquitto:

`sudo apt install mosquitto -y`

`sudo touch /etc/mosquitto/conf.d/bridge.conf`

`sudo nano /etc/mosquitto/conf.d/bridge.conf`

```
add the following:

connection bridge-central
address 157.230.15.139:1883 //replace 157.230.15.139 with ip of central server
topic forest out 0
```

`sudo systemctl restart mosquitto`


Make sure you have installed in a different machine:
- [postman](https://www.getpostman.com/)
- [mqttbox](http://workswithweb.com/html/mqttbox/downloads.html)


# What's in the box?

- postgres  as database
- flask app as rest api
- mosquitto for M2M pub/sub broker 

# Step to build the project from scratch
the build proccess with docker-compose take care of everything you need to have up and runing the project in the RPI, also the containers are setup to auto restart in case the RPI is shutdown or restarted.

    ~$ git clone https://github.com/saycel/black-rock-forest-store-forward.git
    ~$ cd black-rock-forest-store-forward-node
    ~$ sudo nano .env
    
    add the following to .env file
    
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=brfc
    PYTHONPATH=/brfc
    
    ~$ sudo docker-compose build 
    ~$ sudo docker-compose up 

In case you have any permission problems with  docker-compose, please run all docker-compose commands with sudo.

# Step to update the project
To avoid any merge conflics, **DO NOT CHANGE ANY IN THE black-forest project**, unless you know how to merge. 

    ~$ cd black-forest
    ~$ git pull 
    it will ask for gitlab credentials
    ~$ sudo docker-compose stop
    ~$ sudo docker-compose build 
    ~$ sudo docker-compose up 

# Running in Mac with Vagrant
For running the dev env in mac you need to do it with vagrant.
Follow the steps to install and run the project:

1) Install vagrant with brew. ```~$ brew install vagrant```
2) Install the docker provisioner ```~$ vagrant plugin install vagrant-docker-compose```
3) go to the root folder of the project where the **Vagrant** file is 
4) run ```~$ vagrant up```

the ip of the VM is 192.168.33.10  and have to be use as **RPI-IP** on incoming steps

# Register
To start using the platform you need to do a register first by sending a post request to http://**SERVER-IP**:2323/user/register
with the following json payload:

```json 
{	
	"email": "avalid@email.com",
	"password": "4veryS4vePass!!"
}
```

# Login
Once you are register to get a token send a post request to http://**SERVER-IP**:2323/user/register
with the following json payload:

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

# Test
In order to know if the rest api is up and running,first make sure the the pc where you installed postman and the RPI are in the same lan:

  1) get the RPI IP address
  2) in postman create a post request
     1) in the url textbox:  http://**RPI-IP**:2323/login
     2) click in the Authorization tab and choose Basic Auth type
     3) the username is german and the password is martinez
     4) click the send button next to url textbox
     5) you should receive a json response:
         {"message": "success"}

# Store Records HTTP

Follow this steps to store a new record in the database using **GET HTTP REQUEST**.  
The format of the URL is as follow:  

Generic:

http://**RPI-IP**:2323/sensor/collector/<app_key>/<net_key>/<device_id>/?chN=n

Example:

http://10.0.0.115:2323/sensor/collector/1234/abc/x1v3/?ch1=1&ch2=2

  1) open postman
  2) use http://**RPI-IP**:2323/<app_key>/<net_key>/<device_id>/?chN=n
  3) click the send button next to url textbox
  4) after send the request if everything goes ok, you will receive a success message


# Store Records MQTT

Follow this steps to store a new record in the database using **MQTT**. 
//replace 157.230.15.139 with ip of central server

The format of the message:

host:157.230.15.139  
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
                "humidity": "1",
                "temperature": "2"
            }
        }
```

  

# Get records

Follow this steps to get records in the database using a **GET HTTP REQUEST**.  

Generic:
    http://**RPI-IP**:2323/sensor/data/<page_size>/<page_number>

Example:  
    http://10.0.0.115:2323/sensor/10/1/

Add to the request headers the following:

Authorization=**JWT-TOKEN-GENERATED-BEFORE**

  1) open postman
  2) use http://**RPI-IP**:2323/sensor/data/10/1
  3) click the send button next to url textbox
  4) In case you have records in the db you will receive a list of json   
  ```json5
    [
        {
            "page": 1,
            "total_count": 2,
            "total_pages": 0
        },
        {
            "app_key": "1234",
            "created_at": "Sat, 05 Oct 2019 01:05:12 GMT",
            "device_id": "x1v3",
            "field_name": "ch1",
            "net_key": "abc",
            "value": 1.0
        },
        {
            "app_key": "1234",
            "created_at": "Sat, 05 Oct 2019 01:05:12 GMT",
            "device_id": "x1v3",
            "field_name": "ch2",
            "net_key": "abc",
            "value": 2.0
        }
    ]
```  
