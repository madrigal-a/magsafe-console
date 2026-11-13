# Pendientes

Actualizado el 10 de noviembre de 2026. Lista de lo que falta, en el orden en que conviene hacerlo.

## Se puede hacer ya

- [x] **Lista de compra en LCSC.** Está en `hardware/lista-lcsc.md` y `hardware/lista-lcsc.csv` (unos 46 USD). Falta confirmar existencias, mínimos y envío a México en el carrito.
- [ ] **Herramienta para armar.** Pasta de soldar, pistola de calor o plancha, pinzas finas y fundente. El esténcil se pide junto con la placa.
- [ ] **Probar en un iPhone con un recorte de 64 × 98 mm.** La consola se diseñó con medidas de iPhone (31 mm arriba y 67 mm abajo del centro del anillo). Falta la prueba física de que no tapa la cámara.
- [ ] **Revisar la vista 3D en KiCad 10.** Si hay piezas sin cuerpo, corregir la ruta de los modelos (se guardaron con la de KiCad 9).
- [x] **Decidir 2 o 4 capas.** 4 capas.
- [x] **Agujero mínimo.** En 4 capas JLCPCB acepta 0.2 mm, así que las vías térmicas quedan como están.
- [x] **Elegir batería.** LiPo 304050 con protección (3 × 40 × 50 mm, unos 600 mAh). Falta comprarla.
- [x] **Corriente de carga.** R3 pasó a 3 kΩ (C4211): unos 400 mA.
- [ ] **Definir la licencia del repo.**

## Cuando lleguen las piezas del prototipo (22 al 24 de noviembre de 2026)

- [ ] **Panel de pantalla.** Contar los pines del cable plano, medir su paso y su ancho, y ver por qué lado sale. Con eso se elige el conector J3 y se le asigna huella.
- [ ] **Medir la pantalla.** Confirmar los 60 × 43 mm y el grosor.
- [ ] **Medir la bocina.** Diámetro y grosor. Si no cabe en unos 3 mm de grosor, buscar una plana.
- [ ] **Armar el prototipo en protoboard** con `docs/prototipo-conexiones.md` y probar el firmware. Esto valida el esquemático antes de pedir la placa.
- [ ] **Probar el WiFi** con el celular detrás, por la posición de la antena.

## PCB

- [x] Adaptar la placa a las piezas del profesor: USB-C de pines atravesados, USBLC6-2P6, capacitores 0805, LED 0603 (ver `hardware/pcb.md`).
- [ ] Confirmar con el profesor si los capacitores 0805 son de 10 µF o de 15 µF.
- [ ] Revisar que los pines del USB-C que asoman por enfrente no estorben a la carcasa.

- [ ] Colocar el conector de la pantalla.
- [ ] Ajustar la colocación con las medidas reales de batería, bocina y pantalla.
- [ ] Agujeros de montaje, de acuerdo con la carcasa.
- [x] Pasar a 4 capas.
- [x] Trazar las pistas de todo menos la pantalla (trazador automático; ver `hardware/pcb.md`).
- [ ] Trazar las seis pistas de la pantalla cuando esté J3.
- [ ] Repasar el trazado automático en KiCad.
- [ ] Acomodar los textos de la serigrafía.
- [ ] Revisión de reglas sin errores (hoy: cero errores, solo avisos de serigrafía y falta J3).
- [ ] Generar los archivos de fabricación.

## Pedido

- [ ] Cotizar y pedir placa y esténcil en JLCPCB.
- [ ] Pedir las piezas en LCSC.

## Después

- [ ] Carcasa en 3D, con las tapas de los botones y de los gatillos.
- [ ] Elegir los imanes o el anillo MagSafe.
- [ ] Armar y probar la primera placa.
