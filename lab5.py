class Vehicle:
    def __int__(self,wheels,tank,seat,speed):
        self.w =wheels
        self.t =tank
        self.s =seat
        self.sp =speed
    def drive(self):
        print('vehicle in driving mode')