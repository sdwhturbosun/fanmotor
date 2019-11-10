import fanmotorClass
import time
myfanmotor=fanmotorClass.FanMotor(17,27)
myfanmotor.rollclockwise()
time.sleep(5)
myfanmotor.rollanticlockwise()
time.sleep(5)
myfanmotor.stop()

