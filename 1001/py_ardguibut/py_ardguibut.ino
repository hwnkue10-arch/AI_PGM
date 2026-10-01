const int LEDpin1 = 11;
char currentMode = 'B'; // 기본 상태 OFF

void setup() {
  Serial.begin(9600);
  pinMode(LEDpin1, OUTPUT);
  digitalWrite(LEDpin1, LOW);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    if (c == 'A' || c == 'B' || c == 'C') {
      currentMode = c; // 새로운 명령이 들어왔을 때 모드 변경
    }
  }

  // 현재 모드에 따라 LED 동작 유지
  if (currentMode == 'A') {
    digitalWrite(LEDpin1, HIGH);
  } 
  else if (currentMode == 'B') {
    digitalWrite(LEDpin1, LOW);
  } 
  else if (currentMode == 'C') {
    // 점멸 모드
    digitalWrite(LEDpin1, HIGH);
    delay(300);
    digitalWrite(LEDpin1, LOW);
    delay(300);
  }
}