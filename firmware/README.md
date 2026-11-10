# Firmware

La consola usa [Retro-Go](https://github.com/ducalex/retro-go) (GPLv2): menú de juegos y emuladores de NES, Game Boy, Game Boy Color, Master System, Game Gear y más. Aquí solo vive el *target*, es decir, la descripción de nuestro hardware.

**Estado: sin probar en hardware.** Se valida con el prototipo en protoboard.

## Compilar y grabar

Requiere ESP-IDF (Retro-Go soporta de la 4.4 a la 5.3) y una placa ESP32-S3 N16R8.

1. Clona Retro-Go: `git clone https://github.com/ducalex/retro-go`
2. Copia la carpeta `retro-go-target/magsafe-console` a `retro-go/components/retro-go/targets/`.
3. En `retro-go/components/retro-go/config.h`, junto a los demás targets, agrega:
   ```c
   #elif defined(RG_TARGET_MAGSAFE_CONSOLE)
   #include "targets/magsafe-console/config.h"
   ```
4. Compila la imagen: `python rg_tool.py --target magsafe-console build-img`
5. Grábala: `python rg_tool.py --target magsafe-console --port COM3 install` (cambia `COM3` por tu puerto).

## Tarjeta SD

Formato FAT32. Las ROMs van en `/roms/nes`, `/roms/gb`, `/roms/gbc`, etc. Este repo no incluye ni incluirá ROMs.

## Antes de vender consolas

Retro-Go es GPLv2 salvo dos componentes: `fmsx` (MSX), con licencia no comercial, y `handy` (Lynx), con licencia zlib. Para un firmware que se venda instalado hay que compilar sin fMSX.
