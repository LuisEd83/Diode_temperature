#include <Wire.h>
#define sensor A0

void setup(){
    Serial.begin(9600);
}

void loop(){
    int sensorValue = analogRead(sensor);
    float voltage = sensorValue * (5.0 / 1023.0);

    Serial.print("Voltage: ");
    Serial.print(voltage);
    Serial.println(" V");

    // Wait for a second before the next reading:
    delay(1000);
}