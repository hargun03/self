from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3


class adminclass:
    def __init__(self, root2):
        self.root2 = root2
        self.root2.geometry("1550x850+0+0")
        self.root2.title(
            "Laboratory Management System | Developed by Anavi, Arshia, Aryan, Ayush and Himanshu")
        self.root2.config(bg="white")
        self.root2.focus_force()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_admin_id = StringVar()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root2, text="Search Admin", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=100)
        searchadmin = LabelFrame(self.root2, text="Search an Admin", font=(
            "Century Gothic", 20, "bold"), bd=3, relief=RIDGE, bg="white").place(x=500, y=100, width=600, height=100)
        cmb_search = ttk.Combobox(searchadmin, textvariable=self.var_searchby, values=(
            "Select", "Admin ID", "Name", "Designation"), state="readonly", justify=CENTER, font=("Century Gothic", 14)).place(x=525, y=150, width=180)
        # cmb_search.current(0)
        txt_search = Entry(searchadmin, textvariable=self.var_searchtxt, font=(
            "Century Gothic", 14), bg="#a8dadc").place(x=730, y=150)
        searchbtn = Button(searchadmin, text="Search", font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=980, y=145, width=75, height=30)
        lbl_menu = Label(self.root2, text="Admin Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white")
        lbl_menu.place(x=0, y=210, relwidth=1, height=50)
        preview_frame = Frame(self.root2, bd=10, relief=RIDGE).place(
            x=0, y=260, relwidth=1, height=450)
        scrollver = Scrollbar(preview_frame, orient=VERTICAL)
        self.admintable = ttk.Treeview(
            preview_frame, columns=("adminid", "name", "desig"), yscrollcommand=scrollver.set)
        self.admintable.heading("adminid", text="Admin ID")
        self.admintable.heading("name", text="Name")
        self.admintable.heading("desig", text="Designation")
        self.admintable["show"] = "headings"
        self.admintable.place(x=10, y=270, width=1500, height=450)
        scrollver.place(x=1510, y=265, height=440, width=20)
        scrollver.config(command=self.admintable.yview)
        lbl_footer = Label(self.root2, text="LEMS - Laboratory Equipment Management System\n\nAutomative Simplification of Administration", font=(
            "Century Gothic", 14), bg="#4d636d", fg="white").place(x=0, y=705, relwidth=1, height=90)
        lbl_clock = Label(self.root2, text="DATE: DD-MM-YYYY\nTIME: HH-MM-SS", font=(
            "Century Gothic", 14, "bold"), bg="#457b9d", fg="white")
        lbl_clock.place(x=1300, y=712, width=200, height=75)


if __name__ == "__main_":
    root2 = Tk()
    obj = adminclass(root2)
    root2.mainloop()
