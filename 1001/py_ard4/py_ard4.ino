char cmd;
void setup() {
  Serial.begin(9600);}
void loop() {
  if (Serial.available()) {
    cmd = Serial.read();
    if(cmd=='a'){
      Serial.println("GOOD: A");
      delay(100);
    }
    else if (cmd=='b'){
      Serial.println("GOOD: B");
      delay(100);
    }
   }
}