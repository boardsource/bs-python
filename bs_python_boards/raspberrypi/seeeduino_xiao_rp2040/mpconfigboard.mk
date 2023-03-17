USB_VID = 0x2886
USB_PID = 0x0042
USB_PRODUCT = "Seeeduino XIAO RP2040"
USB_MANUFACTURER = "Seeed"

CHIP_VARIANT = RP2040
CHIP_FAMILY = rp2

EXTERNAL_FLASH_DEVICES = "P25Q16H"

FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_NeoPixel
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_Display_Text
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_DisplayIO_SSD1306
FROZEN_MPY_DIRS += $(TOP)/frozen/peg_kmk_firmware/src