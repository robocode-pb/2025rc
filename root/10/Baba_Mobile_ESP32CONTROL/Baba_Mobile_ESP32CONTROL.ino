#include <WiFi.h>
#include <WebServer.h>
WebServer server(80);
void send(char c){
  Serial.print(c);
  server.send(200,"","ok");
 }
void setup() {
  WiFi.setHostname("Baba_jihala_na_velosypedi_i_vpala_v_glyboku_jamu");
  WiFi.begin("Robocode_5G","19robocode19"); 
  while(WiFi.status());

  Serial.begin(115200);
  Serial.println("We have started the mothership, awaiting your commands!");

  server.on("/L", [](){ send('L'); });
  server.on("/R", [](){ send('R'); });
  server.on("/F", [](){ send('F'); });
  server.on("/B", [](){ send('B');});
  server.on("/", [](){ server.send(200,"",R"rawliteral(
    <h1> Баба їхала на велосипеді і впала в глибоку яму </h1>
    <button onclick="fetch('/F')">я впав</button>
    <button onclick="fetch('/L')">*جغلاق جغلاق*</button>
    <button onclick="fetch('/R')">я не впав</button>
    <button onclick="fetch('/B')">hahahahahahahahahaha z yt ,f,f haha</button>
  )rawliteral");
   });

 }

void loop() {
  server.handleClient();

}
