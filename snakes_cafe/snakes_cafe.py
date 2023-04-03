my_string = '''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
If you want to quit just type quit and make notice that orders are case sensitive !

'''
print(my_string)


c_wings = 0
c_cookies = 0
c_sr = 0
c_sa = 0
c_st = 0
c_mt = 0
c_lg = 0
c_ic = 0
c_c=0
c_p = 0
c_co = 0 
c_t = 0
c_ut = 0

while True:
    i=input(">")
   
    if i == "Wings":
        c_wings += 1
        print(f"** {c_wings} order of {i} has been added to your meal **")
    elif i == "Cookies":
        c_cookies += 1
        print(f"** {c_cookies} order of {i} has been added to your meal **")
    elif i == "Spring Rolls":
        c_sr += 1
        print(f"** {c_sr} order of {i} has been added to your meal **")
    elif i == "Salmon":
        c_sa += 1
        print(f"** {c_sa} order of {i} has been added to your meal **")
    elif i == "Steak":
        c_st += 1
        print(f"** {c_st} order of {i} has been added to your meal **")
    elif i == "Meat Tornado":
        c_mt += 1
        print(f"** {c_mt} order of {i} has been added to your meal **")
    elif i == "A Literal Garden":
        c_lg += 1
        print(f"** {c_lg} order of {i} has been added to your meal **")
    elif i == "Ice Cream":
        c_ic += 1
        print(f"** {c_ic} order of {i} has been added to your meal **")
    elif i == "Cake":
        c_c += 1
        print(f"** {c_c} order of {i} has been added to your meal **")
    elif i == "Pie":
        c_p += 1
        print(f"** {c_p} order of {i} has been added to your meal **")
    elif i == "Coffee":
        c_co += 1
        print(f"** {c_co} order of {i} has been added to your meal **")
    elif i == "Tea":
        c_t += 1
        print(f"** {c_t} order of {i} has been added to your meal **")
    elif i == "Unicorn Tears":
        c_ut += 1
        print(f"** {c_ut} order of {i} has been added to your meal **")
    elif i == "quit":
        break
    else :
       print("Sorry, this order is not available on the menu")