class Kek:
    def __init__(self, n, s, ss):
        self.name = n
        self.song = s
        self.skill = ss

    def show(self):
        print(f'Name of artist: {self.name}\nSong played: {self.song}\nAt level of skill: {self.skill}')

class cheburek(Kek):
    def __init__(self, n, s, ss, style, toughness, speed):
        super().__init__(n, s, ss,)
        self.s = style
        self.t = toughness
        self.sp = speed
    def show(self):
        print(f'The speed of song: {self.sp}\nThe toughness of song: {self.t}\nThe style: {self.s}')

k1 = cheburek('Ram', 'taboo', 'middle', 'guitar', 'hard', 'fast')
k1.show()
Kek.show(self=k1)