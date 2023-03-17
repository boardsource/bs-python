USB_VID = 0x239A
USB_PID = 0x8106
USB_PRODUCT = "KB2040"
USB_MANUFACTURER = "Adafruit"

CHIP_VARIANT = RP2040
CHIP_FAMILY = rp2

EXTERNAL_FLASH_DEVICES = "W25Q64JVxQ"

FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_NeoPixel
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_Display_Text
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_DisplayIO_SSD1306
FROZEN_MPY_DIRS += $(TOP)/frozen/peg_kmk_firmware/src