class Player:
    def __init__(self, name, hp, atk, defense):
        self.name = name

        self.max_hp = hp
        self.hp = hp

        self.atk = atk
        self.defense = defense

        self.level = 1
        self.exp = 0
        self.exp_to_next = 100

    # =====================
    # Combat
    # =====================
    def take_damage(self, damage):
        reduced = max(0, damage - self.defense)
        self.hp -= reduced
        self.hp = max(0, self.hp)
        return reduced

    def attack(self, enemy):
        return enemy.take_damage(self.atk)

    def is_alive(self):
        return self.hp > 0

    # =====================
    # Progression
    # =====================
    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.exp_to_next:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.exp_to_next += 50

        self.max_hp += 10
        self.hp = self.max_hp
        self.atk += 2
        self.defense += 1

        print(f"{self.name} leveled up to {self.level}!")
