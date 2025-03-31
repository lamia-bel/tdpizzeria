from pizza import Pizza
from carte_pizzeria_exception import CartePizzeriaException

class CartePizzeria:
    """Classe représentant la carte d'une pizzeria."""
    
    def __init__(self):
        self.pizzas = []

    def is_empty(self) -> bool:
        """Retourne True si la carte est vide, False sinon."""
        return len(self.pizzas) == 0

    def nb_pizzas(self) -> int:
        """Retourne le nombre de pizzas sur la carte."""
        return len(self.pizzas)

    def add_pizza(self, pizza: Pizza):
        """Ajoute une pizza à la carte."""
        self.pizzas.append(pizza)

    def remove_pizza(self, name: str):
        """Supprime une pizza de la carte par son nom. Lève une exception si elle n'existe pas."""
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException(f"La pizza '{name}' n'existe pas dans la carte.")
