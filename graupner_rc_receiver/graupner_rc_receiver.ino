// 1 on receiver is throttle
// 2 on receiver is steering
// 5 on receiver is switch 6
// 6 on receiver is switch 8

const int receiverPins[4] = {5, 6, 7, 8};  // Pins connected to the receiver channels
unsigned long durations[4];

void setup() {
  Serial.begin(38400);
  for (int i = 0; i < 4; i++) {
    pinMode(receiverPins[i], INPUT);
  }
}

void loop() {
  for (int i = 0; i < 4; i++) {
    durations[i] = pulseIn(receiverPins[i], HIGH);
  }

  // Print the values for debugging
//  Serial.print("Throttle: ");
//  Serial.print(durations[0]);
//  Serial.print(" | Steering: ");
//  Serial.print(durations[1]);
//  Serial.print(" | Switch 6: ");
//  Serial.print(durations[2]);
//  Serial.print(" | Switch 8: ");
//  Serial.println(durations[3]);
}
