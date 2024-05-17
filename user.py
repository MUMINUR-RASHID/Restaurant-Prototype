from abc import ABC,abstractmethod

class Users(ABC):
    def __init__(self,name,phone,email,address):
        self.email=email
        self.phone=phone
        self.address=address
        self.name=name


class Customer(Users):
    def __init__(self, name,money,phone,email,address):
        self.wallet=money
        self.__order=None
        self.due_amount=0
        super().__init__(name,phone,email,address)


    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order=order

    def place_order(self,order):
        self.order=order
        self.due_amount+=order.bill
        print(f"Mr. {self.name}, placed an order with bill {self.due_amount} ")

    
    def eat_food(self,order):
        print(f"{self.name} eating foods {order.items}")


    def pay_bill(self,amount):
        pass

    def give_tips(self,amount):
        pass


    def write_review(self,satrs):
        pass
    

class Employee(Users):
    def __init__(self, name,salary,starting_date,department,phone,email,address):

        self.salary=salary
        self.due=salary
        self.starting_date=starting_date
        self.department=department
        super().__init__(name,phone,email,address)

    def receive_salary(self):
        self.due=0



class Chef(Employee):
    def __init__(self, name, salary, starting_date, department, phone, email, address,cooking_item):
        self.cooking_item=cooking_item
        super().__init__(name, salary, starting_date, department, phone, email, address)

class Server(Employee):
    def __init__(self, name, salary, starting_date, department, phone, email, address):
        self.tips_earning=0
        super().__init__(name, salary, starting_date, department, phone, email, address)

    def take_order(self,order):
        pass

    def transfer_order(self,order):
        pass

    def receive_tips(self,amount):
        self.tips.earning+=amount


class Manager(Employee):
    def __init__(self, name, salary, starting_date, department, phone, email, address):
        super().__init__(name, salary, starting_date, department, phone, email, address)