

class RainbowColor:
    
    COLORS = {
        "RED": "Красный",
        "ORANGE": "Оранжевый",
        "YELLOW": "Желтый",
        "GREEN": "Зеленый",
        "LIGHT_BLUE": "Голубой",
        "BLUE": "Синий",
        "PURPLE": "Фиолетовый"
    }
    RED = "Красный"

    def list_colors(self):
        return list(self.COLORS.values())

print(RainbowColor.COLORS["RED"])
print(RainbowColor().list_colors())
print(RainbowColor.RED)

