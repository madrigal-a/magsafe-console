# MagSafe Console

Consola retro open source del tamaño de una tarjeta que se pega por MagSafe a la parte de atrás del celular.

**Estado: en diseño.** Todavía no hay hardware probado.

## Qué es

- Emula NES, Game Boy, Game Boy Color, Master System y Game Gear con [Retro-Go](https://github.com/ducalex/retro-go).
- ESP32-S3 con 8 MB de PSRAM.
- Pantalla IPS a color de 2.4", 320×240.
- Objetivo de tamaño: aprox. 64 × 98 mm y de 8 a 9 mm de grosor, con anillo de imanes MagSafe en la tapa trasera.
- Batería LiPo de 800 a 1000 mAh, con objetivo de 5 a 6 horas de juego.
- PCB fabricada en JLCPCB y armada a mano con piezas de LCSC; carcasa impresa en 3D.

Game Boy Advance queda fuera de esta versión: la ESP32-S3 no lo corre bien.

## Contenido

| Carpeta | Contenido |
|---|---|
| [docs/](docs/) | Guía de conexiones del prototipo y plano de acomodo |
| [firmware/](firmware/) | Target de Retro-Go para esta consola |
| [hardware/](hardware/) | Esquemático y PCB en KiCad, piezas y revisión de huellas |
| [PENDIENTES.md](PENDIENTES.md) | Lista de lo que falta |

## Plan

1. Prototipo en protoboard con placa de desarrollo.
2. Esquemático y PCB en KiCad.
3. Primer pedido a JLCPCB.
4. Carcasa impresa en 3D.

## Licencia

Por definir. El target de firmware deriva de Retro-Go y es GPLv2. Este repo no incluye ROMs.
