class ListCharcter:
    def __init__(
            self,
            name , # имя персонажа
            character_class, # класс персонажа
            character_subclass, # подкласс
            race,  # расса
            backstory, # предыстория
            level = 1, # уровень
            armor_class = 10, # класс брони
            max_health = 10, # здоровье
            speed = 30, # скорость передвижения
            strenght = 10, # сила
            agility = 10, # ловкость
            intellect = 10, # интеллект
            wisdom = 10, # мудрость
            build = 10, # телосложение
            charisma = 10, # харизма
            passive_perception =10 # пассивное восприятие
            ):
        self.name = name
        self.character_class = character_class
        self.character_subclass = character_subclass
        self.race = race
        self.backstory = backstory
        self.level = level
        self.armor_class = armor_class
        self.max_health = max_health
        self.health = max_health
        self.speed = speed

        self.strenght = strenght
        self.agility = agility
        self.intellect = intellect
        self.wisdom = wisdom
        self.build = build
        self.charisma = charisma
        self.passive_perception = passive_perception

    def get_heal(self, amount):
        if amount < 0:
           raise ValueError("Лечение не может быть отрицательным")
        self.health = min(self.max_health, self.health + amount)

    def get_damage(self,damage):
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")
        self.health = max(0, self.health - damage)
    def get_modifier(self):
        pass
    def show_sheet(self):
        print(f"\n=== Лист персонажа ===")
        print(f"Имя: {self.name}")
        