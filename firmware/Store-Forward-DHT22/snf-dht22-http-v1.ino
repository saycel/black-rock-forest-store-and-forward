
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <DHTesp.h>
DHTesp dht;

const char* ssid = "MyAlt";                   //Nombre de la RED
const char* password = "";           //Password de la RED
const char* mqtt_server = "192.168.128.124";   //Dirección servidor
const char* http_server = "192.168.0.148";
const char* HOSTNAME = "esp01";

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
  if (currentMillis % 30000 == 0) {
    float humidity = dht.getHumidity();
    float temperature = dht.getTemperature();
    
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


    
  }
}
