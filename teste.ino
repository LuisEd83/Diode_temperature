#define sensor A0

void setup(){
    Serial.begin(9600);
}

void loop(){
    int sensorValue = analogRead(sensor);
    float voltage = sensorValue * (5 / 1023.0);

    Serial.print("Voltage: ");
    Serial.print(voltage);
    Serial.println(" V");
  
  	float temperature = -(0.002 * voltage) + 0.75;

    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" C");
  
    delay(5000);
}