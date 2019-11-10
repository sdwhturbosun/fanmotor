import RPi.GPIO as g#vcc=5v
class FanMotor:
    def __init__(self,ina,inb):
        g.setmode(g.BCM)
        g.setwarnings(False)
        
        self.ina=ina
        self.inb=inb
        g.setup(self.ina,g.OUT)
        g.setup(self.inb,g.OUT)
        g.output(self.ina,0)
        g.output(self.inb,0)
    def rollclockwise(self):
        g.output(self.ina,1)
        g.output(self.inb,0)
    def rollanticlockwise(self):
        g.output(self.ina,0)
        g.output(self.inb,1)
    def stop(self):
        g.output(self.ina,0)
        g.output(self.inb,0)
    