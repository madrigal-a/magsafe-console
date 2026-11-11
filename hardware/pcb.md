# PCB

Estado al 10 de noviembre de 2026: **contorno y colocación inicial, sin pistas.** Es un punto de partida para mover piezas en KiCad, no un diseño terminado.

## Qué tiene el archivo

- Contorno de 64 × 98 mm con esquinas de 4 mm de radio. Grosor de 0.8 mm, 2 capas.
- Las 68 huellas del esquemático con sus redes ya asignadas. Falta solo el conector de la pantalla (J3), que no tiene huella.
- Planos de tierra en las dos caras.
- Zona sin cobre bajo la antena del ESP32.
- Reglas: pista y separación mínimas de 0.15 mm, 0.3 mm a la orilla, vías de 0.6/0.3 mm. Clase `Potencia` de 0.5 mm para VBUS, VBAT, VSYS, 3.3 V y bocina.
- Dibujos de referencia en la capa `Dwgs.User`: pantalla, batería, anillo MagSafe y bocina. No se fabrican.

## Dónde quedó cada cosa

Las medidas son desde la esquina superior izquierda, viendo la consola de frente.

**Frente:** solo los botones.

| Elemento | Posición (x, y en mm) |
|---|---|
| Pantalla (referencia) | De 2 a 62 a lo ancho, de 2 a 45 a lo alto |
| Cruceta | Centro en (14, 64), botones a 6.5 mm del centro |
| X, A, B, Y | Centro en (50, 64). X arriba, A derecha, B abajo, Y izquierda |
| Menu, Select, Start y Option | En fila a y = 82: Menu en x = 14, Select en 26.5, Start en 37.5, Option en 50 |

**Atrás:** todo lo demás.

| Elemento | Posición |
|---|---|
| Gatillos L y R | Orilla superior, en x = 7 y x = 57. El botón asoma 0.4 mm |
| Batería (referencia) | Detrás de la pantalla, de 5.5 a 45.5 a lo alto |
| Anillo MagSafe (referencia) | Centro en (32, 31) |
| ESP32 | Abajo a la izquierda, antena al ras de la orilla inferior |
| USB-C | Orilla inferior, al centro. Sobresale 1.1 mm de la placa |
| Ranura microSD | Orilla derecha, centrada en y = 80 |
| Interruptor | Orilla derecha, en y = 50.5, arriba de donde va la mano |
| Cargador, reparto de carga y regulador | Columna entre el centro y la ranura microSD |
| Amplificador y pads de bocina | Centro, arriba del USB-C |
| Pads de batería | (52, 49.5) y (56, 49.5), justo debajo de la batería |
| Reset | A la izquierda del ESP32 |

## Qué marca la revisión de reglas

- 94 conexiones sin trazar: es lo esperado, no hay pistas.
- 18 avisos por las vías térmicas de 0.2 mm del ESP32. Falta confirmar el mínimo de JLCPCB.
- Falta la huella de J3.
- Avisos de serigrafía encimada o cortada por la orilla. Se arreglan al acomodar los textos.
- No hay piezas encimadas, cortos ni cobre fuera de la placa.

## Decisiones que tomé y hay que confirmar

| Tema | Lo que puse | Por qué revisarlo |
|---|---|---|
| Antena del ESP32 | Orilla inferior, zona sin cobre solo bajo la antena | El USB-C queda pegado a la antena y el celular queda detrás. El WiFi puede salir débil. Se deja así y se mide en el prototipo |
| Centro del anillo MagSafe | A 31 mm de la orilla superior. Aprobado | Falta medir en el celular que la consola no tape la cámara ni se salga por abajo |
| USB-C | Sobresale 1.1 mm | Depende del grosor de la pared de la carcasa |
| Capas | 2 | Con 4 capas el trazado sería más fácil, a mayor costo |
| Tornillos | No hay agujeros | Se definen con la carcasa |

## Ensamble

**La placa completa se arma a mano.** A JLCPCB solo se le pide la placa y el esténcil, y las piezas se compran aparte.

- Los botones se sueldan con cautín normal: sus cuatro patas salen por los lados.
- El amplificador y el ESP32 tienen pads por debajo. Necesitan pasta y pistola de calor o plancha.
- Las resistencias y condensadores son 0603 para que sean manejables a mano.

El ensamble en JLCPCB se descartó por costo. El ESP32-S3-WROOM-1-N16R8 solo se puede montar con el servicio estándar, y armar la cara de atrás de 5 placas salía en unos 115 USD contra unos 50 USD armándolas a mano (estimado del 10 de noviembre de 2026, sin envío ni impuestos).

## Lo que sigue

1. Elegir la bocina plana y la batería definitivas; su tamaño mueve la colocación.
2. Elegir el conector de la pantalla cuando llegue el panel y colocarlo.
3. Agregar los agujeros de montaje según la carcasa.
4. Trazar las pistas: primero USB y alimentación, después pantalla, tarjeta y audio, al final los botones.
