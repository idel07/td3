class Pizza:
    
    def __init__(self, name, ingredients, prix):
        self.name = name
        self.ingredients = ingredients
        self.prprixice = prix

    def __str__(self):
        return f"Pizza {self.name}: {', '.join(self.ingredients)} - ${self.price:.2f}"