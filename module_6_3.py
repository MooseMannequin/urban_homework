class Horse:
    x_distance = 0
    def __init__(self):
        self.sound = 'Frr'
        super().__init__()


    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0

    def __init__(self):
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        print((self.x_distance, self.y_distance))

    def voice(self):
        print(self.sound)


pegas = Pegasus()
pegas.get_pos()
pegas.move(3,4)
pegas.get_pos()
pegas.move(5,5)
pegas.get_pos()
pegas.voice()
# print(Pegasus.mro())

