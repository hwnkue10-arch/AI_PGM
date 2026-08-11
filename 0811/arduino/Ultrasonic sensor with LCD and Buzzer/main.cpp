// C++ code
//
#include <Adafruit_LiquidCrystal.h>

Adafruit_LiquidCrystal lcd(0); 

// Define the ultrasonic sensor pins
const int trigPin = 9;
const int echoPin = 10;

// Define the buzzer pin
const int buzzerPin = A0;

void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.print("Initializing...");

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  
  delay(2000);
  lcd.clear();
  lcd.print("Ready");
  delay(1000);
}

 void loop() {
  long duration, distance;
     digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH); // measure the time it takes to travel 
  distance = duration * 0.034 / 2; //34cm ms divide 2 is half of total distance

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Distance: ");
  

  if (distance >= 70 || distance <= 0) {
    lcd.print("Out of range");
    noTone(buzzerPin); 
  } else {
    lcd.print(distance);
    lcd.print(" cm");


    if (distance > 60) {
      tone(buzzerPin, 2500); // Play a tone at 2500Hz for distances greater than 60 cm
    } else if (distance > 20) {
      tone(buzzerPin, 1500); // Play a tone at 1500Hz for distances between 20 and 60 cm
    } else if (distance > 1) {
      tone(buzzerPin, 500); // Play a tone at 500Hz for distances less than 20 cm
    }
  }

  delay(500);
}
