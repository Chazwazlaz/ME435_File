const int LED_PIN = LED_BUILTIN;

String inputString = "";
bool isStringComplete = false;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  inputString.reserve(200);
}

void loop() {
  if (isStringComplete) {
    inputString.trim();

    if (inputString.equals("LED ON")) {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED On");
    } else if (inputString.equals("LED OFF")) {
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED Off");
    } else if (inputString.startsWith("FLASH ")) {
      String args = inputString.substring(6);
      int spaceIndex = args.indexOf(" ");
      int numFlashes = args.substring(0, spaceIndex).toInt();
      int periodMs = args.substring(spaceIndex + 1).toInt();

      Serial.print("Flashes = ");
      Serial.print(numFlashes);
      Serial.print("  PeriodMs = ");
      Serial.println(periodMs);

      for (int i = 0; i < numFlashes; i++) {
        digitalWrite(LED_PIN, HIGH);
        delay(periodMs / 2);
        digitalWrite(LED_PIN, LOW);
        delay(periodMs / 2);
      }
    } else {
      Serial.print("Unknown command --> ");
      Serial.println(inputString);
    }

    inputString = "";
    isStringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      isStringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}