import wiringpi

SPIChannel = 1
SPISpeed = 1000000

wiringpi.wiringPiSetupGpio()
print wiringpi.wiringPiSPISetup(SPIChannel, SPISpeed)
#buf = str([0x00,0x00,0x00,0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff])  # []

buf = bytearray.fromhex("00 00 00 00 ff ff ff ff ff ff ff ff")

data = "00000000ffffffffffffffff"
bits = ""
for x in xrange(0, len(data), 2):
  bits += chr(int(data[x:x+2], 16))
print bits
#sendData = str(0x00,0x00,0x00,0x00)

receiveData = wiringpi.wiringPiSPIDataRW(SPIChannel, bits)

print receiveData
