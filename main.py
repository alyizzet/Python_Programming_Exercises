class Sector:
  def __init__(self):
    self.fr = 0
    self.to = 0
    self.rad = 0
  def rotate(self, angle):
    self.fr  = self.fr + angle
    self.to = self.to + angle 
    
    #implement this
    #rotates sector by angle
    #you man assume the rotation never results in a sector with fr > to
    #(it is optional to solve this problem without this assumption; see above)
  def intersect(self, other):
    int1 = max(self.fr,other.fr)
    int2 = min(self.to,other.to)
    return f'{int1} {int2} {other.rad}'
    #implement this
    #returns sector (i.e., object of class Sector) that is intersection
    #of this and other sector
    #you may assume that the two sectors have nonempty intersection
  def is_empty(self):
    if self.to == self.fr:
      return True
    else: 
      return False

    #implement this
    #returns True if the sector has empty area, otherwise False
  def __eq__(self, other):
    if (self.to - self.fr == other.to - other.fr):
      return True
    else: 
      return False
    #implement this
    #returns True this sector is the same as the other, otherwise False
  def __str__(self):
    st = f'{self.fr} {self.to} {self.rad}'
    return str(st)
    #implement this
    #returns string "F T R" where F is from angle, T is to, and R is radius