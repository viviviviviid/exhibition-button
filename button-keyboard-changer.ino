const int button1 = 15;
const int button2 = 14;
const int button3 = 16;

void setup() {
  Serial.begin(9600);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
}

void loop() {
  if (digitalRead(button1) == HIGH) {
    Serial.println("1");
    delay(200);
  }
  if (digitalRead(button2) == HIGH) {
    Serial.println("2");
    delay(200);
  }
  if (digitalRead(button3) == HIGH) {
    Serial.println("3");
    delay(200);
  }
}
