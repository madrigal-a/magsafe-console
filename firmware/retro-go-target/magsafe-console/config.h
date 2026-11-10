// MagSafe Console - target de Retro-Go
// Modulo: ESP32-S3-WROOM-1-N16R8 (16 MB flash, 8 MB PSRAM octal)
// Basado en el target esp32-s3-devkit de Retro-Go (GPLv2).
//
// ESTADO: sin probar en hardware. Los pines coinciden con docs/prototipo-conexiones.md.
// Pines que NO se usan a proposito: 3, 45, 46 (arranque), 19/20 (USB),
// 26-37 (flash y PSRAM), 43/44 (puerto serie).

// Target definition
#define RG_TARGET_NAME             "MAGSAFE-CONSOLE"

// Storage (microSD por SPI, en su propio bus)
#define RG_STORAGE_ROOT             "/sd"
#define RG_STORAGE_SDSPI_HOST       SPI3_HOST
#define RG_STORAGE_SDSPI_SPEED      SDMMC_FREQ_DEFAULT

// Audio (MAX98357A por I2S)
#define RG_AUDIO_USE_INT_DAC        0   // 0 = Disable
#define RG_AUDIO_USE_EXT_DAC        1   // 1 = Enable

// Video (IPS 2.4" 320x240, ST7789, SPI)
#define RG_SCREEN_DRIVER            0   // 0 = ILI9341/ST7789
#define RG_SCREEN_HOST              SPI2_HOST
#define RG_SCREEN_SPEED             SPI_MASTER_FREQ_40M
#define RG_SCREEN_BACKLIGHT         1
#define RG_SCREEN_WIDTH             320
#define RG_SCREEN_HEIGHT            240
#define RG_SCREEN_ROTATE            0
#define RG_SCREEN_VISIBLE_AREA      {0, 0, 0, 0}
#define RG_SCREEN_SAFE_AREA         {0, 0, 0, 0}
// A AJUSTAR con la pantalla real:
//  - imagen girada o en espejo: cambiar el valor de 0x36 (0x68, 0xA8, 0x28, 0xE8...)
//  - rojo y azul cambiados: quitar o poner el bit BGR (0x08) en 0x36
//  - colores en negativo: quitar la linea 0x21
#define RG_SCREEN_INIT()                                                                                         \
    ILI9341_CMD(0x36, 0x68);                 /* Memory Access Control (MX|MV|BGR) */                             \
    ILI9341_CMD(0x21);                       /* Invert colors (paneles IPS) */

// Input: cada boton va de su pin a GND, con pull-up interno
#define RG_GAMEPAD_GPIO_MAP {\
    {RG_KEY_UP,     .num = GPIO_NUM_4,  .pullup = 1, .level = 0},\
    {RG_KEY_DOWN,   .num = GPIO_NUM_5,  .pullup = 1, .level = 0},\
    {RG_KEY_LEFT,   .num = GPIO_NUM_6,  .pullup = 1, .level = 0},\
    {RG_KEY_RIGHT,  .num = GPIO_NUM_7,  .pullup = 1, .level = 0},\
    {RG_KEY_A,      .num = GPIO_NUM_8,  .pullup = 1, .level = 0},\
    {RG_KEY_B,      .num = GPIO_NUM_21, .pullup = 1, .level = 0},\
    {RG_KEY_START,  .num = GPIO_NUM_47, .pullup = 1, .level = 0},\
    {RG_KEY_SELECT, .num = GPIO_NUM_48, .pullup = 1, .level = 0},\
    {RG_KEY_MENU,   .num = GPIO_NUM_0,  .pullup = 1, .level = 0},\
    {RG_KEY_OPTION, .num = GPIO_NUM_39, .pullup = 1, .level = 0},\
    {RG_KEY_L,      .num = GPIO_NUM_2,  .pullup = 1, .level = 0},\
    {RG_KEY_R,      .num = GPIO_NUM_38, .pullup = 1, .level = 0},\
}

// Battery: GPIO1 (ADC1 canal 0) con divisor 1:2 desde la bateria
#define RG_BATTERY_DRIVER           1
#define RG_BATTERY_ADC_UNIT         ADC_UNIT_1
#define RG_BATTERY_ADC_CHANNEL      ADC_CHANNEL_0
#define RG_BATTERY_CALC_PERCENT(raw) (((raw) * 2.f - 3500.f) / (4200.f - 3500.f) * 100.f)
#define RG_BATTERY_CALC_VOLTAGE(raw) ((raw) * 2.f * 0.001f)

// SPI Display
#define RG_GPIO_LCD_MISO            GPIO_NUM_NC
#define RG_GPIO_LCD_MOSI            GPIO_NUM_11
#define RG_GPIO_LCD_CLK             GPIO_NUM_12
#define RG_GPIO_LCD_CS              GPIO_NUM_10
#define RG_GPIO_LCD_DC              GPIO_NUM_9
#define RG_GPIO_LCD_BCKL            GPIO_NUM_13
#define RG_GPIO_LCD_RST             GPIO_NUM_14

// SPI SD Card
#define RG_GPIO_SDSPI_MISO          GPIO_NUM_17
#define RG_GPIO_SDSPI_MOSI          GPIO_NUM_15
#define RG_GPIO_SDSPI_CLK           GPIO_NUM_16
#define RG_GPIO_SDSPI_CS            GPIO_NUM_18

// External I2S DAC
#define RG_GPIO_SND_I2S_BCK         40
#define RG_GPIO_SND_I2S_WS          41
#define RG_GPIO_SND_I2S_DATA        42
