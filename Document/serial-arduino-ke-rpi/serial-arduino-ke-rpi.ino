int data;
void setup()
{
  Serial.begin(115200);
}

void loop()
{
  data = analogRead(A0);
  Serial.println(String(data));
  delay(1000);
  Serial.flush();
}
