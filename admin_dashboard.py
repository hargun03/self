from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
#from admin import adminclass
global root
root = Tk()


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
        cmb_search = ttk.Combobox(self.root2, textvariable=self.var_searchby, values=(
            "Select", "Admin ID", "Name", "Designation"), state="readonly", justify=CENTER, font=("Century Gothic", 14)).place(x=525, y=150, width=180)
        # cmb_search.current(0)
        txt_search = Entry(self.root2, textvariable=self.var_searchtxt, font=(
            "Century Gothic", 14), bg="#a8dadc").place(x=730, y=150)
        searchbtn = Button(self.root2, text="Search", font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=980, y=145, width=75, height=30)
        lbl_menu = Label(self.root2, text="Admin Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white")
        lbl_menu.place(x=0, y=210, relwidth=1, height=50)
        preview_frame = Frame(self.root2, bd=10, relief=RIDGE).place(
            x=0, y=260, relwidth=1, height=450)
        scrollver = Scrollbar(self.root2, orient=VERTICAL)
        self.admintable = ttk.Treeview(
            self.root2, columns=("adminid", "name", "desig"), yscrollcommand=scrollver.set)
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

    def admin(self):
        self.new_win = Toplevel(root)
        self.new_obj = adminclass(self.new_win)



class LEMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x850+0+0")
        self.root.title(
            "Laboratory Management System | Developed by Anavi, Arshia, Aryan, Ayush and Himanshu")
        self.root.config(bg="white")
        self.icon_title = PhotoImage(file="C:\epcd\self\default.png")
        title = Label(self.root, text="Admin Dashboard", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=100)
        logout_btn = Button(self.root, text="Logout", font=("Century Gothic", 15, "bold"),
                            bg="#ff9f1c", cursor="hand2").place(x=1400, y=30, height=35, width=100)
        self.lbl = Label(self.root, text="Welcome back Admin!", font=(
            "Century Gothic", 15), bg="#4d636d", fg="white")
        self.lbl.place(x=0, y=100, relwidth=1, height=35)
        #self.menulogo = Image.open("C:\epcd\self\UIET_logo.png")
        #self.menulogo = self.menulogo.resize((300, 300), Image.ANTIALIAS)
        #self.menulogo = ImageTk.PhotoImage(self.menulogo)
        Menu = Frame(self.root, bd=3, relief=RIDGE)
        Menu.place(x=0, y=135, width=1550, height=100)
        Data = Frame(self.root, bd=10, relief=RIDGE)
        Data.place(x=0, y=235, width=1550, height=475)
        #lbl_menulogo = Label(Data, image=self.menulogo)
        #lbl_menulogo.place(x=600, y=100)
        lbl_menu = Label(Menu, text="MENU", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white")
        lbl_menu.place(x=0, y=0, relwidth=1, height=50)
        Admin_btn = Button(Menu, text="Search an Admin", command=lambda:adminclass.admin(adminclass), font=("Century Gothic", 15, "bold"),
                           bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=0, y=50, height=47, width=255)
        Student_btn = Button(Menu, text="Search a Student", font=("Century Gothic", 15, "bold"),
                             bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=255, y=50, height=47, width=255)
        Complaints_btn = Button(Menu, text="Complaints System", font=("Century Gothic", 15, "bold"),
                                bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=510, y=50, height=47, width=255)
        Equipment_btn = Button(Menu, text="Equipment\nManagement", font=("Century Gothic", 13, "bold"),
                               bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=765, y=50, height=47, width=255)
        Labs_btn = Button(Menu, text="View Lab Details", font=("Century Gothic", 15, "bold"),
                          bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=1020, y=50, height=47, width=255)
        Contactus_btn = Button(Menu, text="Contact us", font=("Century Gothic", 15, "bold"),
                               bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=1275, y=50, height=47, width=255)
        lbl_footer = Label(self.root, text="LEMS - Laboratory Equipment Management System\n\nAutomative Simplification of Administration", font=(
            "Century Gothic", 14), bg="#4d636d", fg="white").place(x=0, y=705, relwidth=1, height=90)
        lbl_clock = Label(self.root, text="DATE: DD-MM-YYYY\nTIME: HH-MM-SS", font=(
            "Century Gothic", 14, "bold"), bg="#457b9d", fg="white")
        lbl_clock.place(x=1300, y=712, width=200, height=75)
        self.lbl_admin = Label(Data, text="Total Admins: [ 6 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=50, y=25, height=80, width=500)
        self.lbl_admin = Label(Data, text="Total Students: [ 60 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=50, y=130, height=80, width=500)
        self.lbl_admin = Label(Data, text="Total Labs: [ 6 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=50, y=245, height=80, width=500)
        self.lbl_admin = Label(Data, text="New Complaints: [ 10 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=50, y=350, height=80, width=500)
        self.lbl_admin = Label(Data, text="Resolved Complaints: [ 27 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=950, y=25, height=80, width=500)
        self.lbl_admin = Label(Data, text="Pending Complaints: [ 13 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=950, y=130, height=80, width=500)
        self.lbl_admin = Label(Data, text="Working Equipments: [ 48 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=950, y=245, height=80, width=500)
        self.lbl_admin = Label(Data, text="Non-working Equipments: [ 12 ] ", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=950, y=350, height=80, width=500)

    # def admin(self):
    #     self.new_win = Toplevel(self.root)
    #     self.new_obj = adminclass(self.new_win)


# if __name__ == "__main_":

obj = LEMS(root)
root.mainloop()


