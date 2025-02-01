// Define the LED pin.  The Nano 33 IoT often uses pin 13 for the built-in LED.
const int ledPin = 13;

void setup() {
  // Initialize the LED pin as an output.
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Turn the LED on.
  digitalWrite(ledPin, HIGH);  // HIGH means on for most LEDs
  delay(300);                  // Wait for one second.

  // Turn the LED off.
  digitalWrite(ledPin, LOW);   // LOW means off for most LEDs
  delay(300);                  // Wait for one second.
}