#include <Adafruit_LiquidCrystal.h>

#define BUTTON_1P 10
#define BUTTON_2P 9
#define BUTTON_START 8

Adafruit_LiquidCrystal lcd(0);

unsigned int buttonCnt1 = 0;
unsigned int buttonCnt2 = 0;

unsigned long currTime = 0;
unsigned long prevTime = 0;

unsigned int gameTime = 30;

bool gameRunning = false;

void setup() {
  pinMode(BUTTON_1P, INPUT_PULLUP);
  pinMode(BUTTON_2P, INPUT_PULLUP);
  pinMode(BUTTON_START, INPUT_PULLUP);

  lcd.begin(16, 2);

  displayGame();
}

void loop() {

  // START 버튼
  if (buttonStart() == 1) {
    gameTime = 30;
    buttonCnt1 = 0;
    buttonCnt2 = 0;

    currTime = millis();
    prevTime = currTime;

    gameRunning = true;

    displayGame();
  }

  // 게임 중일 때만 점수 입력
  if (gameRunning) {

    if (button1P() == 1) {
      buttonCnt1++;
    }

    if (button2P() == 1) {
      buttonCnt2++;
    }

    // 1초마다 시간 감소
    currTime = millis();

    if (currTime - prevTime >= 1000) {
      prevTime += 1000;

      if (gameTime > 0) {
        gameTime--;
      }

      // 시간이 끝나면 게임 종료
      if (gameTime == 0) {
        gameRunning = false;
      }

      displayGame();
    }
  }
}


// =========================
// LCD 출력
// =========================

void displayGame() {

  lcd.clear();

  lcd.setCursor(3, 0);
  lcd.print("TIME: ");
  lcd.print(gameTime);

  lcd.setCursor(0, 1);
  lcd.print("1P:");
  lcd.print(buttonCnt1);

  lcd.setCursor(8, 1);
  lcd.print("2P:");
  lcd.print(buttonCnt2);
}


// =========================
// 1P 버튼
// =========================

int button1P() {

  static int oldSw = HIGH;
  int newSw = digitalRead(BUTTON_1P);

  if (newSw != oldSw) {
    oldSw = newSw;

    if (newSw == LOW) {
      delay(20);

      if (digitalRead(BUTTON_1P) == LOW) {
        return 1;
      }
    }
  }

  return 0;
}


// =========================
// 2P 버튼
// =========================

int button2P() {

  static int oldSw = HIGH;
  int newSw = digitalRead(BUTTON_2P);

  if (newSw != oldSw) {
    oldSw = newSw;

    if (newSw == LOW) {
      delay(20);

      if (digitalRead(BUTTON_2P) == LOW) {
        return 1;
      }
    }
  }

  return 0;
}


// =========================
// START 버튼
// =========================

int buttonStart() {

  static int oldSw = HIGH;
  int newSw = digitalRead(BUTTON_START);

  if (newSw != oldSw) {
    oldSw = newSw;

    if (newSw == LOW) {
      delay(20);

      if (digitalRead(BUTTON_START) == LOW) {
        return 1;
      }
    }
  }

  return 0;
}
