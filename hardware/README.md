# Hardware

Aquí irá el proyecto de KiCad (esquemático y PCB) y los archivos de fabricación para JLCPCB.

**Pendiente:** elegir el modelo exacto de pantalla. Su conector define parte del esquemático.

## Bloques del circuito

| Bloque | Pieza prevista |
|---|---|
| Cerebro | ESP32-S3-WROOM-1-N16R8 |
| Pantalla | IPS 2.4" 320×240 ST7789, conector FPC |
| Almacenamiento | Ranura microSD |
| Audio | MAX98357A + bocina de 8 Ω |
| Energía | USB-C, cargador de litio, regulador a 3.3 V, LiPo de 800 a 1000 mAh |
| Controles | Cruceta, A, B, Start, Select, Menu, Option, L, R |

La asignación de pines está en [docs/prototipo-conexiones.md](../docs/prototipo-conexiones.md).

Las piezas concretas de energía y sus números de catálogo se definen al hacer el esquemático.
