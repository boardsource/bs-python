USB_VID = 0x1B4F
USB_PID = 0x0026
USB_PRODUCT = "Pro Micro RP2040"
USB_MANUFACTURER = "SparkFun"

CHIP_VARIANT = RP2040
CHIP_FAMILY = rp2

EXTERNAL_FLASH_DEVICES = "W25Q128JVxM"

FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_NeoPixel
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_Display_Text
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_DisplayIO_SSD1306
FROZEN_MPY_DIRS += $(TOP)/frozen/peg_kmk_firmware/src