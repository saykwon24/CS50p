class Food:
    base_hearts = 1    # class variable
    
    def __init__(self, ingredients):    # instance method
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)
    
    @classmethod
    def calculate_hearts(cls, ingredients):    # class method
        hearts = cls.base_hearts    # reference the class variable
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts
    
    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingredients=[])    # new instance(object) of this class 'Food'
        food.hearts = hearts
        return food


def main():
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")
    
    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")


main()