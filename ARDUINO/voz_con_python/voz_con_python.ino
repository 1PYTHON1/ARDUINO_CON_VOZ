void setup() 
{
  Serial.begin(9600,SERIAL_8N1);
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
}

void loop() 
{
int temp= analogRead(0);
float mv = (temp/1024.0)*5000;                    
temp = mv/10;

  char  led;
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

      if(led=='5')
  {
  Serial.println(temp);
  }

     if (led=='e')
     {
      bool estado1=digitalRead(13);
      bool estado2=digitalRead(12);
      bool estado3=digitalRead(11);
      bool estado4=digitalRead(10);
      if(estado1)
      Serial.println("on1");
      else 
      Serial.println("off1");
      
      if(estado2)
      Serial.println("on2");
      else 
      Serial.println("off2");
      
      if(estado3)
      Serial.println("on3");
      else 
      Serial.println("off3");

      if(estado4)
      Serial.println("on4");
      else 
      Serial.println("off4");
     }

  }
}
