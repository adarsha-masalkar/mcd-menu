from tkinter import *

menu = {"Paneer McGrill": 79, "Chicken McGrill": 89, "McVeggie": 99,
        "McSpicy Paneer": 119, "McSpicy Chicken": 139, "Veg Wrap": 89, "McFloat": 89, "McChicken Nuggets": 119}

root = Tk()
root.title("McDonald's")

total = 0


def exit_command():
    exit()


def screen3_response(response):
    root2 = Tk()
    root2.title("Transferring")
    root2.geometry("500x750")
    root2.configure(bg="red")

    cancel_button = Button(root2, fg="white", bg="red", text="Cancel", command=exit_command)
    cancel_button.place(x=210, y=125, height=30, width=100)

    if response == 1:
        final_label = Label(root2, fg="white", bg="red", text="You can pay at the terminal ahead")
        final_label.place(x=170, y=50)
    elif response == 2:
        final_label = Label(root2, fg="white", bg="red", text="Transferring request to Transaction Portal")
        final_label.place(x=170, y=50)
    elif response == 3:
        final_label = Label(root2, fg="white", bg="red", text="Transferring request to Transaction Portal")
        final_label.place(x=170, y=50)
    elif response == 4:
        final_label = Label(root2, fg="white", bg="red", text="Transferring request to Transaction Portal")
        final_label.place(x=170, y=50)
    elif response == 5:
        exit()

    root.mainloop()


def screen3():
    root1 = Tk()
    root1.geometry("500x750")
    root1.configure(bg="red")
    root1.title("Payment")

    main_label = Label(root1, fg="white", bg="red", text="How would you like to pay?")
    cash_button = Button(root1, fg="white", bg="red", text="Cash", command=lambda: screen3_response(1), height=2, width=20)
    credit_button = Button(root1, fg="white", bg="red", text="Credit Card", command=lambda: screen3_response(2), height=2, width=20)
    debit_button = Button(root1, fg="white", bg="red", text="Debit Card", command=lambda: screen3_response(3), height=2, width=20)
    upi_button = Button(root1, fg="white", bg="red", text="UPI", command=lambda: screen3_response(4), height=2, width=20)
    cancel_button = Button(root1, fg="white", bg="red", text="Cancel", command=lambda: screen3_response(5), height=2, width=20)

    main_label.place(x=170, y=30)
    cash_button.place(x=170, y=100)
    credit_button.place(x=170, y=175)
    upi_button.place(x=170, y=250)
    debit_button.place(x=170, y=325)
    cancel_button.place(x=170, y=400)

    root1.mainloop()


def callback(response):
    global total
    if response == 1:
        base_label = Label(fg="white", bg="red", text="Paneer McGrill Added!")
        base_label.place(x=200, y=250)
        total += menu["Paneer McGrill"]
    elif response == 2:
        base_label = Label(fg="white", bg="red", text="Chicken McGrill Added!")
        base_label.place(x=200, y=270)
        total += menu["Chicken McGrill"]
    elif response == 3:
        base_label = Label(fg="white", bg="red", text="McVeggie Added!")
        base_label.place(x=200, y=290)
        total += menu["McVeggie"]
    elif response == 4:
        base_label = Label(fg="white", bg="red", text="McSpicy Paneer Added!")
        base_label.place(x=200, y=310)
        total += menu["McSpicy Paneer"]
    elif response == 5:
        base_label = Label(fg="white", bg="red", text="McSpicy Chicken Added!")
        base_label.place(x=200, y=330)
        total += menu["McSpicy Chicken"]
    elif response == 6:
        base_label = Label(fg="white", bg="red", text="Veg Wrap Added!")
        base_label.place(x=200, y=350)
        total += menu["Veg Wrap"]
    elif response == 7:
        base_label = Label(fg="white", bg="red", text="McFloat Added!")
        base_label.place(x=200, y=370)
        total += menu["McFloat"]
    elif response == 8:
        base_label = Label(fg="white", bg="red", text="McChicken Nuggets Added!")
        base_label.place(x=200, y=390)
        total += menu["McChicken Nuggets"]
    elif response == 9:
        base_label = Label(fg="white", bg="red", text="Shutting Down!")
        base_label.place(x=200, y=410)
        exit()
    elif response == 10:
        base_label = Label(fg="white", bg="red", text="Donated ₹20")
        base_label.place(x=200, y=430)
        total += 20
    elif response == 11:
        base_label = Label(fg="white", bg="red", text="Payment", command=screen3())
    else:
        base_label = Label(fg="white", bg="red", text="Invalid response!")
        base_label.place()
    bill_counter = Label(fg="white", bg="red", text=f"Your bill is {total}")
    bill_counter.place(x=210, y=200)
    bill_generate_button = Button(fg="white", bg="red", text="Bill", command=screen3, height=1, width=5)
    bill_generate_button.place(x=300, y=200)


def screen2():
    logo = PhotoImage(file="static/mcdlogo.png")
    logo_label = Label(image=logo)
    logo_label.image = logo
    logo_label.place(x=300, y=65, height=130, width=180)
    menu_label = Label(fg="white", bg="red", text="""What would you like to order:
1.) Paneer McGrill         ₹79
2.) Chicken McGrill       ₹89
3.) McVeggie                 ₹99
4.) McSpicy Paneer      ₹119
5.) McSpicy Chicken    ₹139
6.) Veg Wrap                 ₹89
7.) McFloat                    ₹89""")
    menu_label.place(x=20, y=60)
    title_label = Label(fg="white", bg="red", text="""WELCOME TO MCDONALD'S""")
    title_label.place(x=170, y=20)

    choice1_button = Button(fg="white", bg="red", text="Paneer McGrill", command=lambda: callback(1), height=2, width=20)
    choice1_button.place(x=20, y=250)

    choice2_button = Button(fg="white", bg="red", text="Chicken McGrill", command=lambda: callback(2), height=2, width=20)
    choice2_button.place(x=330, y=250)

    choice3_button = Button(fg="white", bg="red", text="McVeggie", command=lambda: callback(3), height=2, width=20)
    choice3_button.place(x=20, y=350)

    choice4_button = Button(fg="white", bg="red", text="McSpicy Paneer", command=lambda: callback(4), height=2, width=20)
    choice4_button.place(x=330, y=350)

    choice5_button = Button(fg="white", bg="red", text="McSpicy Chicken", command=lambda: callback(5), height=2, width=20)
    choice5_button.place(x=20, y=450)

    choice6_button = Button(fg="white", bg="red", text="Veg Wrap", command=lambda: callback(6), height=2, width=20)
    choice6_button.place(x=330, y=450)

    choice7_button = Button(fg="white", bg="red", text="McFloat", command=lambda: callback(7), height=2, width=20)
    choice7_button.place(x=20, y=550)

    choice8_button = Button(fg="white", bg="red", text="McChicken Nuggets", command=lambda: callback(8), height=2, width=20)
    choice8_button.place(x=330, y=550)

    choice9_button = Button(fg="white", bg="red", text="Quit", command=lambda: callback(9), height=2, width=20)
    choice9_button.place(x=20, y=650)

    choice10_button = Button(fg="white", bg="red", text="""Donate""", command=lambda: callback(10), height=2, width=20)
    choice10_button.place(x=330, y=650)


root.configure(bg="red")
root.geometry("500x750")
screen2()
root.mainloop()
