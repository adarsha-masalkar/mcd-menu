from tkinter import *

menu={"Paneer McGrill":79,"Chicken McGrill":89,"McVeggie":99,"McSpicy Paneer":119,"McSpicy Chicken":139,"Veg Wrap":89,"McFloat":89,"McChicken Nuggets":119}

root=Tk()

total=0

def exit_command():
	exit()

def screen3_response(response):
	root2=Tk()
	root2.title("Transferring")
	root2.geometry("1000x1000")
	root2.configure(bg="red")
	
	cancel_button=Button(root2,fg="white",bg="red",text="Cancel",command=exit_command)
	cancel_button.place(x=400,y=100)
	
	if response==1:
		final_label=Label(root2,fg="white",bg="red",text="You can pay at the terminal ahead")
		final_label.pack()
	elif response==2:
		final_label=Label(root2,fg="white",bg="red",text="Transferring request to Transaction Portal")
		final_label.pack()
	elif response==3:
		final_label=Label(root2,fg="white",bg="red",text="Transferring request to Transaction Portal")
		final_label.pack()
	elif response==4:
		final_label=Label(root2,fg="white",bg="red",text="Transferring request to Transaction Portal")
		final_label.pack()
	elif response==5:
		exit()
		
	root.mainloop()


def screen3():
	
	root1=Tk()
	root1.geometry("1000x1000")
	root1.configure(bg="red")
	root1.title("Payment")
	
	main_label=Label(root1,fg="white",bg="red",text="How would you like to pay?")
	cash_button=Button(root1,fg="white",bg="red",text="Cash",command=lambda:screen3_response(1))
	credit_button=Button(root1,fg="white",bg="red",text="Credit Card",command=lambda:screen3_response(2))
	debit_button=Button(root1,fg="white",bg="red",text="Debit Card",command=lambda:screen3_response(3))
	upi_button=Button(root1,fg="white",bg="red",text="UPI",command=lambda:screen3_response(4))
	cancel_button=Button(root1,fg="white",bg="red",text="Cancel",command=lambda:screen3_response(5))

	main_label.place(x=200,y=100)
	cash_button.place(x=200,y=200)
	credit_button.place(x=500,y=200)
	upi_button.place(x=200,y=400)
	debit_button.place(x=500,y=400)
	cancel_button.place(x=500,y=600)
	
	
	root1.mainloop()


def callback(response):
	global total
	if response==1:
		base_label=Label(fg="white",bg="red",text="Paneer McGrill Added!")
		base_label.place(x=0,y=700)
		total+=menu["Paneer McGrill"]
	elif response==2:
		base_label=Label(fg="white",bg="red",text="Chicken McGrill Added!")
		base_label.place(x=600,y=700)
		total+=menu["Chicken McGrill"]
	elif response==3:
		base_label=Label(fg="white",bg="red",text="McVeggie Added!")
		base_label.place(x=0,y=900)
		total+=menu["McVeggie"]
	elif response==4:
		base_label=Label(fg="white",bg="red",text="McSpicy Paneer Added!")
		base_label.place(x=600,y=900)
		total+=menu["McSpicy Paneer"]
	elif response==5:
		base_label=Label(fg="white",bg="red",text="McSpicy Chicken Added!")
		base_label.place(x=0,y=1100)
		total+=menu["McSpicy Chicken"]
	elif response==6:
		base_label=Label(fg="white",bg="red",text="Veg Wrap Added!")
		base_label.place(x=600,y=1100)
		total+=menu["Veg Wrap"]
	elif response==7:
		base_label=Label(fg="white",bg="red",text="McFloat Added!")
		base_label.place(x=0,y=1300)
		total+=menu["McFloat"]
	elif response==8:
		base_label=Label(fg="white",bg="red",text="McChicken Nuggets Added!")
		base_label.place(x=600,y=1300)
		total+=menu["McChicken Nuggets"]
	elif response==9:
		base_label=Label(fg="white",bg="red",text="Shutting Down!")
		base_label.place(x=0,y=1500)
		exit()
	elif response==10:
		base_label=Label(fg="white",bg="red",text="Donated ₹20")
		base_label.place(x=600,y=1500)
		total+=20
	elif response==11:
		base_label=Label(fg="white",bg="red",text="Payment",command=screen3())
	else:
		base_label=Label(fg="white",bg="red",text="Invalid response!")
		base_label.place()
	bill_counter=Label(fg="white",bg="red",text=f"Your bill is {total}")
	bill_counter.place(x=700,y=200)
	bill_generate_button=Button(fg="white",bg="red",text="Bill",command=screen3)
	bill_generate_button.place(x=800,y=400)

def screen2():
	menu_label=Label(fg="white",bg="red",text="""Welcome to McDonald's!
What would you like to order:
1.) Paneer McGrill         ₹79
2.) Chicken McGrill       ₹89
3.) McVeggie                 ₹99
4.) McSpicy Paneer      ₹119
5.) McSpicy Chicken    ₹139
6.) Veg Wrap                 ₹89
7.) McFloat                    ₹89""")
	menu_label.place(x=0,y=0)
	title_label=Label(fg="white",bg="red",text="""What would you
like to order""")
	choice1_button=Button(fg="white",bg="red",text="Paneer McGrill",command=lambda:callback(1))
	choice1_button.place(x=0,y=600)

	choice2_button=Button(fg="white",bg="red",text="Chicken McGrill",command=lambda:callback(2))
	choice2_button.place(x=600,y=600)

	choice3_button=Button(fg="white",bg="red",text="McVeggie",command=lambda:callback(3))
	choice3_button.place(x=0,y=800)
	
	choice4_button=Button(fg="white",bg="red",text="McSpicy Paneer",command=lambda:callback(4))
	choice4_button.place(x=600,y=800)
	
	choice5_button=Button(fg="white",bg="red",text="McSpicy Chicken",command=lambda:callback(5))
	choice5_button.place(x=0,y=1000)
	
	choice6_button=Button(fg="white",bg="red",text="Veg Wrap",command=lambda:callback(6))
	choice6_button.place(x=600,y=1000)

	choice7_button=Button(fg="white",bg="red",text="McFloat",command=lambda:callback(7))
	choice7_button.place(x=0,y=1200)

	choice8_button=Button(fg="white",bg="red",text="McChicken Nuggets",command=lambda:callback(8))
	choice8_button.place(x=600,y=1200)
	
	choice9_button=Button(fg="white",bg="red",text="Quit",command=lambda:callback(9))
	choice9_button.place(x=0,y=1400)
	
	choice10_button=Button(fg="white",bg="red",text="""Donate""",command=lambda:callback(10))
	choice10_button.place(x=600,y=1400)


root.configure(bg="red")
screen2()
root.mainloop()