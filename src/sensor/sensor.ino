// Define the LED pin.  The Nano 33 IoT often uses pin 13 for the built-in LED.
const int ledPin = 13;
const int amperePIN = A1; 

const float sensivity = 100;

const int ampere_msr_cnt = 10;
int ampere_index = 0;
float ampere_msrs[ampere_msr_cnt] = {};

float offsetAmpere = 1.61;

void setup() {
  Serial.begin(9600);
  
  pinMode(ledPin, OUTPUT);
  pinMode(amperePIN, INPUT);
}

void loop() {
  get_ampere_measurement();

  Serial.print(ampere_msrs[ampere_index]);
  Serial.print(",");
  Serial.print(get_average_ampere());

  delay(100);
}

float get_ampere_measurement() {  
  ampere_index = (ampere_index + 1) % ampere_msr_cnt;

  float ampereState = analogRead(amperePIN);
  float voltage = (ampereState * 5.0) / 1023.0;
  float current = (voltage - offsetAmpere) * sensivity;
  
  ampere_msrs[ampere_index] = current;
}

float get_average_ampere() {
  float avr = 0;

  for (int i = 0; i < ampere_msr_cnt; i++) {
    avr += ampere_msrs[i] / static_cast<float>(ampere_msr_cnt);
  }

  return avr;
}