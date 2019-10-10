char  serialData;
int led1 = 6;
int led2 = 5;

void setup()
{
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    serialData = Serial.read();
    Serial.print(serialData);

    if (serialData == '0') {
      digitalWrite(led1, LOW);
    } else if (serialData == '1') {
      digitalWrite(led1, HIGH);
    } else if (serialData == '2') {
      digitalWrite(led2, LOW);
    } else if (serialData == '3') {
      digitalWrite(led2, HIGH);
    } else if (serialData == '4') {
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);
    } else if (serialData == '5') {
      digitalWrite(led1, HIGH);
      digitalWrite(led2, HIGH);
    }
  }
}
