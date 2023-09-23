from tkinter import *
from tkinter import messagebox
import pandas
import csv
from datetime import date

FONT = ("Arial", 50, "bold")
B_FONT = ("Arial", 18)
L_FONT = ("Arial", 18)

class Brain:
    def __init__(self):

        self.window = Tk()
        self.window.title('Excel Data Connect')
        self.window.geometry("1920x1080")
        # self.window.config(bg='green')

        self.entry_tuple = (1, 1, 1, 1, 1)
        self.entry_list = []
        
        self.today = date.today()

        title_label = Label(self.window, text='Excel Data Connect', font=FONT, highlightthickness=0)
        title_label.pack(pady=20)

        self.pages = {
            'home_page': self.create_home_page(),
            'add_page': self.create_add_page(),
            'create_sheet_page': self.create_excel_sheet_page(),
        }

        self.show_page('home_page')

        self.window.mainloop()

    def exit(self):
        self.window.destroy()

    def save(self):
        self.cus_name = self.name_entry.get()
        self.phone_no = self.no_entry.get()
        self.product = self.product_entry.get()
        self.quantity = self.quantity_entry.get()
        
        self.new_data = [self.cus_name,self.phone_no,self.product,self.quantity]
        
        self.cols = ['Name','Phone Numbers','Products','Quantity']
        
        try:
            with open(f'{self.today}.csv',mode='r') as data_file:
                old_data = csv.reader(data_file)

        except FileNotFoundError:
            with open(f'{self.today}.csv',mode='w') as data_file:
                csv_writer = csv.writer(data_file)
                csv_writer.writerow(self.cols)
                csv_writer.writerow(self.new_data)
                
        else:
            with open(f'{self.today}.csv',mode='a') as data_file:
                csv_writer = csv.writer(data_file)
                csv_writer.writerow(self.new_data)
        
        finally:
            self.name_entry.delete(0,END)
            self.no_entry.delete(0,END)
            self.product_entry.delete(0,END)
            self.quantity_entry.delete(0,END)

    def create_home_page(self):  # home page
        home_page = Frame(self.window)

        # Buttons
        add_button = Button(home_page, text='Add Data', highlightthickness=0, font=B_FONT,command=lambda: self.show_page("add_page"))
        add_button.grid(row=0, column=1, padx=30)

        create_button = Button(home_page, text='Create New Sheet', highlightthickness=0, font=B_FONT,command=lambda: self.show_page('create_sheet_page'))
        create_button.grid(row=0, column=2, padx=30)

        exit_button = Button(home_page, text='Exit', highlightthickness=0, font=B_FONT, command=self.exit)
        exit_button.grid(row=0, column=3, padx=30, pady=30)

        return home_page

    def create_entry(self):
        if len(self.entry_list) < len(self.entry_tuple):
            self.entry_list = list(self.entry_tuple)

        # product
        self.product_entry_2 = Entry(self.add_page, width=15)
        self.product_entry_2.grid(row=len(self.entry_list), column=1)

        # quantity
        self.quantity_entry = Entry(self.add_page, width=15)
        self.quantity_entry.grid(row=len(self.entry_list), column=2)

        self.entry_list.append(self.product_entry)
        self.entry_list.append(self.quantity_entry)

    def exit_add(self):
        '''lenq = len(self.entry_list) - 5
        print(self.entry_list)
        print(lenq)
        for product_entry in self.entry_list:
            self.product_entry.destroy()
            self.quantity_entry.destroy()

        print(self.entry_list)'''
        self.show_page('home_page')

        self.entry_list.clear()

    def create_add_page(self):  # add page
        self.add_page = Frame(self.window)

        # name
        name_label = Label(self.add_page, text='Name:', font=L_FONT)
        name_label.grid(row=1, column=1, padx=50)
        name_label.focus()

        self.name_entry = Entry(self.add_page, width=30)
        self.name_entry.grid(row=1, column=2, columnspan=2)

        # phone_no
        no_label = Label(self.add_page, text='Phone Number:', font=L_FONT)
        no_label.grid(row=2, column=1)

        self.no_entry = Entry(self.add_page, width=30)
        self.no_entry.grid(row=2, column=2, columnspan=2)

        # product
        product_label = Label(self.add_page, text='Product:', font=L_FONT)
        product_label.grid(row=3, column=1, pady=10)

        self.product_entry = Entry(self.add_page, width=15)
        self.product_entry.grid(row=4, column=1)

        # quantity
        quantity_label = Label(self.add_page, text='Quantity:', font=L_FONT)
        quantity_label.grid(row=3, column=2, pady=10)

        self.quantity_entry = Entry(self.add_page, width=15)
        self.quantity_entry.grid(row=4, column=2)

        # Buttons
        self.add_button = Button(self.add_page, text='Add Data', command=self.save)
        self.add_button.grid(row=0, column=4)

        back_button = Button(self.add_page, text='Home Page', command=self.exit_add)
        back_button.grid(row=0, column=0)

        add_product_button = Button(self.add_page, text='Add Product', width=15, command=self.create_entry)
        add_product_button.grid(row=0, column=1, columnspan=2)

        return self.add_page

    def create_excel_sheet_page(self):
        excel_sheet_page = Frame(self.window)

        def create_excel_sheet():
            data_file = pandas.DataFrame(columns=["Name", "Phone No", "Product",'Quantity'])

            file_name = file_name_entry.get()

            if not file_name.endswith('.csv'):
                file_name += '.csv'

            data_file.to_excel(file_name, index=False)

            result_label.config(text=f"Excel sheet '{file_name}' created successfully")
            
        #Label
        file_name_label = Label(excel_sheet_page, text="Enter Excel File Name:",font=L_FONT)
        file_name_label.grid(row=1, column=1)
        
        result_label = Label(excel_sheet_page, text="",font=L_FONT)
        result_label.grid(row=3, column=1)

        #entry
        file_name_entry = Entry(excel_sheet_page)
        file_name_entry.grid(row=2, column=1)

        #Button
        back_button = Button(excel_sheet_page, text='Home Page', command=lambda: self.show_page('home_page'))
        back_button.grid(row=0, column=0)

        create_excel_button = Button(excel_sheet_page, text='Create', command=create_excel_sheet)
        create_excel_button.grid(row=0, column=2)

        return excel_sheet_page

    def show_page(self, page):
        # Hides all pages
        for p in self.pages.values():
            p.pack_forget()

        # Show the selected page
        self.pages[page].pack()


root = Brain()