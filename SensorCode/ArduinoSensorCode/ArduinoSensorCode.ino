
//Define the numbers of Rows, Columns and Total Sensor Points
#define Rows 16
#define Cols 16
#define Points Rows*Cols

//Label All The Required Digital Pins
int s01 = 2;//First 3 for the Row Muxs
int s11 = 3;
int s21 = 4;
int s02 = 5;//Next 3 for the Col Muxs
int s12 = 6;
int s22 = 7;
int inh1 = 8;//Inhibitor Pins for Each Mux
int inh2 = 9;
int inh3 = 10;
int inh4 = 11;

int x = 0;

//Label the Analog In pins
int in1 = A0;
int in2 = A1;

//Matrix of Data
int incomingValues[Points] = {};

//How Each Mux Will Be Controlled
int rowpins[] = {s01, s11, s21};
int colpins[] = {s02, s12, s22};


//Setup Each Pin to Be Availible for Write
void setup() {
  pinMode(s01, OUTPUT);
  pinMode(s11, OUTPUT);
  pinMode(s21, OUTPUT);
  pinMode(s02, OUTPUT);
  pinMode(s12, OUTPUT);
  pinMode(s22, OUTPUT);
  pinMode(inh1, OUTPUT);
  pinMode(inh2, OUTPUT);
  pinMode(inh3, OUTPUT);
  pinMode(inh4, OUTPUT);
  Serial.begin(9600);
}

//Loop Through the Rows and then the Col for each point, set the proper trace and read in from the correct Analog pin
void loop() {
  for (int i = 0; i < 16; i++){
    pinrow(i);
    for (int j = 0; j < 16;j++){
      pincol(j);
      if (j < 8){
        incomingValues[i*16 + j] = analogRead(in1);
      }else{
        incomingValues[i*16 + j] = analogRead(in2);
      }
    }
  }
  for (int k = 1; k < Points + 1; k++){
    Serial.print(incomingValues[k-1]);
    if (k == 256){
      Serial.print("\n");
      delay(1000);
    }else{
      Serial.print(", ");
    }
  }
// Printing Method
//  for (int k = 1; k < Points + 1; k++){
//    Serial.print(String(incomingValues[k-1]) + ", ");
//    Serial.print("\t");
//    if(k%16 == 0){
//      Serial.println();
//    }
//    if (k == 256){
//      Serial.println();
//      Serial.println();
//    }
//  }
//  Serial.println();
//  delay(1000);
}

//Enables the Correct Trace and Mux for the Rows
void pinrow(int pin){
  if (pin < 8){
    digitalWrite(inh1, LOW);
    digitalWrite(inh2, HIGH);
  }else{
    pin = pin-8;
    digitalWrite(inh1, HIGH);
    digitalWrite(inh2, LOW);
   }
   switch(pin){
    case 0:
      digitalWrite(rowpins[0], LOW);
      digitalWrite(rowpins[1], LOW);
      digitalWrite(rowpins[2], LOW);
      break;
    case 1:
      digitalWrite(rowpins[0], HIGH);
      digitalWrite(rowpins[1], LOW);
      digitalWrite(rowpins[2], LOW);
      break;
    case 2:
      digitalWrite(rowpins[0], LOW);
      digitalWrite(rowpins[1], HIGH);
      digitalWrite(rowpins[2], LOW);
      break;
    case 3:
      digitalWrite(rowpins[0], HIGH);
      digitalWrite(rowpins[1], HIGH);
      digitalWrite(rowpins[2], LOW);
      break;
    case 4:
      digitalWrite(rowpins[0], LOW);
      digitalWrite(rowpins[1], LOW);
      digitalWrite(rowpins[2], HIGH);
      break;
    case 5:
      digitalWrite(rowpins[0], HIGH);
      digitalWrite(rowpins[1], LOW);
      digitalWrite(rowpins[2], HIGH);
      break;
    case 6:
      digitalWrite(rowpins[0], LOW);
      digitalWrite(rowpins[1], HIGH);
      digitalWrite(rowpins[2], HIGH);
      break;
    case 7:
      digitalWrite(rowpins[0], HIGH);
      digitalWrite(rowpins[1], HIGH);
      digitalWrite(rowpins[2], HIGH);
      break;
    }
}

//Enables the Correct Trace and Mux for each Col
void pincol(int pin){
  if (pin < 8){
    digitalWrite(inh3, LOW);
    digitalWrite(inh4, HIGH);
  }else{
    pin = pin-8;
    digitalWrite(inh3, HIGH);
    digitalWrite(inh4, LOW);
   }
   switch(pin){
    case 0:
      digitalWrite(colpins[0], LOW);
      digitalWrite(colpins[1], LOW);
      digitalWrite(colpins[2], LOW);
      break;
    case 1:
      digitalWrite(colpins[0], HIGH);
      digitalWrite(colpins[1], LOW);
      digitalWrite(colpins[2], LOW);
      break;
    case 2:
      digitalWrite(colpins[0], LOW);
      digitalWrite(colpins[1], HIGH);
      digitalWrite(colpins[2], LOW);
      break;
    case 3:
      digitalWrite(colpins[0], HIGH);
      digitalWrite(colpins[1], HIGH);
      digitalWrite(colpins[2], LOW);
      break;
    case 4:
      digitalWrite(colpins[0], LOW);
      digitalWrite(colpins[1], LOW);
      digitalWrite(colpins[2], HIGH);
      break;
    case 5:
      digitalWrite(colpins[0], HIGH);
      digitalWrite(colpins[1], LOW);
      digitalWrite(colpins[2], HIGH);
      break;
    case 6:
      digitalWrite(colpins[0], LOW);
      digitalWrite(colpins[1], HIGH);
      digitalWrite(colpins[2], HIGH);
      break;
    case 7:
      digitalWrite(colpins[0], HIGH);
      digitalWrite(colpins[1], HIGH);
      digitalWrite(colpins[2], HIGH);
      break;
    }
}
