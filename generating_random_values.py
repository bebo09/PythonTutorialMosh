import random

for i in range(3):
    print(random.randint(10, 20))

member = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(member)
print(leader)

# Dice Excercise

class Dice:

    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

dice = Dice()
print(dice.roll())