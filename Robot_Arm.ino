#include <Servo.h>
#define numOfValsRec 5
#define digitsPerValRec 1

Servo thumb;
Servo index; 
Servo middle; 
Servo ring; 
Servo pinky;  

int valsRec[numOfValsRec];
int stringLength = numOfValsRec * digitsPerValRec+1; 
int counter = 0; 
bool counterStart = false; 
String recievedString; 

void setup() {
  Serial.begin(9600);
  thumb.attach(7);
  index.attach(8);
  middle.attach(9);
  ring.attach(10);
  pinky.attach(11);
}

void recieveData(){
  while(Serial.available()){
    char c = Serial.read();

     if (c == '$'){
      counterStart = true; 
     }
     
     if(counterStart){
      if(counter < stringLength){
        recievedString = String(recievedString+c);
        counter++;
      }
      if(counter >= stringLength){
        for(int i = 0; i < numOfValsRec; i++){
          int num = (i*digitsPerValRec)+1;
          valsRec[i] = recievedString.substring(num, num + digitsPerValRec).toInt();
        
        }
        recievedString = "";
        counter = 0; 
        counterStart = false;
      }
     }
  }
}

void loop() {
  recieveData(); 
  if (valsRec[0] == 1){thumb.write(180);}else{thumb.write(0);}
  if (valsRec[1] == 1){index.write(180);}else{index.write(0);}
  if (valsRec[2] == 1){middle.write(180);}else{middle.write(0);}
  if (valsRec[3] == 1){ring.write(180);}else{ring.write(0);}
  if (valsRec[4] == 1){pinky.write(180);}else{pinky.write(0);}

}