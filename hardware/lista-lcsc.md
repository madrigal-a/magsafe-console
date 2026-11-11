# Lista de compra en LCSC

Para 5 placas, con repuesto. Hecha el 10 de noviembre de 2026 a partir del esquemático.

Las cantidades de resistencias, condensadores, diodos y LED están redondeadas hacia arriba porque LCSC las vende por múltiplos. **El mínimo de compra, las existencias y el envío a México se confirman en el carrito**; los precios son los aproximados de `piezas.md`.

Para cargarla de un jalón: en LCSC, *BOM Tool*, subir `lista-lcsc.csv`.

| Pieza | Uso | LCSC | Por placa | Pedir | Subtotal aprox. (USD) |
|---|---|---|---|---|---|
| ESP32-S3-WROOM-1-N16R8 | Cerebro (U3) | C2913202 | 1 | 5 | 24.75 |
| MAX98357AETE+T | Amplificador (U4) | C910544 | 1 | 6 | 7.86 |
| TP4056-42-ESOP8 | Cargador (U1) | C16581 | 1 | 7 | 1.33 |
| AP2112K-3.3TRG1 | Regulador 3.3 V (U2) | C51118 | 1 | 7 | 1.19 |
| TYPE-C-31-M-12 | USB-C (J1) | C165948 | 1 | 7 | 1.33 |
| TF-01A | Ranura microSD (J4) | C91145 | 1 | 6 | 1.14 |
| MSK12C02 | Interruptor (SW1) | C431540 | 1 | 7 | 0.35 |
| TS-1187A-B-A-B | Botones frontales y reset (SW2 a SW14) | C318884 | 13 | 80 | 1.60 |
| TS24CA | Gatillos L y R (SW15, SW16) | C393942 | 2 | 15 | 0.45 |
| AO3401A | MOSFET P (Q1) | C15127 | 1 | 10 | 0.90 |
| AO3400A | MOSFET N (Q2) | C20917 | 1 | 10 | 0.90 |
| B5819W | Diodo Schottky (D3) | C8598 | 1 | 20 | 0.60 |
| KT-0603R | LED rojo (D1) | C2286 | 1 | 20 | 0.20 |
| KT-0805G | LED verde (D2) | C2297 | 1 | 20 | 0.40 |
| 10 Ω 0603 | R13 | C22859 | 1 | 100 | 0.10 |
| 1 kΩ 0603 | R4, R5 | C21190 | 2 | 100 | 0.10 |
| 3 kΩ 0603 | R3 | C4211 | 1 | 100 | 0.10 |
| 5.1 kΩ 0603 | R1, R2 | C23186 | 2 | 100 | 0.10 |
| 10 kΩ 0603 | R7, R8, R9 | C25804 | 3 | 100 | 0.10 |
| 100 kΩ 0603 | R6, R14, R15 | C25803 | 3 | 100 | 0.10 |
| 1 MΩ 0603 | R10, R11, R12 | C22935 | 3 | 100 | 0.10 |
| 100 nF 0603 | C7, C8, C10, C11 | C14663 | 4 | 100 | 0.30 |
| 1 µF 0603 | C3, C5 | C15849 | 2 | 50 | 0.30 |
| 10 µF 0603 | C1, C2, C4, C6, C9, C12 | C19702 | 6 | 100 | 2.00 |

**Total aproximado: 46 USD**, sin envío ni impuestos.

## No va en este pedido

- **Conector de la pantalla (J3).** Se elige cuando llegue el panel.
- **Batería, bocina y pantalla.** Se compran aparte.
- **Pasta de soldar, fundente y esténcil.** El esténcil se pide con la placa en JLCPCB.
