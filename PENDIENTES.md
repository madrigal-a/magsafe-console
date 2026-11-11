# Pendientes

Actualizado el 10 de noviembre de 2026. Lista de lo que falta, en el orden en que conviene hacerlo.

## Se puede hacer ya

- [ ] **Lista de compra en LCSC.** Pieza por pieza, con cantidades para 5 placas, a partir de `hardware/piezas.md`. Confirmar existencias, mínimos de compra y costo de envío a México.
- [ ] **Herramienta para armar.** Pasta de soldar, pistola de calor o plancha, pinzas finas y fundente. El esténcil se pide junto con la placa.
- [ ] **Medir el celular.** Desde el centro del anillo MagSafe: la consola ocupa 31 mm hacia arriba y 67 mm hacia abajo. Confirmar que no tapa la cámara ni se sale por abajo.
- [ ] **Revisar la vista 3D en KiCad 10.** Si hay piezas sin cuerpo, corregir la ruta de los modelos (se guardaron con la de KiCad 9).
- [ ] **Decidir 2 o 4 capas.** Con 4 capas el trazado es más fácil; cuesta más.
- [ ] **Confirmar con JLCPCB** el agujero mínimo en 2 capas, por las vías térmicas de 0.2 mm del ESP32.
- [ ] **Elegir batería.** El espacio previsto es de 55 × 40 × 3 mm.
- [ ] **Definir la licencia del repo.**

## Cuando lleguen las piezas del prototipo (22 al 24 de noviembre de 2026)

- [ ] **Panel de pantalla.** Contar los pines del cable plano, medir su paso y su ancho, y ver por qué lado sale. Con eso se elige el conector J3 y se le asigna huella.
- [ ] **Medir la pantalla.** Confirmar los 60 × 43 mm y el grosor.
- [ ] **Medir la bocina.** Diámetro y grosor. Si no cabe en unos 3 mm de grosor, buscar una plana.
- [ ] **Armar el prototipo en protoboard** con `docs/prototipo-conexiones.md` y probar el firmware. Esto valida el esquemático antes de pedir la placa.
- [ ] **Probar el WiFi** con el celular detrás, por la posición de la antena.

## PCB

- [ ] Colocar el conector de la pantalla.
- [ ] Ajustar la colocación con las medidas reales de batería, bocina y pantalla.
- [ ] Agujeros de montaje, de acuerdo con la carcasa.
- [ ] Trazar las pistas: primero USB y alimentación, después pantalla, tarjeta y audio, al final los botones.
- [ ] Acomodar los textos de la serigrafía.
- [ ] Revisión de reglas sin errores.
- [ ] Generar los archivos de fabricación.

## Pedido

- [ ] Cotizar y pedir placa y esténcil en JLCPCB.
- [ ] Pedir las piezas en LCSC.

## Después

- [ ] Carcasa en 3D, con las tapas de los botones y de los gatillos.
- [ ] Elegir los imanes o el anillo MagSafe.
- [ ] Armar y probar la primera placa.
