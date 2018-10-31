import wiringpi

SPIChannel = 1
SPISpeed = 1000000

wiringpi.wiringPiSetupGpio()
print wiringpi.wiringPiSPISetup(SPIChannel, SPISpeed)
#buf = str([0x00,0x00,0x00,0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff])  # []

buf = bytearray.fromhex("00 00 00 00 ff ff ff ff ff ff ff ff")
print buf
#sendData = str(0x00,0x00,0x00,0x00)

receiveData = wiringpi.wiringPiSPIDataRW(SPIChannel, buf)

print receiveData