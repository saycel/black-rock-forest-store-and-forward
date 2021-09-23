//********************************************************************/
// First we include the libraries

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <DHTesp.h>
#include <OneWire.h> 
#include <DallasTemperature.h>

/********************************************************************/
// Data wire is plugged into pin 2 on the Arduino 
//#define ONE_WIRE_BUS 2 
#define ONE_WIRE_PIN D2

/********************************************************************/
// Setup a oneWire instance to communicate with any OneWire devices  
// (not just Maxim/Dallas temperature ICs) 
//OneWire oneWire(ONE_WIRE_BUS); 
OneWire oneWire(ONE_WIRE_PIN);
OneWire  ds(D4);
/********************************************************************/
// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);
//DallasTemperature sensors(&amp;oneWire);
/********************************************************************/ 


DHTesp dht;

const char* ssid = "NET-MESH-FOREST";                //Nombre de la RED
const char* password = "B4r3f2c1!+";           //Password de la RED
const char* mqtt_server = "192.168.128.124";   //Dirección servidor
const char* http_server = "192.168.0.148";
const char* HOSTNAME = "CritterCam_1";

WiFiClient espClient;
long lastMsg = 0;
char msg[100];
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
  WiFi.hostname(HOSTNAME);
  randomSeed(micros());
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.printf("HostName:%s\n", WiFi.hostname().c_str());
  Serial.println(WiFi.localIP());
}


void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(9600);
  setup_wifi();
 
   // Start up the library ground temp
      Serial.println("Dallas Temperature IC Control Library Demo");
   sensors.begin(); 
 // setupDHT();
}





void postRequest(String msg)
{
  HTTPClient http;

  if (http.begin(espClient, "http://165.22.191.125:5002/v1/collector/")) //Iniciar conexión
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
      Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
    }

    http.end();
  }
  else {
    Serial.printf("[HTTP} Unable to connect\n");
  }

}



void loop() {
  long currentMillis = millis();
  if (currentMillis % 180000 == 0) {

    sensors.requestTemperatures();
    
    float humidity = dht.getHumidity();
    float temperature = dht.getTemperature();
    float groundTemp = sensors.getTempCByIndex(0);
    Serial.println(sensors.getTempCByIndex(0));
    
    String buf;
    buf += "{\"AppKey\":\"CritterCam_1\",\"NetKey\":\"ESP-DHT22-temperature\",\"Hostname\":\"CritterCam_1\",\"DeviceId\":\"101\",\"Value\":\"";
    buf += String(temperature, 2);
    buf += "\"}";
    Serial.println(buf);
    postRequest(buf);
       
    String buf_1;
    buf_1 += "{\"AppKey\":\"CritterCam_1\",\"NetKey\":\"ESP-DHT22-humidity\",\"Hostname\":\"CritterCam_1\",\"DeviceId\":\"102\",\"Value\":\"";
    buf_1 += String(humidity, 2);
    buf_1 += "\"}";
    Serial.println(buf_1);
    postRequest(buf_1);

    String buf_2;
    buf_2 += "{\"AppKey\":\"CritterCam_1\",\"NetKey\":\"ESP-Ground-Temp\",\"Hostname\":\"CritterCam_1\",\"DeviceId\":\"103\",\"Value\":\"";
    buf_2 += String(groundTemp, 2);
    buf_2 += "\"}";
    Serial.println(buf_2);
    postRequest(buf_2);


    
  }
}
