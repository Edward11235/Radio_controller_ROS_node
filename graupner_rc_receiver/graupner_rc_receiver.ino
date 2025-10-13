const int receiverPins[5] = {5, 7, 9, 10, 1};  // Pins connected to the receiver channels including the joystick
unsigned long durations[5];  // Increased the size to accommodate the joystick

void setup() {
  Serial.begin(38400);
  for (int i = 0; i < 5; i++) {
    pinMode(receiverPins[i], INPUT);
  }
}

void loop() {
  for (int i = 0; i < 5; i++) {
    durations[i] = pulseIn(receiverPins[i], HIGH);
  }

  // Print the values for debugging
  Serial.print("Throttle: ");
  Serial.print(durations[0]);
  Serial.print(" | Steering: ");
  Serial.print(durations[1]);
  Serial.print(" | Switch 6: ");
  Serial.print(durations[2]);
  Serial.print(" | Switch 8: ");
  Serial.print(durations[3]);
  Serial.print(" | Lateral: ");
  Serial.println(durations[4]);
}

