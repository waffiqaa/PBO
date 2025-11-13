# Contoh Polymorphism dengan tema K-Band Xdinary Heroes

class Lagu:
    def play(self):
        print("Memutar lagu secara umum")

class HairCut(Lagu):
    def play(self):
        print("Memutar 'Hair Cut' — penuh energi dan rebellious vibes!")

class StrawberryCake(Lagu):
    def play(self):
        print("Memutar 'Strawberry Cake' — nuansa manis tapi tetap powerful!")

class FreakingBad(Lagu):
    def play(self):
        print("Memutar 'Freaking Bad' — semangat meledak dan penuh rock!")

class TestMe(Lagu):
    def play(self):
        print("Memutar 'Test Me' — anthem kebebasan dan keberanian!")

# Daftar lagu yang akan diputar
playlist = [HairCut(), StrawberryCake(), FreakingBad(), TestMe()]

# Polymorphism in action!
for lagu in playlist:
    lagu.play()
