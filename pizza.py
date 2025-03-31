from typing import List

class Pizza:
    """Classe représentant une pizza avec un nom, des ingrédients et un prix."""
    
    def __init__(self, name: str, ingredients: List[str], price: float):
        self.name = name
        self.ingredients = ingredients
        self.price = price
