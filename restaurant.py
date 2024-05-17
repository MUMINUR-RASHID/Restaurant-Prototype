class Restaurant:
    def __init__(self,name,rent,menu=[]) -> None:
        self.name=name
        self.orders=[]
        self.chef=None
        self.server=None
        self.manager=None
        self.menu=menu
        self.revenue=0
        self.expense=0
        self.balance=0
        self.profit=0
        self.rent=rent


    def add_employee(self,employee_type,employee):
        if employee_type=='chef':
            self.chef=employee

        elif employee_type=='server':
            self.server=employee

        elif employee_type=='manager':
            self.manager=employee

    def add_order(self,order):
        self.orders.append(order)

    def receive_payment(self,order,amount,customer):
        if amount>= order.bill:
            self.revenue+=order.bill
            self.balance+=order.bill
            customer.due_amount=0
            return amount-order.bill
        else:
            print("Not Enough money given")
        

    def pay_expense(self,amount,description):
        if amount<self.balance:
            self.expense+=amount
            self.balance-=amount
            print(f"Expence {amount} for {description}")

        else:
            print(f"Not Enough Money To Pay {amount}")


    def pay_salary(self,employee):
        if employee.salary<self.balance:
            self.balance-=employee.salary
            self.expense+=employee.salary
            employee.receive_salary()
        else:
            print("Not Enough Cash for payong salary.")

    def show_employee(self):
        print("Employees:")
        if self.chef is not None:
            print(f"Chef: {self.chef.name} With salary {self.chef.salary}")
        if self.server is not None:
            print(f"Server: {self.server.name} With salary {self.server.salary}")
        if self.manager is not None:
            print(f"Manager: {self.manager.name} With salary {self.manager.salary}")




