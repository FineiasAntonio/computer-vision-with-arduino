const int ledPin = LED_BUILTIN;
String comando;

void setup() {
  Serial.begin(115200);

  pinMode(ledPin, OUTPUT);

  digitalWrite(ledPin, HIGH);
  delay(500);
  digitalWrite(ledPin, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    comando = Serial.readStringUntil('\n');

    piscarLed(1, 100);

    if (comando  == "SINAL_ROCK") {
      piscarLed(3, 200);
    }

    if (comando == "MAO_FECHADA") {
      digitalWrite(ledPin, HIGH);
      delay(1000);
      digitalWrite(ledPin, LOW);
    }
  }
}

void piscarLed(int vezes, int duracao) {
  for (int i = 0; i < vezes; i++) {
    digitalWrite(ledPin, HIGH);
    delay(duracao);
    digitalWrite(ledPin, LOW);
    delay(duracao);
  }
}
