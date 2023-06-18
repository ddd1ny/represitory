class AA:
    def __init__(self):
        super().__init__()
        self.A = "A"
class BB:
    def __init__(self):
        super().__init__()
        self.B = "B"

class C(BB,AA):
    def __init__(self):
        super().__init__()

        print(f"{A}-{B}")

#Типо классы . 2 класса в третим