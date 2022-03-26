USB_VID = 0x239A
USB_PID = 0x80B4
USB_PRODUCT = "nice!nano"
USB_MANUFACTURER = "Nice Keyboards"

MCU_CHIP = nrf52840

INTERNAL_FLASH_FILESYSTEM = 1

FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_BLE
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_NeoPixel
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_SSD1306
# you need to fix the 1306 lib and you need to add framebuf