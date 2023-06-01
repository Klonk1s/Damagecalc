class player():
    def __init__(self, name, hp, physdmg, magedmg, armor, magearmor):
        self.name = name
        self.hp = hp
        self.physdmg = physdmg
        self.magedmg = magedmg
        self.armor = armor
        self.magearmor = magearmor
        print(self.name, "har", self.hp, "hp och", self.armor, "armor")

    def calc_multiplier(self):
        if self.armor >= 0:
            damage_multiplier = 100 / (100 + self.armor)
        else:
            damage_multiplier = 2 - 100 / (100 - self.armor)

        if self.magearmor >= 0:
            magedamage_multiplier = 100 / (100 + self.magearmor)
        else:
            magedamage_multiplier = 2 - 100 / (100 - self.magearmor)

        return damage_multiplier, magedamage_multiplier

    def take_damage(self, damage_multiplier, magedamage_multiplier):
        self.takedamage = damage_multiplier + magedamage_multiplier

    def damage_take(self, opdmg, damage_multiplier, magedamage_multiplier):
        print("opdmg:", opdmg, "damage_multiplier:", damage_multiplier)
        self.hp -= opdmg * damage_multiplier * magedamage_multiplier

        if self.hp <= 0:
            print(self.name, "är död")

    def attack(self, target):
        print(self.name, "attackerar", target.name)
        damage_multipliers = target.calc_multiplier()
        target.damage_take(self.physdmg + self.magedmg, *damage_multipliers)
        print(target.name, "har", target.hp, "hp och", target.armor, "armor kvar")


p1 = player("Darrow", 100, 400, 0, 250, 0)
p2 = player("Lysander", 100, 100, 100, 250, 100)

p2.attack(p1)