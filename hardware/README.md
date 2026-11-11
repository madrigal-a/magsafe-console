# Hardware

Proyecto de KiCad y, más adelante, los archivos de fabricación para JLCPCB.

| Archivo | Contenido |
|---|---|
| [kicad/magsafe-console.kicad_pro](kicad/magsafe-console.kicad_pro) | Proyecto. Abrir este en KiCad (formato 9, compatible con 10) |
| [kicad/magsafe-console.kicad_sch](kicad/magsafe-console.kicad_sch) | Esquemático v0.1 |
| [esquematico.pdf](esquematico.pdf) | El esquemático en PDF |
| [circuito.md](circuito.md) | Explicación del circuito por bloques |
| [piezas.md](piezas.md) | Piezas verificadas en el catálogo de JLCPCB |
| [kicad/lib/](kicad/lib/) | Símbolos, huellas y modelos 3D de piezas que no trae KiCad |

## Estado del esquemático

- Pasa la revisión eléctrica (ERC) de KiCad 9 sin errores. Queda un aviso inofensivo en el pad térmico del amplificador.
- **Sin probar en hardware** y sin revisar todavía contra las hojas de datos de cada pieza.
- Las conexiones se hacen con etiquetas de red en vez de cables largos: dos pines con la misma etiqueta están conectados.
- **Provisional:** el conector de la pantalla (J3) y la resistencia de la luz de fondo (R13).
- **Sin huella asignada todavía:** solo el conector de la pantalla.
- Las huellas aún no se han comparado contra las hojas de datos.
- La PCB aún no existe.

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

El diseño por bloques, con piezas y conexiones, está en [circuito.md](circuito.md).
