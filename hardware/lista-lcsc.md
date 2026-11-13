# Lista de compra

Para 4 consolas, con repuesto. Actualizada el 13 de noviembre de 2026. El detalle con precios está en `compras.xlsx`.

## Se le compra al profesor

| Pieza | Número | Uso | Pedir |
|---|---|---|---|
| Regulador 3.3 V | AP2112K-3.3TRG1 | U2 | 4 |
| Conector USB-C de pines atravesados | GCT USB4085-GF-A | J1 | 4 |
| MOSFET N SOT-23 | 2N7002 | Q2 | 6 |
| Diodo Schottky SOD-123 | 1N5819HW-7-F | D3 | 6 |
| Protección USB SOT-666 | USBLC6-2P6 | U5 | 6 |
| LED verde 0603 | el que tenga | D2, carga completa | 8 |
| LED azul 0603 | el que tenga | D1, cargando | 8 |
| Resistencia 1 kΩ 0603 | | R4, R5 | 12 |
| Resistencia 3 kΩ 0603 | | R3 | 10 |
| Resistencia 5.1 kΩ 0603 | | R1, R2 | 12 |
| Resistencia 1 MΩ 0603 | | R10, R11, R12 | 16 |
| Capacitor 100 nF 0603 | | C7, C8, C10, C11 | 20 |
| Capacitor 1 µF 0603 | | C3, C5 | 12 |
| Capacitor 0805, 10 V o más (ver nota) | | C1, C2, C4, C6, C9, C12 | 30 |
| Interruptor (lo tiene después) | MSK12C02 | SW1 | 6 |

Nota: el esquemático dice 10 µF. La hoja de compras dice 15 µF; cualquiera de los dos sirve, falta confirmar cuál tiene el profesor.

## Se compra en LCSC

Para cargarla de un jalón: en LCSC, *BOM Tool*, subir `lista-lcsc.csv`.

| Pieza | Número | LCSC | Uso | Pedir |
|---|---|---|---|---|
| ESP32 | ESP32-S3-WROOM-1-N16R8 | C2913202 | U3 | 4 |
| Amplificador | MAX98357AETE+T | C910544 | U4 | 5 |
| Cargador | TP4056-42-ESOP8 | C16581 | U1 | 6 |
| Ranura microSD | TF-01A | C91145 | J4 | 5 |
| Botones frontales | TS-1187A-B-A-B | C318884 | SW2 a SW14 | 60 |
| Gatillos | TS24CA | C393942 | SW15, SW16 | 10 |
| MOSFET P | AO3401A | C15127 | Q1 | 6 |
| Resistencia 10 Ω 0603 | | C22859 | R13 | 100 |
| Resistencia 10 kΩ 0603 | | C25804 | R7, R8, R9 | 100 |
| Resistencia 100 kΩ 0603 | | C25803 | R6, R14, R15 | 100 |

Unos 31 USD sin envío ni impuestos. Las resistencias se venden de 100 en 100.

## No va en estas listas

Conector de la pantalla (J3), batería, bocina, pantalla, pasta de soldar y esténcil.
