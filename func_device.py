from ppadb.client import Client as adbc

class RemoteControl :
    adb = adbc(host="127.0.0.1", port = 5037)
    device = adb.devices()[0]
    
    
    def right(self) :
        self.device.shell("input tap 350 1260")
    
    
    def left(self) :
        self.device.shell("input tap 67 1260")
    
    
    def up(self) :
        self.device.shell("input tap 206 1120")
    
        
    def down(self) :
        self.device.shell("input tap 206 1404")
        
    
    def check(self) :
        self.device.shell("input tap 796 1368")
        
        
    def not_check(self) :
        self.device.shell("input tap 553 1368")