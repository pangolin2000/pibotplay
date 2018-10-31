import spidev

SPIChannel = 0
device = 1 #?
spi0 = spidev.SpiDev()
spi.open(SPIChannel, device)