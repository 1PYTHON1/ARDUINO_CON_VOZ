void setup() 
{
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
}

void loop() 
{
  char led;
  if(Serial.available()==1)
  {
     led = Serial.read();
     if(led=='1')
     {
      digitalWrite(13,!digitalRead(13));
      //condicionamos para mandar el estado actual del led 
      if(digitalRead(13))
      Serial.println("on");
      if(!digitalRead(13))
      Serial.println("off");
     }
     if(led=='2')
     {
      digitalWrite(12,!digitalRead(12));
      //condicionamos para mandar el estado actual del led 
      if(digitalRead(12))
      Serial.println("on");
      if(!digitalRead(12))
      Serial.println("off");
      }
     if(led=='3')
     {
      digitalWrite(11,!digitalRead(11));
      //condicionamos para mandar el estado actual del led 
      if(digitalRead(11))
      Serial.println("on");
      if(!digitalRead(11))
      Serial.println("off");
      }
     if(led=='4')
     {
      digitalWrite(10,!digitalRead(10));
      //condicionamos para mandar el estado actual del led 
      if(digitalRead(10))
      Serial.println("on");
      if(!digitalRead(10))
      Serial.println("off");
      }

  }
}
