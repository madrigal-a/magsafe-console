# Revisión de huellas contra hojas de datos

Hecha el 10 de noviembre de 2026 sobre el esquemático v0.1. Se comparó cada huella con el dibujo del fabricante (pads, paso, numeración de pines y orientación) y cada símbolo con el pinout de la hoja de datos.

## Resultado

| Pieza | Huella | Resultado |
|---|---|---|
| TS24CA (gatillos) | `magsafe:SW-SMD_2P-TS24CA` | Correcta. Es de actuación lateral. Un ajuste menor (ver abajo) |
| TS-1187A-B-A-B (botones) | `magsafe:SW-SMD_4P-L5.1-W5.1-P3.70-LS6.5-TL_H1.5` | Correcta |
| TF-01A (microSD) | `magsafe:TF-SMD_TF-01A` | **Corregida**: los 9 contactos estaban 0.1 mm corridos |
| ESP32-S3-WROOM-1 | `magsafe:ESP32-S3-WROOM-1_KeepoutReducido` | Pads correctos. **Se cambió la zona prohibida** (ver abajo) |
| TP4056 | SOIC-8 con pad térmico | Correcta. Pinout del símbolo correcto |
| AP2112K-3.3 | SOT-23-5 | Correcta. Pinout correcto |
| MAX98357A | TQFN-16 3×3 | Correcta. Pinout correcto |
| TYPE-C-31-M-12 | Huella de KiCad para esa misma pieza | Correcta |
| MSK12C02 | Huella de KiCad para esa misma pieza | Correcta |
| AO3401A, AO3400A | SOT-23 (1 puerta, 2 fuente, 3 drenaje) | Correcta |
| B5819W | SOD-123 (1 cátodo) | Correcta |
| LED, resistencias, condensadores | 0603, 0805, 0402 | Correctas |
| Conector de pantalla (J3) | Sin huella | Pendiente: depende del panel |

## TS24CA, gatillos L y R

- **Sí es de actuación lateral.** El cuerpo va acostado sobre la placa y el botón sale paralelo a ella.
- El botón apunta hacia el lado de los dos pads de sujeción (3 y 4). Los dos terminales eléctricos (1 y 2) quedan del lado contrario, hacia adentro de la placa.
- Medidas de la hoja de datos contra la huella: terminales a 3.4 mm entre sí, pads de 0.6 × 1.2 mm; pads de sujeción con 5.3 mm de extremo a extremo y 3.2 mm de hueco; dos postes de 0.5 mm a 1.7 mm entre sí. Todo coincide.
- Los pads de sujeción con forma de L son los que recomienda el fabricante. Van a tierra.
- El botón sobresale 2.47 mm desde el centro de la huella, y el cuerpo 1.23 mm. Como los pads de sujeción llegan a 1.62 mm, el cuerpo no puede quedar al ras de la orilla: en la placa el botón asoma unos 0.4 mm. La tapa del gatillo de la carcasa tiene que cubrir esa diferencia.
- Ajuste: los dos agujeros de los postes estaban como agujeros metalizados. Se cambiaron a no metalizados.

## TS-1187A-B-A-B, botones

- Pads recomendados: 7.0 mm de extremo a extremo y 5.0 mm de hueco a lo ancho; 4.5 y 3.0 mm a lo alto. La huella coincide.
- Por dentro están unidos los dos pads de arriba (1 y 2) y los dos de abajo (3 y 4); el botón cierra entre las dos filas. Usar los pads 1 y 4 es correcto.
- La variante B-A-B mide 1.5 mm de alto, con 160 gf y cabeza de latón.

## TF-01A, ranura microSD

- Numeración correcta: pin 1 DAT2, 2 CS, 3 MOSI, 4 VDD, 5 CLK, 6 GND, 7 MISO, 8 DAT1, 9 detección de tarjeta.
- Pads de sujeción, agujeros de los postes (1.0 mm, a 8.0 mm entre sí) y separaciones a lo largo coinciden.
- **Error encontrado:** la hoja de datos pone el contacto 9 a 1.10 mm del centro del pad de sujeción vecino. La huella del catálogo lo tenía a 1.20 mm, así que la fila completa de contactos estaba 0.1 mm corrida. Además los pads medían 0.6 mm de ancho en vez de 0.7 mm. Se corrigieron las dos cosas.
- Con la medida correcta, entre el contacto 9 y el pad de sujeción quedan 0.15 mm. Por eso la separación mínima del proyecto se fijó en 0.15 mm.
- Los dos agujeros de los postes se cambiaron a no metalizados.
- La tarjeta entra por el lado contrario a los contactos.

## ESP32-S3-WROOM-1

- Pines del símbolo y pads de la huella coinciden con la hoja de datos. Los GPIO 35, 36 y 37 quedan libres, como debe ser en el N16R8.
- La huella de KiCad trae una zona prohibida de 48 × 21 mm alrededor de la antena, que es la recomendación ideal de Espressif. En una placa de 64 mm de ancho no cabe: taparía el USB-C.
- Se hizo una copia en la librería del proyecto con la zona prohibida solo bajo la antena (18.6 × 6.5 mm). **Es un compromiso**: el alcance del WiFi será menor que el ideal y hay que medirlo en el prototipo.
- Las 18 vías térmicas del pad central son de 0.2 mm. La revisión de reglas las marca porque el mínimo configurado es 0.3 mm. Falta confirmar el mínimo de JLCPCB para 2 capas.

## Cambios en el esquemático

- U3 usa ahora la huella `magsafe:ESP32-S3-WROOM-1_KeepoutReducido`.
- Los puntos de prueba, los pads de batería y bocina y el puente JP1 quedaron fuera de la lista de materiales, porque no son piezas que se compren.

## Hojas de datos usadas

- [TS24CA](https://datasheet.lcsc.com/lcsc/2404241539_SHOU-HAN-TS24CA_C393942.pdf)
- [TS-1187A-B-A-B](https://datasheet.lcsc.com/lcsc/2304140030_XKB-Connectivity-TS-1187A-B-A-B_C318884.pdf)
- [TF-01A](https://www.lcsc.com/datasheet/C91145.pdf)
