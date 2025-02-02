// Define the LED pin.  The Nano 33 IoT often uses pin 13 for the built-in LED.
const int ledPin = 13;
const int amperePIN = A1; 
const int StatusLedRot = A3;
const int StatusLedGrun = A2;

const float sensivity = 10000;

float offsetAmpere = 2.51;

void setup() {
  Serial.begin(9600);
  
  pinMode(ledPin, OUTPUT);
  pinMode(amperePIN, INPUT);
  pinMode(StatusLedRot, INPUT);
  pinMode(StatusLedGrun, INPUT);
}

void loop() {
  Serial.print(get_ampere_measurement());
  Serial.print(",");
  Serial.print(analogRead(StatusLedRot));
  Serial.print(",");
  Serial.println(analogRead(StatusLedGrun));

  delay(100);
}

float get_ampere_measurement() {  
  float ampereState = analogRead(amperePIN);
  float voltage = (ampereState * 5.0) / 1023.0;
  float current = (voltage - offsetAmpere) * (sensivity);

  return current;
}