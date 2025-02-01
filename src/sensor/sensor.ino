// Define the LED pin.  The Nano 33 IoT often uses pin 13 for the built-in LED.
const int ledPin = 13;
const int kapazPIN = 7;
const int induktPIN = 8;
const int amperePIN = A1; 

const float sensivity = 100;

float offsetAmpere = 1.61;
int ampere_index = 0;
float ampere_measurements[] = {0.0, 0.0, 0.0};

void setup() {
  // Initialize the LED pin as an output.
  Serial.begin(9600);
  
  pinMode(ledPin, OUTPUT);
  pinMode(induktPIN, INPUT);
  pinMode(kapazPIN, INPUT);
  pinMode(amperePIN, INPUT);
}

void loop() {
  int kapazState = digitalRead(kapazPIN);
  int induktState = digitalRead(induktPIN);

  ampere_measurements[ampere_index] =  analogRead(amperePIN);
  
  float average_ampere = get_average_ampere();

  // if(kapazState == HIGH){
  //   Serial.println("Kapaz erkannt");
  // } else{
  //   Serial.println("keine Kapaz erkannt");
  // }

  // if(induktState == LOW){
  //   Serial.println("indukt erkannt");
  // } else{
  //   Serial.println("keine Indukt erkannt");
  // }

  Serial.println(average_ampere);
  digitalWrite(ledPin,HIGH);

  delay(100);

// // Turn the LED on.
//   digitalWrite(ledPin, HIGH);  // HIGH means on for most LEDs
//   delay(300);                  // Wait for one second.
//   // Turn the LED off.
//   digitalWrite(ledPin, LOW);   // LOW means off for most LEDs
//   delay(300);                  // Wait for one second.
}

float get_ampere_measurement() {  
  float ampereState = analogRead(amperePIN);
  float voltage = (ampereState * 5.0) / 1023.0;
  float current = (voltage - offsetAmpere) * sensivity;
  ampere_measurements[ampere_index] = current;

  ampere_index = (ampere_index++) % 3;
}

float get_average_ampere() {
  float avr = 0;

  for (int i = 0; i < 3; i++) {
    avr += ampere_measurements[i] / 3.0;
  }

  return avr;
}