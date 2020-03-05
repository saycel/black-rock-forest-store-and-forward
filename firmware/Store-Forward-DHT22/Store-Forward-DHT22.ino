//****************************************************************//
//  Name    : Store-Forward-DHT22                                 //
//  Author  : German Martinez, Edwin Reed-Sanchez                 //
//  Date    : 5 March, 2020                                       //
//  Version : 1.0                                                 //
//  Notes   : Code for WEMOS D1 (ESP8266) with DHT22              //
//          :                                                     //
//****************************************************************//

//include needed libraries

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "DHTesp.h"
#define MQTT_MAX_PACKET_SIZE = 4096
DHTesp dht;

// Input your Wifi and MQTT server credentials.  
// Ask the security administrator at Black Rock Forest or your local admin for the correct credentials. 

const char* ssid = "YOUR_WIFI";          //SSID
const char* password = "WIFI_PASSWORD";           //SSID Password
const char* mqtt_server = "XXX.XXX.XXX.XXX";   // Store and Forward Node Address (RPi or Server)

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[1000];
int value = 0;
int sensorPin = A0;

void setup_wifi() {

  delay(10);
  
 // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(2000);
    Serial.print(".");
  }

  randomSeed(micros());
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  String pay_load = "";
  for ( int i = 0; i < length; i++ ) {
    pay_load = pay_load + (char)payload[i];
  }
  Serial.println(pay_load); // HERE IS WHERE THE MENSSAGE FROM MQTT ARRIVE
}


void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      //client.publish("outTopic", "hello world");
      // ... and resubscribe
      //client.subscribe("forest"); // THIS IS WHERE YOU SETUP THE TOPIC

    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {

  Serial.begin(9600);
  Serial.setTimeout(2000);

setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  dht.setup(D2, DHTesp::DHT22);
  if (!client.connected()) {
    reconnect();
  }

  delay(500);

  Serial.println();
  Serial.print("MAC: ");
  Serial.println(WiFi.macAddress());

}

void loop() {
  client.loop();

  long now = millis();
  if (now % 5000 == 0) {

    if (String(dht.getHumidity(), 2) == String("nan")) {
      String humidity = "0.0";
      String temperature = "0.0";
      Serial.print("Temp: " + temperature + "\tHumidity: " + humidity + "  bad wiring?" + "\n");
    }
    else {

      
      String humidity = String(dht.getHumidity(), 2);//String(dht.readHumidity(), 2);
      String temperature = String(dht.getTemperature(), 2);//String(dht.readTemperature(), 2);

      Serial.print("Temp: " + temperature + "\tHumidity: " + humidity + "\n");

// change "YOUR-SENS" to the device id you want to define for your sensor.  
// You later use this id to graph the data or for your API end point.  
      
      String buf;
      buf += "{\"unit\":\"%\",\"net_key\":\"net\",\"app_key\":\"app\",\"device_id\":\"YOUR-SENS\",\"channels\":{ \"humidity\":\"";
      buf += humidity;
      buf += "\"}}";

      if (!client.publish("forest",  buf.c_str())) {
        client.publish("debug", "esp8266 messsage for humidity is too large");
      }

      buf = "{\"unit\":\"°C\",\"net_key\":\"net\",\"app_key\":\"app\",\"device_id\":\"YOUR-SENS\",\"channels\":{ \"temperature\":\"";
      buf += temperature;
      buf += "\"}}";

      if (!client.publish("forest",  buf.c_str())) {
        client.publish("debug", "esp8266 messsage for temperature is too large");
      }
      
    }

    delay(5000);

// You can enable Deep Sleep Mode; ESP.deepSleep(600e6) is for 10 min sleep intervals.    

// Serial.println("deep sleep mode for 10 min");
// ESP.deepSleep(600e6); 
  
  }

  

}
