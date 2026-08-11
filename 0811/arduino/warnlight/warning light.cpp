#define LED_BLUE 8
#define LED_RED 7
#define DELAY_TIME 80

void setup(){
  pinMode(LED_BLUE, OUTPUT);
  pinMode(LED_RED, OUTPUT);
}

void loop() {
  digitalWrite(LED_BLUE, HIGH);
  digitalWrite(LED_RED, LOW);
  delay(DELAY_TIME);
  digitalWrite(LED_RED, HIGH);
  digitalWrite(LED_BLUE, LOW);
  delay(DELAY_TIME);
}
