# Piezas para JLCPCB

Verificadas en el catálogo de ensamble de JLCPCB el 10 de noviembre de 2026: el número existe, corresponde a la pieza y tenía stock. El stock y el precio cambian a diario, así que se confirman otra vez al ordenar.

Cada pieza del esquemático lleva su número en el campo `LCSC`.

La placa se va a armar a mano, así que las piezas se compran aparte (LCSC u otra tienda) y a JLCPCB solo se le pide la placa y el esténcil. Por eso las resistencias y condensadores pasaron de 0402 a 0603 el 10 de noviembre de 2026; los precios de esas filas son aproximados.

| Pieza | Uso | LCSC | Tipo | Precio aprox. (USD) |
|---|---|---|---|---|
| ESP32-S3-WROOM-1-N16R8 | Cerebro | C2913202 | Extendida | 4.95 |
| TP4056-42-ESOP8 | Cargador de batería | C16581 | Extendida | 0.19 |
| AP2112K-3.3TRG1 | Regulador 3.3 V | C51118 | Extendida | 0.17 |
| MAX98357AETE+T | Amplificador de audio | C910544 | Extendida | 1.31 |
| TYPE-C-31-M-12 | Conector USB-C | C165948 | Extendida | 0.19 |
| TF-01A | Ranura microSD | C91145 | Extendida | 0.19 |
| MSK12C02 | Interruptor de encendido | C431540 | Extendida | 0.05 |
| TS-1187A-B-A-B | Botones frontales y reset (13) | C318884 | Básica | 0.02 |
| TS24CA | Gatillos L y R, actuación lateral | C393942 | Extendida | 0.03 |
| AO3401A | MOSFET P, reparto de carga | C15127 | Básica | 0.09 |
| AO3400A | MOSFET N, luz de fondo | C20917 | Básica | 0.09 |
| B5819W | Diodo Schottky | C8598 | Básica | 0.03 |
| KT-0603R | LED rojo, cargando | C2286 | Básica | 0.01 |
| KT-0805G | LED verde, carga completa | C2297 | Básica | 0.02 |
| Resistencias 0603 | 10 Ω, 1 k, 2 k, 5.1 k, 10 k, 100 k, 1 M | C22859, C21190, C22975, C23186, C25804, C25803, C22935 | Básicas | 0.001 |
| Condensador 100 nF 0603 | Desacoplo | C14663 | Básica | 0.003 |
| Condensador 1 µF 0603 | Regulador y reset | C15849 | Básica | 0.006 |
| Condensador 10 µF 0603 | Filtrado | C19702 | Básica | 0.02 |

Las piezas de una consola suman unos 8 USD, sin pantalla, batería ni bocina.

JLCPCB cobra un cargo fijo por cada tipo de pieza extendida (unos 3 USD, por confirmar al cotizar). Hay ocho, y no encontré equivalentes básicos para ellas.

## Huellas

| Origen | Piezas |
|---|---|
| Librería oficial de KiCad | TP4056, AP2112K, MAX98357A, USB-C, interruptor, MOSFET, diodo, LED, resistencias, condensadores |
| Catálogo de JLCPCB, en `kicad/lib/` con modelo 3D | Ranura microSD TF-01A, botón TS-1187A y gatillo TS24CA |
| Copia modificada de la de KiCad, en `kicad/lib/` | ESP32-S3 |
| Pads para soldar cable | Batería y bocina |
| Pendiente | Conector de la pantalla |

## Revisión contra hojas de datos

Hecha el 10 de noviembre de 2026. El detalle está en [revision-huellas.md](revision-huellas.md).

- El TS24CA es de actuación lateral. Su botón apunta hacia el lado de los pads de sujeción.
- Del botón TS-1187A se usan los pads 1 y 4, que quedan en filas distintas. Es correcto.
- La huella de la ranura microSD tenía los contactos 0.1 mm corridos. Ya está corregida.
- El pin de detección de tarjeta de la ranura microSD queda sin usar.
- El ESP32 usa una copia de la huella con la zona prohibida solo bajo la antena.
