String htmlControl = R"rawliteral(
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Uhhhhhhhhhhhh</title>
    <style>
        body {
            font-family: sans-serif;
            text-align: center;
            background: #000000;
            color: #64deff;
        }

        img {
            max-width: 100%;
            max-height: 300px;
            border: 2px solid #333;
            margin: 20px auto;
            display: block;
        }

        .controls {
            display: grid;
            grid-template-columns: repeat(5, 100px);
            grid-gap: 10px;
            justify-content: center;
            margin-top: 10px;
        }

        button {
            padding: 10px; border-radius:10% ;
            font-size: 18px; border-style: none;
            cursor: pointer; background-color: #4acfff;
        }
        #bS{
            width: 50px;
            background-color: #cf0202;
        }
    </style>
</head>

<body>
    <h2>11100010 10000010 10110100 01000101 01010011 01010000 00110011 00110010 00100000 01000011 01100001 01110010 00100000 01000011 01101111 01101110 01110100 01110010 01101111 01101100 01100101 01110010 00100000 01101111 01101110 00100000 01010100 01100001 01111000 01000101 01110110 01100001 01110011 01101001 01101111 01101110 00100000 01100001 01101110 01100100 00100000 01000010 01101001 01110000 01000010 01110101 01110000 11100010 10000010 10110100</h2>
    <img id="cam" alt="Camera Feed">
    <div class="controls">
        <button onclick="sendCommand('F')">↑</button>
        <div></div>
        <div></div>
        <div></div>
        <button onclick="sendCommand('B')">↓</button>
        <button onclick="sendCommand('L')">←</button>
        <div></div>
        <div></div>
        <button id="bS" onclick="sendCommand('S')">■</button>
        <button onclick="sendCommand('R')">→</button>
        <div></div>
        <div></div>
    </div>

    <script>

        async function sendCommand(cmd) {
            try {
                await fetch(`/cmd?cmd=${cmd}`);
                console.log("Sent via HTTP:", cmd);
            } catch (err) {
                console.error("HTTP send failed:", err);
            }
        }

        // Автоматично підключити стрім камери
        document.getElementById("cam").src = `http://${location.hostname}:81/stream`;
    </script>
</body>

</html>
)rawliteral";

#include "esp_camera.h"
#include <WiFi.h>

#define CAMERA_MODEL_AI_THINKER 

#include "camera_pins.h"

#include <HardwareSerial.h>
HardwareSerial leo(2);

void startCameraServer();

void WiFiBegin(const char* ssid,const char* password){
  pinMode(33, OUTPUT);

  WiFi.begin("Robocode_5G_old", "19robocode19");
  WiFi.setSleep(false);
  int wifiTime = 3;
  while (WiFi.status() != WL_CONNECTED and wifiTime) {
    wifiTime--;
    delay(500);
    digitalWrite(33, 0);
    delay(500);
    digitalWrite(33, 1);
    Serial.print(".");
  }

  WiFi.begin(ssid, password);
  WiFi.setSleep(false);
  
  Serial.print("WiFi connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    digitalWrite(33, 0);
    delay(500);
    digitalWrite(33, 1);
    Serial.print(".");
  }
  
  Serial.println("WiFi connected");
  Serial.print("Camera Ready! Use http://");
  Serial.println(WiFi.localIP());
  Serial.print("tesr! Use http://");
  Serial.print(WiFi.localIP());
  Serial.println("/cmd?cmd=test");
}

void CamBegin(){
   Serial.setDebugOutput(true);
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.frame_size = FRAMESIZE_UXGA;
  config.pixel_format = PIXFORMAT_JPEG;  // for streaming
  //config.pixel_format = PIXFORMAT_RGB565; // for face detection/recognition
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 12;
  config.fb_count = 1;

  // if PSRAM IC present, init with UXGA resolution and higher JPEG quality
  //                      for larger pre-allocated frame buffer.
  if (config.pixel_format == PIXFORMAT_JPEG) {
    if (psramFound()) {
      config.jpeg_quality = 10;
      config.fb_count = 2;
      config.grab_mode = CAMERA_GRAB_LATEST;
    } else {
      // Limit the frame size when PSRAM is not available
      config.frame_size = FRAMESIZE_SVGA;
      config.fb_location = CAMERA_FB_IN_DRAM;
    }
  } else {
    // Best option for face detection/recognition
    config.frame_size = FRAMESIZE_240X240;
#if CONFIG_IDF_TARGET_ESP32S3
    config.fb_count = 2;
#endif
  }

#if defined(CAMERA_MODEL_ESP_EYE)
  pinMode(13, INPUT_PULLUP);
  pinMode(14, INPUT_PULLUP);
#endif

  // camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  sensor_t *s = esp_camera_sensor_get();
  // initial sensors are flipped vertically and colors are a bit saturated
  if (s->id.PID == OV3660_PID) {
    s->set_vflip(s, 1);        // flip it back
    s->set_brightness(s, 1);   // up the brightness just a bit
    s->set_saturation(s, -2);  // lower the saturation
  }
  // drop down frame size for higher initial frame rate
  if (config.pixel_format == PIXFORMAT_JPEG) {
    s->set_framesize(s, FRAMESIZE_QVGA);
  }

#if defined(CAMERA_MODEL_M5STACK_WIDE) || defined(CAMERA_MODEL_M5STACK_ESP32CAM)
  s->set_vflip(s, 1);
  s->set_hmirror(s, 1);
#endif

#if defined(CAMERA_MODEL_ESP32S3_EYE)
  s->set_vflip(s, 1);
#endif

// Setup LED FLash if LED pin is defined in camera_pins.h
//#if defined(LED_GPIO_NUM)
//  setupLedFlash(LED_GPIO_NUM);
//#endif

}


#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

const char* nameBT     = "ESP32-Node-1";
String handleCommand(String cmd);

// UUID'и не змінюємо
#define SERVICE_UUID        "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
#define CHARACTERISTIC_UUID "6e400002-b5a3-f393-e0a9-e50e24dcca9e"

class CommandCallback : public BLECharacteristicCallbacks {
  void onWrite(BLECharacteristic *pCharacteristic) {
    String cmd = pCharacteristic->getValue().c_str();  // <-- ключове
    if (cmd.length() > 0) {
      Serial.println("BT: "+cmd);
      handleCommand(cmd);
    }
  }
};

void BtBegin(){
  // УНІКАЛЬНА НАЗВА ДЛЯ КОЖНОГО ESP32
  BLEDevice::init(nameBT); // Зміни на "ESP32-Node-2", "ESP32-Node-3" і т.д.

  BLEServer *pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService(SERVICE_UUID);

  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
    CHARACTERISTIC_UUID,
    BLECharacteristic::PROPERTY_WRITE
  );
  pCharacteristic->setCallbacks(new CommandCallback());

  pService->start();
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pAdvertising->start();

  Serial.print("BLE: ");
  Serial.println(nameBT);
  
}
