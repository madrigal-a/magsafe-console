# Prototipo en protoboard: conexiones

Objetivo: comprobar pantalla, SD, audio, botones y Retro-Go antes de pedir la PCB. La PCB usará exactamente estos mismos pines.

**Estado: sin probar.** Al armarlo, anota aquí cualquier cambio.

## Piezas

| Pieza | Nota |
|---|---|
| Placa ESP32-S3 N16R8 (módulo ESP32-S3-WROOM-1) | La ESP32-WROOM-32 no sirve para Retro-Go: no tiene PSRAM |
| Pantalla IPS 2.4" 320×240, ST7789, SPI | Versión en módulo con pines |
| Módulo SD HW-203 | Con la microSD en su adaptador |
| Módulo MAX98357A + bocina de 8 Ω | |
| 11 botones táctiles | El botón MENU es el BOOT de la placa |

Todo se alimenta del pin **3V3** de la placa y comparte **GND**.

## Pantalla (bus SPI2)

| Pantalla | ESP32-S3 |
|---|---|
| VCC | 3V3 |
| GND | GND |
| SCL / SCK | GPIO 12 |
| SDA / MOSI | GPIO 11 |
| CS | GPIO 10 |
| DC / RS | GPIO 9 |
| RES / RST | GPIO 14 |
| BLK / LED | GPIO 13 |

Si el módulo no tiene pin CS, deja GPIO 10 sin conectar.

## Tarjeta SD, módulo HW-203 (bus SPI3)

| HW-203 | ESP32-S3 |
|---|---|
| +3.3 | 3V3 |
| GND | GND |
| SCK | GPIO 16 |
| MOSI | GPIO 15 |
| MISO | GPIO 17 |
| CS | GPIO 18 |

El pin **+5** se queda sin conectar.

## Audio, MAX98357A

| MAX98357A | ESP32-S3 |
|---|---|
| VIN | 3V3 (o 5V para más volumen) |
| GND | GND |
| BCLK | GPIO 40 |
| LRC | GPIO 41 |
| DIN | GPIO 42 |
| SD, GAIN | Sin conectar |

La bocina va a las terminales + y − del módulo.

## Botones

Cada botón va de su pin a **GND**. No llevan resistencias: se usa el pull-up interno.

| Botón | GPIO |
|---|---|
| Arriba | 4 |
| Abajo | 5 |
| Izquierda | 6 |
| Derecha | 7 |
| A | 8 |
| B | 21 |
| Start | 47 |
| Select | 48 |
| Menu | 0 (botón BOOT de la placa) |
| Option | 39 |
| L | 2 |
| R | 38 |

En algunas placas el LED RGB está en GPIO 48 o 38. No estorba, pero puede parpadear al presionar Select o R.

## Batería (solo en la PCB)

GPIO 1 mide la batería a través de un divisor de dos resistencias iguales. En el prototipo se queda sin conectar y el porcentaje de batería que muestre Retro-Go no significa nada.

## Pines que no se usan

| GPIO | Motivo |
|---|---|
| 3, 45, 46 | Definen el modo de arranque |
| 19, 20 | USB |
| 26 a 37 | Memoria flash y PSRAM |
| 43, 44 | Puerto serie |
