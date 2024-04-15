from math import sin, cos, radians

class Projectile:

    def __init__(self, angle, velocity, height):
        self.Xpos = 0.0
        self.Ypos = height
        theta = radians(angle)
        self.Xvel = velocity*cos(theta)
        self.Yvel = velocity*sin(theta)
    
    def update(self, time):
        self.Xpos = self.Xpos + (time*self.Xvel)
        Yvel2 = self.Yvel - (time*(9.8))
        self.Ypos = self.Ypos + (time*(self.Yvel + Yvel2)/2) 
        self.yvel = Yvel2

    def getX(self):
        return self.Xpos
    
    def getY(self):
        return self.Ypos
    
    def get_inputs():
        A = float(input("Enter the launch angle(in degrees): "))
        V = float(input("Enter the velocity(in metres)): "))
        H = float(input("Enter the height(in metres): "))
        T = float(input("Enter the time interval between positions: "))
        return A, V, H, T
    
    def main():
        angle, vel, h0, time = get_inputs()
        cball = Projectile (angle , vel , h0) 
        while cball.getY () >= 0: 
            cball.update (time) 
            print ("\nDistance traveled: {0: 0 .if} meters.". format (cball.getXO)) 