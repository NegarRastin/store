from tkinter import *
from tkinter import ttk

from controller.customer_controller import CustomerController
from view.component import Table

class CustomerView:
    def __init__(self):
        win = Tk()
        win.geometry("300x300")

        self.person_table = Table(win, ["Id", "Name", "Family", "Age"], [50,80,80,50],20,20, self.person_table_click)

        self.person_table.set_data(CustomerController.find_all()[0])

        win.mainloop()

    def person_table_click(row):
        print(row)

    


