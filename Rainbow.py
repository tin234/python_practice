

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

    @classmethod
    def list_colors(cls):
        return list(cls.COLORS.values())

print(RainbowColor.COLORS["RED"])
print(RainbowColor.list_colors())

