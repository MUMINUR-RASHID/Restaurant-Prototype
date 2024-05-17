class Food:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.cooking_time=15


class Burger(Food):
    def __init__(self, name, price,mid,ingredients):
        super().__init__(name, price)
        self.mid=mid
        self.ingredients=ingredients



class Pizza(Food):
    def __init__(self, name, price,size,toppings):
        super().__init__(name, price)
        self.size=size
        self.toppings=toppings


class Drinks(Food):
    def __init__(self, name, price,size,isCold=True):
        super().__init__(name, price)
        self.isCold=isCold
        self.size=size


#composition
class Menu:
    def __init__(self) -> None:
        self.pizzas=[]
        self.burgers=[]
        self.drinks=[]


    def add_menu_item(self,item_type,item):
        if item_type=="pizza":
            self.pizzas.append(item)
        elif item_type=='burger':
            self.burgers.append(item)
        elif item_type=='drink':
            self.drinks.append(item)

    def remove_item(self,item):
        if item in self.pizzas:
            self.pizzas.remove(item)

        elif item in self.burgers:
            self.burgers.remove(item)

        elif item in self.drinks:
            self.drinks.remove(item)

    def show_menu(self):
        print("PIZZAS:")
        for pizza in self.pizzas:
            print(f"name: {pizza.name}, price: {pizza.price}")

        print("BURGERS:")
        for burger in self.burgers:
            print(f"name: {burger.name}, price: {burger.price}")

        print("DRINKS:")
        for drink in self.drinks:
            print(f"name: {drink.name}, price: {drink.price}")