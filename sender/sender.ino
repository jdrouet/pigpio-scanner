#include "RH_ASK.h"
#include <SPI.h>

#define RF_MESSAGE_SIZE 80
#define RF_SPEED 2000
#define RF_RX_PIN 11
#define RF_TX_PIN 12
#define RF_REPEAT 5
#define SERIAL_SPEED 4800
#define SLEEP_DELAY 60000

RH_ASK driver(RF_SPEED, RF_RX_PIN, RF_TX_PIN, 0);
uint8_t iteration = 0;

void send_state(uint8_t index) {
  char msg[RF_MESSAGE_SIZE];

  sprintf(msg, "ping %3d", index);

  driver.send((uint8_t *)msg, strlen(msg));
  driver.waitPacketSent();
}

void setup()
{
  Serial.begin(SERIAL_SPEED);
  if (!driver.init()) {
    Serial.println("init rf failed");
  }
}

void loop()
{
  send_state(iteration++);
  delay(SLEEP_DELAY);
}
