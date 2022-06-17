#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ESP8266HTTPClient.h>
#include <DHTesp.h>
#include <uFire_SHT3x.h>
#include <DallasTemperature.h>
#include <OneWire.h>

int value = 0;
float vIN = 0.0;
float vOUT = 0.0;
float R1 = 30000.0;
float R2 = 7500.0;

String _appKey = "BRF-APP";
String _netKey = "BRF-NET";


OneWire oneWire(D4);
DallasTemperature sensors(&oneWire);
uFire::SHT3x sht30;
DHTesp dht;


const char* ssid = "NET-MESH-FOREST";              //Nombre de la RED
const char* password = "B4r3f2c1!+";           //Password de la RED
const char* mqtt_server_local = "192.168.0.148";
const char* mqtt_server_remote = "165.22.191.125";
const char* http_collector_server_local = "http://192.168.0.148:5002/v1/collector/";
const char* http_collector_server_remote = "http://165.22.191.125:5002/v1/collector/";
const char* HOME_TOPIC = "home";

const char* HOSTNAME = "CRITTERCAM01";
WiFiClient espClient;


PubSubClient client(espClient);

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
  WiFi.hostname(HOSTNAME);
  randomSeed(micros());
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.printf("HostName:%s\n", WiFi.hostname().c_str());
  Serial.println(WiFi.localIP());
}

String messageBuilder(String appKey, String netKey, String deviceId, String _hostname, float value){
  String buf;
    buf += "{\"AppKey\":\"";
    buf += appKey;
    buf += "\",\"NetKey\":\"";
    buf += netKey;
    buf += "\",\"DeviceId\":\"";
    buf += deviceId;
    buf += "\",\"Hostname\":\"";
    buf += String(_hostname);
    buf += "\",\"Value\":\"";
    buf += String(value, 2);
    buf += "\"}";

    Serial.println(buf);

    return buf;
}


void postRequest(String msg, String server)
{
  HTTPClient http;

  if (http.begin(espClient, server)) //Iniciar conexión
  {
    Serial.print("[HTTP] POST...\n");
    http.addHeader("Content-Type", "application/json");
    int httpCode = http.POST(msg);  // Realizar petición

    if (httpCode > 0) {
      Serial.printf("[HTTP] POST... code: %d\n", httpCode);

      if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
        String payload = http.getString();   // Obtener respuesta
        Serial.println(payload);
      }
    }
    else {
      Serial.printf("[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
    }

    http.end();
  }
  else {
    Serial.printf("[HTTP} Unable to connect\n");
  }

}


void callback(char* topic, byte* payload, unsigned int length) 
{

  String pay_load = "";
  for( int i = 0; i < length; i++ ){
    pay_load = pay_load + (char)payload[i];
    }  
  Serial.println(pay_load); // HERE IS WHERE THE MENSSAGE FROM MQTT ARRIVE
}


void reconnect() 
{
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = HOSTNAME;
    // clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      
      client.publish("forest", HOSTNAME);
      // ... and resubscribe
      //client.subscribe("forest"); // THIS IS WHERE YOU SETUP TE TOPIC
      
      } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup()
{
    Serial.begin(9600);
    setup_wifi();
    client.setKeepAlive(10);
    client.setBufferSize(8192);
    client.setServer(mqtt_server_remote,1883);
    if (!client.connected()) {
        reconnect();
    }
    sensors.begin();
    Wire.begin();
}

void loop()
{
    Serial.println("DHT22");
    float humidity = dht.getHumidity();
    float temperature = dht.getTemperature();
    Serial.println(humidity, 2);
    Serial.println(temperature, 2);
    postRequest(messageBuilder(_appKey, _netKey, "3", HOSTNAME, temperature), http_collector_server_remote);
    postRequest(messageBuilder(_appKey, _netKey, "4", HOSTNAME, humidity), http_collector_server_remote);
    delay(5000);

    Serial.println("SHT30");
    if (sht30.begin() != true)
    {
        Serial.println("not working");
    } 

    postRequest(messageBuilder(_appKey, _netKey, "5", HOSTNAME, sht30.tempC), http_collector_server_remote);
    postRequest(messageBuilder(_appKey, _netKey, "6", HOSTNAME, sht30.RH), http_collector_server_remote);
    delay(5000);

    Serial.println("DS18B20");
    sensors.requestTemperatures(); 
    float temperatureC = sensors.getTempCByIndex(0);
    Serial.print(temperatureC);
    postRequest(messageBuilder(_appKey, _netKey, "7", HOSTNAME, temperatureC), http_collector_server_remote);
    delay(5000);
    
  Serial.println("VOLTAGE sensor"); 
  value = analogRead(A0);
  Serial.println(value);
  vOUT=((value * 3.3) / 1024.0);
  vIN = vOUT / (R2/(R1+R2));
  Serial.println(vIN);
    postRequest(messageBuilder(_appKey, _netKey, "8", HOSTNAME, vIN), http_collector_server_remote);
    delay(5000);


}
