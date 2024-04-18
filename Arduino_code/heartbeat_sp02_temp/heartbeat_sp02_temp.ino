#include <Wire.h>
#include "MAX30105.h"
#include "spo2_algorithm.h"

MAX30105 particleSensor;

const int RATE_SIZE = 4; // Number of readings to average for heart rate
byte rates[RATE_SIZE];
byte rateSpot = 0;
long lastBeat = 0;

float beatsPerMinute;
int beatAvg;

uint32_t irBuffer[100];
uint32_t redBuffer[100];
int32_t bufferLength = 100;
int32_t spo2 = 0;
int8_t validSpo2 = 0;
int32_t heartRate = 0;
int8_t validHeartRate = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("Initializing...");

  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) {
    Serial.println("MAX30105 was not found. Please check wiring/power.");
    while (1);
  }

  particleSensor.setup(); // Configure sensor with default settings
  particleSensor.setPulseAmplitudeRed(0x0A); // Adjust if necessary
  particleSensor.setPulseAmplitudeGreen(0); // Turn off Green LED
}

void loop() {
  readTemperature();
  delay(1000); // Delay to prevent overwhelming the sensor and the serial output

  readHeartRateAndSpO2();
  delay(1000); // Adjust based on your needs

  readHeartRatePBA();
  delay(1000); // Adjust based on your needs
}

void readTemperature() {
  float temperature = particleSensor.readTemperature();
  Serial.print("Temperature: ");
  Serial.print(temperature, 4);
  Serial.println(" C");
}

void readHeartRateAndSpO2() {
  for (int i = 0; i < bufferLength; i++) {
    while (particleSensor.available() == false) // Wait for a measurement
      particleSensor.check(); // Check the sensor for new data

    redBuffer[i] = particleSensor.getRed();
    irBuffer[i] = particleSensor.getIR();
    particleSensor.nextSample();
  }

  maxim_heart_rate_and_oxygen_saturation(irBuffer, bufferLength, redBuffer, &spo2, &validSpo2, &heartRate, &validHeartRate);

  Serial.print("Heart Rate: ");
  Serial.print(heartRate);
  Serial.print(" BPM | SpO2: ");
  Serial.print(spo2);
  Serial.println("%");
}

void readHeartRatePBA() {
  long irValue = particleSensor.getIR();

  if (irValue < 50000) {
    Serial.println("No finger detected.");
    return;
  }

  bool beatDetected = checkForBeat(irValue);
  if (beatDetected) {
    long delta = millis() - lastBeat;
    lastBeat = millis();

    beatsPerMinute = 60 / (delta / 1000.0);

    if (beatsPerMinute < 255 && beatsPerMinute > 20) {
      rates[rateSpot++] = (byte)beatsPerMinute;
      rateSpot %= RATE_SIZE;

      beatAvg = 0;
      for (byte x = 0; x < RATE_SIZE; x++) {
        beatAvg += rates[x];
      }
      beatAvg /= RATE_SIZE;
    }
  }

  Serial.print("IR=");
  Serial.print(irValue);
  Serial.print(", BPM=");
  Serial.print(beatsPerMinute);
  Serial.print(", Avg BPM=");
  Serial.println(beatAvg);
}

bool checkForBeat(long irValue) {
  // This function should implement the PBA algorithm to detect heart beats
  // Placeholder for simplicity; you'll need to integrate your own or a library's PBA here
  return false; // Default to false unless implemented
}