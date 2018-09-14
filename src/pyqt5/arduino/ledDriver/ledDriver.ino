int IncomeByte = 0;
int LEDPin = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // Wait until the serial communication is established
  while(!Serial);
  Serial.println("Communication established.");
  pinMode(LEDPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0 ) {
    
    IncomeByte = Serial.read();
    Serial.print("Reading ");
    Serial.print(IncomeByte);
    Serial.print("\n"); 
    
    if (IncomeByte == '0') {
      
      // Input = 0: Turn the LED off
      Serial.println("LED reset, the lights should be turned off now...");
      digitalWrite(LEDPin, LOW);
      
    } else if (IncomeByte == '1') {
      
      // Input = 1: Turn the LED on
      Serial.println("LED set, the lights should be turned on now...");
      digitalWrite(LEDPin, HIGH);
      
    } else if (IncomeByte == '9') {
      
      // Input = 9: Checking if there is an arduino running properly
      Serial.println("Alive");
      
    }
  }
}
