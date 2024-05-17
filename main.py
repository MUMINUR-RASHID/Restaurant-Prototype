from menu import Pizza,Burger,Drinks,Menu
from restaurant import Restaurant
from user import Users,Chef,Customer,Manager,Server
from order import Order

def main():

    #menu
    menu=Menu()
    pizza1=Pizza("Shutki",600,"large",['sutki','onion'])
    menu.add_menu_item('pizza',pizza1)
    pizza2=Pizza("Alu",400,"large",['potato','onion'])
    menu.add_menu_item('pizza',pizza2)
    pizza3=Pizza("Dal",300,"large",['dal','onion'])
    menu.add_menu_item('pizza',pizza3)

    burger1=Burger("Naga_Burger",600,"Chicken",['Chili','chicken','onion','bread'])
    menu.add_menu_item('burger',burger1)
    burger2=Burger("Meat_Burger",400,"meat",['meat','onion','bread'])
    menu.add_menu_item('burger',burger2)
    burger3=Burger("Vegitable_Burger",300,"Vegitables",['Vegitables','onion','bread'])
    menu.add_menu_item('burger',burger3)

    drink1=Drinks("Coke",100,"2ltr",True)
    menu.add_menu_item('drink',drink1)
    drink2=Drinks("Frutika",80,"2ltr",False)
    menu.add_menu_item('drink',drink2)
    drink3=Drinks("Coffe",150,"250ml",False)
    menu.add_menu_item('drink',drink3)

    menu.show_menu()

    #restaurent
    restaurant=Restaurant("Baba_Ka_Dhaba",2000,menu)

    manager=Manager("Mumin",12000,"Jan-01,2020","Managment","1123456789","mumin.manager@gmail.com","Sylhet")
    restaurant.add_employee("manager",manager)

    chef=Chef("Mamun",10000,"Jan-01,2020","Cooking","0123456789","mamun.chef@gmail.com","Sylhet","Chinese")
    restaurant.add_employee("chef",chef)

    server=Server("rustom",2000,"Jan-01,2020","server","0223456789","rostom.manager@gmail.com","Sylhet")
    restaurant.add_employee("server",server)

    restaurant.show_employee()


    #customer

    customer1=Customer("Sakib Khan",100000,"12345678","sakibkhan@gmail.com","Gulshan-1")
    order1=Order(customer1,[pizza3,burger1,pizza2,drink1,drink2])
    customer1.place_order(order1)
    restaurant.add_order(order1)
    restaurant.receive_payment(order1,10000,customer1)

    print("First Customer",restaurant.revenue,restaurant.balance)


    customer2=Customer("Sakib Al hassan",100000,"12345678","sakibkhan@gmail.com","Gulshan-1")
    order2=Order(customer2,[pizza1,burger1,pizza2,drink3])
    customer2.place_order(order2)
    restaurant.add_order(order2)
    restaurant.receive_payment(order2,10000,customer2)

    print("After second Customer",restaurant.revenue,restaurant.balance)

    restaurant.pay_expense(restaurant.rent,"Rent")
    print("After RENT",restaurant.revenue,restaurant.balance)


#call the main
if __name__=="__main__":
    main()