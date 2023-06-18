import random


class HappyEnd:
    def __init__(self):
        self.pc = "Поздравляю вас вы .. вы прошли игру ! .\n Happy End"

class Student(HappyEnd):

    def __init__(self,name,):
        super().__init__()
        self.name = name
        self.gladness = 50
        self.alive = True
        self.money = 400
        self.energy = 100
        self.pet = 0
        self.car = 1



    def kataca(self):
        print("Пойду покатаюсь на машине :) . Куплю бензин")
        self.money -= 35
        self.gladness += 25
        self.energy += 10

    def podrabotka(self):
        print("Давно хотел заработать . Пойду на подработку")
        self.money += 40
        self.gladness -= 20
        self.energy -= 10

    def love(self):
        print("Пойдем погуляем ? \n Давай")
        self.money -= 10
        self.energy -= 10
        self.gladness += 40

    def odin(self):
        print("Я так одинок ...")
        self.gladness -= 30
        self.energy -= 20
        self.money += 0


    def rabota(self):
        print("Время работать")
        self.money += 25
        self.gladness -= 5
        self.energy -= 30

    def sleep(self):
        print("Пойду посплю")
        self.gladness += 3
        self.energy += 40
        self.money += 0

    def chill(self):
        print("reset time")
        self.gladness += 5
        self.energy += 30
        self.money -= 10

    def is_alive(self):
        if self.money <= 0:
            print("Банкрот...")
            self.alive = False

        if self.energy <= 0:
            print("Совсем нет сил..")
            self.sleep()

        if self.gladness <= 0:
            print("Депресия")
            self.alive = False

        if self.pet >= 4:
            print("Охх сколько петомцев развелось . Я не могу за ними ухаживать..")
            self.pet -= 3
    def buypc(self):
        self.gladness += 100
        self.money -= 300
        print("Я так рад ! Я купил себе самый мощный игровой пк ! Я стану самым успешным стримером !!\n*Спустя 2 года*\n Я стал самым богатым Человеком в мире)) Я теперь так счастлив")
        print(f"{self.pc}")
        self.alive = False
    def buyPet(self):
        self.pet += 1
        print("Я купил щеночка ! Я так рад !")
        self.money -= 100
        self.gladness += 30
    def sport(self):
        print("Пойду ка займусь спортом")
        self.energy -= 15
        self.gladness += 25
        self.money += 0
    def end_of_day(self):
        print(f"Счастье = {self.gladness}")
        print(f"{self.money}$ на счету")
        print(f"У меня  {self.energy} единиц енергии")
        print(f"У меня есть {self.pet} петомцев")
        print(f"")
    def live(self,day):
        day = "День " + str(day) + "жизни" + self.name

        print(f"{day:=^50}")
        livecube = random.randint(1,11)
        if livecube == 1:
            self.rabota()

        elif livecube == 2:
            self.sleep()

        elif livecube == 3:
            self.chill()

        elif livecube == 4:
            self.sport()

        elif livecube == 5:
            self.buyPet()

        elif livecube == 6:
            self.kataca()
        elif livecube == 7:
            self.love()
        elif livecube == 8:
            self.odin()
        elif livecube == 9:
            self.podrabotka()
        elif livecube == 10:
            self.sport()

        elif livecube == 11:
            self.buypc()


        self.end_of_day()
        self.is_alive()





nick = Student(name="Ника")

for day in range (365):
    if nick.alive == False:
        break
    nick.live(day)