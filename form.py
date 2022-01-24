from  tkinter import *

root=Tk()
root.title("Airline Reservation System")
root.geometry("400x250")


lbl=Label(root, text=" ").pack()
title=Label(root, text="Passenger Info", font=("calibri", 18, "bold"), bg="grey")
title.pack()

#frame1
frame1=LabelFrame(root,text="Passenger Info", height=150, width=300, padx=5, pady=5)
frame1.pack(padx=10, pady=10)

nm1=Label(frame1, text="Full name", font=("calibri", 12, "bold"), height=2)
nm1.grid(column=0, row=0)
psg_name1=StringVar()
nm_entry1=Entry(frame1, textvariable=psg_name1, width=36)
nm_entry1.grid(column=1, row=0, columnspan=3)

ag1=Label(frame1, text="Age", font=("calibri", 12, "bold"), height=2) 
ag1.grid(column=0, row=1)
psg_age1=StringVar()
age_entry1=Entry(frame1, textvariable=psg_age1, width=11)
age_entry1.grid(column=1, row=1)

gdr1=Label(frame1, text="Gender", font=("calibri", 12, "bold"), height=2)
gdr1.grid(column=2, row=1)
psg_gdr1=StringVar()
gdr_entry1=Entry(frame1, textvariable=psg_gdr1, width=11)
gdr_entry1.grid(column=3, row=1)

id_no1=Label(frame1, text="Passenger ID", font=("calibri", 12, "bold"), height=2)
id_no1.grid(column=0,row=2)
psg_id1=StringVar()
id_entry1=Entry(frame1, textvariable=psg_id1, width=36)
id_entry1.grid(column=1, row=2, columnspan=3)

def submit():
	return

def add():
 	return

def clear():
	return

btn_submit=Button(root, text="Submit", command=submit).pack()
btn_add=Button(root, text="Add more", command=add).pack()
btn_clear=Button(root, text="Clear", command=clear).pack()

