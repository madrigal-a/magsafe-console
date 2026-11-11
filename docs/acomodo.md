# Plano de acomodo (propuesta v1)

Dónde va cada cosa en la consola. **Propuesta sin aprobar**; las medidas son aproximadas y la de la pantalla se confirma al recibir el panel.

## Medidas generales

| Medida | Valor |
|---|---|
| Ancho × alto | 64 × 98 mm |
| Grosor estimado | 8 a 9 mm |
| Orientación | Vertical, pantalla arriba y botones abajo |

El ancho sube de 62 a 64 mm para dejar pared de carcasa a los lados de la pantalla. El grosor sube respecto al objetivo inicial de 7.5 mm al sumar las capas reales.

## Capas, de frente hacia atrás

| Capa | Grosor aprox. |
|---|---|
| Tapa frontal | 1.0 mm |
| Pantalla | 2.4 mm |
| PCB | 0.8 mm |
| Batería y piezas altas (ESP32, 3.1 mm) | 3.2 mm |
| Tapa trasera con el anillo MagSafe embutido | 1.2 mm |

## Frente

| Elemento | Posición |
|---|---|
| Pantalla 2.4", horizontal | Arriba, de orilla a orilla (60 × 43 mm) |
| Cruceta | Abajo a la izquierda |
| A y B | Abajo a la derecha, en diagonal |
| Select y Start | Centro, abajo |
| Menu y Option | Esquinas inferiores |

## Interior, lado trasero de la PCB

| Elemento | Posición |
|---|---|
| Batería 55 × 40 × 3 mm | Detrás de la pantalla |
| Anillo MagSafe (56 mm exterior, 46 mm interior) | En la tapa trasera, centrado sobre la batería |
| ESP32-S3 | Zona de botones, con la antena hacia una orilla y lejos del anillo |
| Bocina | Zona de botones, al centro |
| Ranura microSD | Orilla lateral, la tarjeta entra de lado |
| USB-C | Orilla inferior, al centro |
| Interruptor de encendido | Orilla lateral |

## Decisiones abiertas

| Tema | Opciones |
|---|---|
| Botones L y R | No hay lugar natural en el frente. Opción A: quitarlos en v1 (NES, Game Boy y Game Boy Color no los usan). Opción B: ponerlos en la orilla superior con botones de actuación lateral, que es otra pieza |
| Batería | El modelo se elige según el espacio final; 55 × 40 × 3 mm da unos 700 a 800 mAh |
| Imanes y antena | Verificar en el prototipo que el anillo no afecte al WiFi ni a la bocina |
