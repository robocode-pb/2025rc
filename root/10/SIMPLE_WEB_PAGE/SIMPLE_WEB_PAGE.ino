#include <Wire.h>
#include <LiquidCrystal_I2C.h>

int l = 0;
int ec = 0;
int e1 = 0;
//Fixed by RoboCode
LiquidCrystal_I2C lcd_27(0x27, 16, 2);
int el = 0;

void setup()
{
  pinMode(2, INPUT);
  lcd_27.begin ();
  lcd_27.backlight();
  l = 0;
  ec = 0;
  e1 = 0;
}

void loop()
{
  if (digitalRead(2))
  {
    l = 1;
  }
  else
  {
    l = 2;
  }
  lcd_27.setCursor(1-1, l-1);
  lcd_27.print( "@" );
  lcd_27.setCursor(ec-1, el-1);
  lcd_27.print( "<-" );
  ec = ( ec - 1 );
  if (ec < 1)
  {
    ec = 16;
    e1 = 	random( 0 , 3 );
  }
  delay(100);
  lcd_27.clear();
}
