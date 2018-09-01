#include <SPI.h> 

/* 14.08.2018
   Arduino Uno Pin Connection
   Sensor           Arduino
   VCC -----------> 3.3V
   GND -----------> GND
   DIN(MOSI) -----> pin (11)
   DOUT(MISO) ----> pin (12)
   SCLK ----------> pin (13)
   MCLK ----------> pin (9)
*/

int clock = 9; 
 
void resetsensor() //this function keeps the sketch a little shorter 
{ 
  SPI.setDataMode(SPI_MODE0);  
  SPI.transfer(0x15); 
  SPI.transfer(0x55); 
  SPI.transfer(0x40); 
} 
 
void setup() { 
  Serial.begin(9600); 
  SPI.begin(); //see SPI library details on arduino.cc for details 
  SPI.setBitOrder(MSBFIRST);
  SPI.setClockDivider(SPI_CLOCK_DIV32); //divide 16 MHz to communicate on 500 kHz 
  pinMode(clock, OUTPUT); 
  delay(100); 
} 
 
void loop()  
{ 
  TCCR1B = (TCCR1B & 0xF8) | 1 ; //generates the MCKL signal 
  analogWrite (clock, 128) ;  
 
  resetsensor();//resets the sensor - caution: afterwards mode = SPI_MODE0! 
 
  //Calibration word 1 
  unsigned int word1 = 0; 
  unsigned int word11 = 0; 
  SPI.transfer(0x1D); //send first byte of command to get calibration word 1 
  SPI.transfer(0x50); //send second byte of command to get calibration word 1 
  SPI.setDataMode(SPI_MODE1); //change mode in order to listen 
  word1 = SPI.transfer(0x00); //send dummy byte to read first byte of word 
  word1 = word1 << 8; //shift returned byte  
  word11 = SPI.transfer(0x00); //send dummy byte to read second byte of word 
  word1 = word1 | word11; //combine first and second byte of word 
 
  resetsensor();//resets the sensor 
 
  //Calibration word 2; see comments on calibration word 1 
  unsigned int word2 = 0;  
  byte word22 = 0;  
  SPI.transfer(0x1D); 
  SPI.transfer(0x60); 
  SPI.setDataMode(SPI_MODE1);  
  word2 = SPI.transfer(0x00); 
  word2 = word2 <<8; 
  word22 = SPI.transfer(0x00); 
  word2 = word2 | word22; 
 
  resetsensor();//resets the sensor 
 
  //Calibration word 3; see comments on calibration word 1 
  unsigned int word3 = 0; 
  byte word33 = 0; 
  SPI.transfer(0x1D); 
  SPI.transfer(0x90);  
  SPI.setDataMode(SPI_MODE1);  
  word3 = SPI.transfer(0x00); 
  word3 = word3 <<8; 
  word33 = SPI.transfer(0x00); 
  word3 = word3 | word33; 
 
  resetsensor();//resets the sensor 
 
  //Calibration word 4; see comments on calibration word 1 
  unsigned int word4 = 0; 
  byte word44 = 0; 
  SPI.transfer(0x1D); 
  SPI.transfer(0xA0); 
  SPI.setDataMode(SPI_MODE1);  
  word4 = SPI.transfer(0x00); 
  word4 = word4 <<8; 
  word44 = SPI.transfer(0x00); 
  word4 = word4 | word44; 
   
  long c1 = word1 >> 1; 
  long c2 = ((word3 & 0x3F) << 6) | ((word4 & 0x3F)); 
  long c3 = (word4 >> 6) ; 
  long c4 = (word3 >> 6); 
  long c5 = (word2 >> 6) | ((word1 & 0x1) << 10); 
  long c6 = word2 & 0x3F; 
// 
//  Serial.println(c1); 
//  Serial.println(c2); 
//  Serial.println(c3); 
//  Serial.println(c4); 
//  Serial.println(c5); 
//  Serial.println(c6); 
 
  resetsensor();//resets the sensor 
 
 //Temperature: 
  unsigned int tempMSB = 0; //first byte of value 
  unsigned int tempLSB = 0; //last byte of value 
  unsigned int D2 = 0; 
  SPI.transfer(0x0F); //send first byte of command to get temperature value 
  SPI.transfer(0x20); //send second byte of command to get temperature value 
  delay(35); //wait for conversion end 
  SPI.setDataMode(SPI_MODE1); //change mode in order to listen 
  tempMSB = SPI.transfer(0x00); //send dummy byte to read first byte of value 
  tempMSB = tempMSB << 8; //shift first byte 
  tempLSB = SPI.transfer(0x00); //send dummy byte to read second byte of value 
  D2 = tempMSB | tempLSB; //combine first and second byte of value 
 
  resetsensor();//resets the sensor 
 
  //Pressure: 
  unsigned int presMSB = 0; //first byte of value 
  unsigned int presLSB =0; //last byte of value 
  unsigned int D1 = 0; 
  SPI.transfer(0x0F); //send first byte of command to get pressure value 
  SPI.transfer(0x40); //send second byte of command to get pressure value 
  delay(35); //wait for conversion end 
  SPI.setDataMode(SPI_MODE1); //change mode in order to listen 
  presMSB = SPI.transfer(0x00); //send dummy byte to read first byte of value 
  presMSB = presMSB << 8; //shift first byte 
  presLSB = SPI.transfer(0x00); //send dummy byte to read second byte of value 
  D1 = presMSB | presLSB;  
   
  const long UT1 = (c5 * 8) + 20224; 
  const long dT = (D2 - UT1);
  const long TEMP = 200 + ((dT * (c6 + 50))/1024.0); 
  const long OFF  = (c2*4) + (((c4 - 512) * dT)/4096.0); 
  const long SENS = c1 + ((c3 * dT)/1024.0) + 24576.0; 
   
  float PCOMP = ((((SENS * (D1 - 7168.0))/16384.0)- OFF)/32.0)+250.0; 
  float TEMPREAL = TEMP/10.0; 
  Serial.print("pressure =    "); 
  Serial.print(PCOMP); 
  Serial.println(" mbar"); 

  float h;

  if (PCOMP < 1045){
    h = PCOMP - 982,5;
  } else {
    h = PCOMP - 981;
  }

  // p = h * d * g calculation of water depth
  //float p = PCOMP;
  //float g = 9.80665;
  //float d = 1.0;
  //float h = p / ( d * g * 1000 );
  
  Serial.print("water depth = ");
  Serial.print(h);
  Serial.println(" cm");
 
  const long dT2 = dT - ((dT >> 7 * dT >> 7) >> 3); 
  const float TEMPCOMP = (200 + (dT2*(c6+100) >>11))/10.0; 
  Serial.print("temperature = "); 
  Serial.print(TEMPCOMP);   
  Serial.println(" °C"); 
  Serial.print("Real temperature = ");
  Serial.print(TEMPREAL);
  Serial.println(" °C"); 
  Serial.println("************************************"); 
 
  delay(1000); 
}
