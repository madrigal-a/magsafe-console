# Diseño del circuito (v1)

Descripción del esquemático de KiCad, que está en [kicad/](kicad/) y en [esquematico.pdf](esquematico.pdf). **Estado: borrador sin probar en hardware.** Los números de catálogo de JLCPCB están verificados en [piezas.md](piezas.md).

Los pines de la ESP32-S3 son los de [docs/prototipo-conexiones.md](../docs/prototipo-conexiones.md).

## Energía

```
USB-C ──5V──> cargador TP4056 ──> batería LiPo (con protección integrada)
   │                                   │
   └────> reparto de carga <───────────┘
                 │
              VSYS (3.5 a 5 V)
                 ├──> regulador 3.3 V ──> ESP32-S3, pantalla, microSD
                 └──> amplificador de audio
```

| Bloque | Pieza | LCSC | Notas |
|---|---|---|---|
| Conector | USB-C de 16 pines | C165948 | CC1 y CC2 con 5.1 kΩ a GND cada uno |
| Cargador | TP4056 | C16581 | Resistencia PROG de 2 kΩ: carga a unos 580 mA |
| Protección | La de la propia batería | | Usar una batería con circuito de protección integrado. En v1 no va protección en la placa |
| Reparto de carga | MOSFET P AO3401A + diodo Schottky B5819W | C15127 | Con USB conectado, la consola se alimenta del USB y no de la batería |
| Regulador 3.3 V | AP2112K-3.3 | C51118 | 600 mA. Su pin EN va al interruptor de encendido |
| Encendido | Interruptor deslizable MSK12C02 | C431540 | Apaga el regulador; la carga sigue funcionando. 100 kΩ a GND en EN |
| Medición de batería | Divisor 1 MΩ + 1 MΩ, con 100 nF | | A GPIO 1 |

Indicadores: LED de carga y LED de carga completa en los pines CHRG y STDBY del TP4056.

## ESP32-S3-WROOM-1-N16R8

LCSC: C2913202.

| Conexión | Detalle |
|---|---|
| 3V3 | 10 µF + 100 nF pegados al módulo |
| EN | 10 kΩ a 3V3 y 1 µF a GND; botón de reset a GND |
| GPIO 0 | Botón Menu a GND. Presionado al encender, entra en modo de grabación |
| GPIO 19, 20 | D− y D+ del USB-C, directos. Se graba por USB sin chip adicional |
| Antena | Sin cobre, batería ni imanes debajo ni alrededor de la antena del módulo |

## Pantalla

Panel desnudo de 2.4" ST7789V con cable plano. **Pendiente:** número de pines y separación, al recibir la pieza.

| Señal | GPIO |
|---|---|
| SCK | 12 |
| MOSI | 11 |
| CS | 10 |
| DC | 9 |
| RST | 14 |
| Luz de fondo | 13, por PWM a través de un MOSFET N AO3400A, con 100 kΩ a GND |

## microSD

Ranura push-push (LCSC: C91145), por SPI.

| Señal | GPIO |
|---|---|
| SCK | 16 |
| MOSI | 15 |
| MISO | 17 |
| CS | 18 |

Resistencias de 10 kΩ a 3V3 en CS y MISO. Condensador de 100 nF en la alimentación.

## Audio

MAX98357AETE (LCSC: C910544), alimentado desde VSYS.

| Señal | GPIO |
|---|---|
| BCLK | 40 |
| LRCLK | 41 |
| DIN | 42 |

- SD_MODE con 1 MΩ a la alimentación, como en el módulo del prototipo.
- GAIN sin conectar (9 dB).
- 10 µF + 100 nF en la alimentación.
- Bocina plana de 8 Ω, por elegir.

## Botones

Doce botones táctiles TS-1187A (5.1 × 5.1 × 1.5 mm, LCSC C318884), cada uno de su GPIO a GND, sin resistencias externas. El de reset es igual.

| Botón | GPIO | Botón | GPIO |
|---|---|---|---|
| Arriba | 4 | Start | 47 |
| Abajo | 5 | Select | 48 |
| Izquierda | 6 | Menu | 0 |
| Derecha | 7 | Option | 39 |
| A | 8 | L | 2 |
| B | 21 | R | 38 |

## Para depurar la primera placa

- Puntos de prueba en VBUS, VBAT, VSYS, 3V3, GND, EN, GPIO 0, TX y RX.
- Pads para puerto serie (GPIO 43 y 44) por si el USB nativo falla.
- Puente de soldadura en la salida del regulador, para aislar la ESP32 y probar primero la energía.

## Decisiones abiertas

| Tema | Depende de |
|---|---|
| Conector de la pantalla y resistencia de la luz de fondo | Tener el panel en la mano |
| Modelo de batería | Espacio que deje la PCB dentro de la carcasa |
| Bocina plana | Grosor final |
| Posición del anillo MagSafe | No tapar la antena ni la cámara del celular |
