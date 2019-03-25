# Before Start
make sure you have installed in the RPI:
-  docker
- docker-compose 
- git

make sure you hace installed in other machine:
- postman

# What's in the box?

- postgres  as database
- flask app as rest api
- mosquitto for M2M pub/sub broker 

# Step to build the project from scratch
the build proccess with docker-compose take care of everything you need to have up and runing the project in the RPI, also the containers are setup to auto restart in case the RPI is shutdown or restarted.

    ~$ git clone
    it will ask you to login with your gitlab credentials
    ~$ cd black-forest 
    ~$ docker-compose build 
    ~$ docker-compose up 

In case you have any permission problems with  docker-compose, please run all docker-compose commands with sudo.

# Step to update the project
To avoid any merge conflics, **DO NOT CHANGE ANY IN THE black-forest project**, unless you know how to merge. 

    ~$ cd black-forest
    ~$ git pull 
    it will ask for gitlab credentials
    ~$ docker-compose stop
    ~$ docker-compose build 
    ~$ docker-compose up 

# Test
In order to know if the rest api is up and running,first make sure the the pc where you installed postman and the RPI are in the same lan:

  1) get the RPI IP address
  2) in postman create a post request
     1) in the url textbox:  http://**RPI-IP**:2323/login
     2) click in the Authorization tab and in type choose Basic Auth
     3) the the username is german and the password is martinez
     4) click the send button next to url textbox
     5) you should recevie al json response:
         {"message": "success"}



