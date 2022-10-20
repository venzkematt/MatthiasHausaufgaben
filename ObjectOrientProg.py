# class Cuboid:
#     def __init__(self):
#         self.length = 0
#         self.breadth = 0
#         self.hight = 0
#         self.weight = 0

class Cuboid:
    def __init__(self, length, breadth, hight, weight):
        self.length = length
        self.breadth = breadth
        self.hight = hight
        self.weight = weight

    def volume (self):
        x = self.length
        y = self.breadth
        z = self.hight
        v = x * y * z
        print (f"The volume is: {(round(v, 2))}")
    
    def density (self):
        x = self.length
        y = self.breadth
        z = self.hight
        v = x * y * z
        d = self.weight / v
        print (f"The density is: {(round(d, 2))}")
    
    def surface (self):
        x = self.length
        y = self.breadth
        z = self.hight
        s = 2 * (x * y + y * z + x * z)
        print (f"The surface area is: {(round(s, 2))}")

theCuboid = Cuboid (4.5, 7.3, 17.4, 20.2)
theCuboid.volume()
theCuboid.density()
theCuboid.surface()
   