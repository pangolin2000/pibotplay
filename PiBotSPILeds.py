import wiringpi

SPIChannel = 0
SPISpeed = 1000000

wiringpi.wiringPiSetupGpio()
print wiringpi.wiringPiSPISetup(SPIChannel, SPISpeed)
#buf = str([0x00,0x00,0x00,0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff])  # []

#startFrame = '00 00 00 00'
#endFrame = 'ff ff ff ff'
#ledsWhite = 'ff ff ff ff'

#for 8 leds set to certain configuration in loop?

#buf = bytearray.fromhex("00 00 00 00 ff ff ff ff ff ff ff ff")

data = "00000000ffffffffffffffff"
bits = ""  # wiringpi requires a str object.
for x in xrange(0, len(data), 2):
  bits += chr(int(data[x:x+2], 16))
print bits
#sendData = str(0x00,0x00,0x00,0x00)

receiveData = wiringpi.wiringPiSPIDataRW(SPIChannel, bits)

print receiveData
