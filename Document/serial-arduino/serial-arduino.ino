void setup() {
  Serial.begin(115200);
  Serial.setTimeout(5);
}

void loop() {
  int x, y;
  if (Serial.available()) {
    while (Serial.available()) {
      byte incomingByte = Serial.read();
      //Serial.write(incomingByte);
      if (incomingByte == 'x') x = Serial.parseInt();
      if (incomingByte == 'y') y = Serial.parseInt();
    }
    Serial.println("\tx : " + String(x) + "\ty : " + String(y));
  }
}
