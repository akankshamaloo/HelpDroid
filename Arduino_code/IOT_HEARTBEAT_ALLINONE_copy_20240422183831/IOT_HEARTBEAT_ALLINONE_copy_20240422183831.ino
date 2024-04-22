#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include "MAX30105.h"
#include "spo2_algorithm.h"

// WiFi credentials
const char* ssid = "rick";
const char* password = "rick";

// Flask server address
const char* serverName = "http://192.168.1.3:5000/sensing"; // Replace with your server's IP address

// LED Pin
const int ledPin = 2; // Use GPIO 2 for the LED

MAX30105 particleSensor;

// Heart rate and SpO2 calculation variables
const int RATE_SIZE = 4; // Number of readings to average for heart rate
byte rates[RATE_SIZE];
byte rateSpot = 0;
long lastBeat = 0;

float beatsPerMinute;
int beatAvg;

uint32_t irBuffer[100];  // IR LED sensor data
uint32_t redBuffer[100]; // Red LED sensor data
int32_t bufferLength = 100; // Buffer length
int32_t spo2 = 0;
int8_t validSpo2 = 0;
int32_t heartRate = 0;
int8_t validHeartRate = 0;

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT); // Initialize the LED pin as an output

  // First, attempt to initialize the MAX30105 sensor
  if (!particleSensor.begin(Wire, I2C_SPEED_STANDARD)) { // Adjust for your setup, possibly use I2C_SPEED_FAST
    Serial.println("MAX30105 was not found. Please check wiring/power.");
    while (1); // Infinite loop to halt further execution
  }

  particleSensor.setup(); // Configure sensor with default settings
  particleSensor.setPulseAmplitudeRed(0x0A); // Adjust if necessary

  // Now, connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
  digitalWrite(ledPin, HIGH); // Turn on the LED when connected to WiFi
}

void loop() {
  // Collect data
  readHeartRateAndSpO2();

  // Send data to server if WiFi is connected
  if(WiFi.status() == WL_CONNECTED){
    sendSensorData();
  } else {
    Serial.println("WiFi not connected");
    digitalWrite(ledPin, LOW); // Optionally, turn off the LED if disconnected
  }

  delay(5000); // Adjust delay  
}

void readHeartRateAndSpO2() {
  for (int i = 0; i < bufferLength; i++) {
    while (particleSensor.available() == false) // Wait for a measurement
      particleSensor.check(); // Check the sensor for new data
    
    redBuffer[i] = particleSensor.getRed();
    irBuffer[i] = particleSensor.getIR();
    particleSensor.nextSample(); // Move to next sample
  }

  // Calculate heart rate and SpO2 after filling up the buffers
  maxim_heart_rate_and_oxygen_saturation(irBuffer, bufferLength, redBuffer, &spo2, &validSpo2, &heartRate, &validHeartRate);
}

void sendSensorData() {
  HTTPClient http;
  http.begin(serverName);
  http.addHeader("Content-Type", "application/json");
  
  StaticJsonDocument<300> doc;
  doc["temperature"] = particleSensor.readTemperature();
  doc["heartRate"] = heartRate;
  doc["spo2"] = spo2;
  
  String requestBody;
  serializeJson(doc, requestBody);
  Serial.print("Sending JSON payload: ");
  Serial.println(requestBody);
  
  int httpResponseCode = http.POST(requestBody);
  Serial.print("HTTP Response code: ");
  Serial.println(httpResponseCode);
  
  http.end();
}
