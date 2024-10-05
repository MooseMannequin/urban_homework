class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frr'
        super().__init__()


    def run(self, dx):
        self.x_distance += dx


class Eagle:


    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


pegas = Pegasus()
print(pegas.get_pos())
pegas.move(3,4)
print(pegas.get_pos())
pegas.move(5,5)
print(pegas.get_pos())
pegas.voice()
# print(Pegasus.mro())

