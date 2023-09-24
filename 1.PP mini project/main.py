from tkinter import *
from tkinter import messagebox
import pandas
from datetime import date

FONT = ("Garamond", 50, "bold",)
B_FONT = ("Times new roman", 18)
L_FONT = ("Arial", 18)
PAGE_LABEL_BG = '#25274d'
BUTTON_BG = '#2e9cca'

class Brain:
    def __init__(self):

        self.window = Tk()
        self.window.title('Excel Data Connect')
        self.window.attributes('-fullscreen',True)
        self.window.config(bg=PAGE_LABEL_BG)

        self.p_e_list = []
        self.q_e_list = []
        self.pr_e_list = []
        
        self.today = date.today()

        title_label = Label(self.window, text='Excel Data Connect',fg='white', font=FONT,bg=PAGE_LABEL_BG, highlightthickness=0)
        title_label.pack(pady=20)

        self.pages = {
            'home_page': self.create_home_page(),
            'add_page': self.create_add_page(),
            'create_sheet_page': self.create_excel_sheet_page(),
        }

        self.show_page('home_page')

        self.window.mainloop()

    def save(self):
        product_list = []
        quantity_list = []
        price_list = []
        
        cus_name = self.name_entry.get()
        phone_no = self.no_entry.get()
        product = self.product_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        
        for entry in self.p_e_list:
            p_data = entry.get()
            product_list.append(p_data)
            
        for entry in self.q_e_list:
            q_data = entry.get()
            quantity_list.append(q_data)
            
        for entry in self.pr_e_list:
            pr_data = entry.get()
            price_list.append(pr_data)
        
        data = {
            'Name':[cus_name],
            'Phone No':[phone_no],
            'Product': [product],
            'Quantity':[quantity],
            'Price':[price]
        }
        
        data_file = pandas.DataFrame(data)
        
        if len(cus_name) == 0 or len(phone_no) == 0 or len(product) == 0 or len(quantity) == 0 or len(price) == 0:
            messagebox.showinfo(title='Oops!!', message='Please make sure you haven\'t left any fields empty.')
        else:
            try:
                pandas.read_csv(f'{self.today}.csv')

            except FileNotFoundError:
                if not len(product_list) == 0 or len(quantity_list) == 0 or len(price_list) == 0:
                    data_file.to_csv(f'{self.today}.csv',mode='w',index=False,header=True)
                    
                    for (product_2,quantity_2,price_2) in zip(product_list,quantity_list,price_list):
                        new_data = {
                            'Name':cus_name,
                            'Phone No':phone_no,
                            'Product': [product_2],
                            'Quantity':[quantity_2],
                            'Price':[price_2]
                        }
                        new_data_file = pandas.DataFrame(new_data)
                        new_data_file.to_csv(f'{self.today}.csv',mode='a',index=False,header=False)
                        
                else:
                    data_file.to_csv(f'{self.today}.csv',mode='w',index=False,header=True)
                        
            else:
                if not len(product_list) == 0 or len(quantity_list) == 0 or len(price_list) == 0:
                    data_file.to_csv(f'{self.today}.csv',mode='a',index=False,header=False)
                    
                    for (product_2,quantity_2,price_2) in zip(product_list,quantity_list,price_list):
                        new_data = {
                            'Name':cus_name,
                            'Phone No':phone_no,
                            'Product': [product_2],
                            'Quantity':[quantity_2],
                            'Price':[price_2]
                        }
                        new_data_file = pandas.DataFrame(new_data)
                        new_data_file.to_csv(f'{self.today}.csv',mode='a',index=False,header=False)
                else:
                    data_file.to_csv(f'{self.today}.csv',mode='a',index=False,header=False)
            
            finally:
                self.name_entry.delete(0,END)
                self.no_entry.delete(0,END)
                self.product_entry.delete(0,END)
                self.quantity_entry.delete(0,END)
                self.price_entry.delete(0,END)
                for (p_entry,q_entry,pr_entry) in zip(self.p_e_list,self.q_e_list,self.pr_e_list):
                    p_entry.destroy()
                    q_entry.destroy()
                    pr_entry.destroy()
                messagebox.showinfo(title='Excel Data Connect', message=f'Data has been added to file {self.today}.csv')

    def create_home_page(self):  # home page
        home_page = Frame(self.window)
        home_page.config(bg=PAGE_LABEL_BG)

        # Buttons
        add_button = Button(home_page, text='Add Data',bg=BUTTON_BG, highlightthickness=0, font=B_FONT,command=lambda: self.show_page("add_page"))
        add_button.grid(row=0, column=1, padx=30)

        create_button = Button(home_page, text='Create New Sheet',bg=BUTTON_BG, highlightthickness=0, font=B_FONT,command=lambda: self.show_page('create_sheet_page'))
        create_button.grid(row=0, column=2, padx=30)

        exit_button = Button(home_page, text='Exit', highlightthickness=0,bg=BUTTON_BG, font=B_FONT, command=self.exit)
        exit_button.grid(row=0, column=3, padx=30, pady=30)

        return home_page
    
    def create_add_page(self):  # add page
        self.add_page = Frame(self.window)
        self.add_page.config(bg=PAGE_LABEL_BG)

        # name
        name_label = Label(self.add_page, text='Name:', font=L_FONT,bg=PAGE_LABEL_BG,fg='White')
        name_label.grid(row=1, column=1, padx=50)
        name_label.focus()

        self.name_entry = Entry(self.add_page, width=30)
        self.name_entry.grid(row=1, column=2, columnspan=2)

        # phone_no
        no_label = Label(self.add_page, text='Phone Number:', font=L_FONT,bg=PAGE_LABEL_BG,fg='White')
        no_label.grid(row=2, column=1)

        self.no_entry = Entry(self.add_page, width=30)
        self.no_entry.grid(row=2, column=2, columnspan=2)

        # product
        product_label = Label(self.add_page, text='Product:', font=L_FONT,bg=PAGE_LABEL_BG,fg='White')
        product_label.grid(row=3, column=1, pady=10)

        self.product_entry = Entry(self.add_page, width=15)
        self.product_entry.grid(row=4, column=1)

        # quantity
        quantity_label = Label(self.add_page, text='Quantity:', font=L_FONT,bg=PAGE_LABEL_BG,fg='White')
        quantity_label.grid(row=3, column=2, pady=10,padx=70)

        self.quantity_entry = Entry(self.add_page, width=15)
        self.quantity_entry.grid(row=4, column=2)
        
        #price
        price_label = Label(self.add_page, text='Price:', font=L_FONT,bg=PAGE_LABEL_BG,fg='White')
        price_label.grid(row=3, column=3, pady=10,padx=50)
        
        self.price_entry = Entry(self.add_page, width=15)
        self.price_entry.grid(row=4, column=3)

        # Buttons
        self.add_button = Button(self.add_page, text='Add Data', command=self.save,bg=BUTTON_BG)
        self.add_button.grid(row=0, column=4,pady=10)

        back_button = Button(self.add_page, text='Home Page', command=self.exit_add,bg=BUTTON_BG)
        back_button.grid(row=0, column=0)

        add_product_button = Button(self.add_page, text='Add Product', width=15, command=self.create_entry,bg=BUTTON_BG)
        add_product_button.grid(row=0, column=2)

        return self.add_page

    def create_entry(self):
        # product
        self.product_entry_2 = Entry(self.add_page, width=15)
        self.product_entry_2.grid(row=len(self.p_e_list)+5, column=1)

        # quantity
        self.quantity_entry_2 = Entry(self.add_page, width=15)
        self.quantity_entry_2.grid(row=len(self.q_e_list)+5, column=2)
        
        #price
        self.price_entry_2 = Entry(self.add_page, width=15)
        self.price_entry_2.grid(row=len(self.pr_e_list)+5, column=3)

        self.p_e_list.append(self.product_entry_2)
        self.q_e_list.append(self.quantity_entry_2)
        self.pr_e_list.append(self.price_entry_2)

    def exit_add(self):
        self.name_entry.delete(0,END)
        self.no_entry.delete(0,END)
        self.product_entry.delete(0,END)
        self.quantity_entry.delete(0,END)
        self.price_entry.delete(0,END)
        for (p_entry,q_entry,pr_entry) in zip(self.p_e_list,self.q_e_list,self.pr_e_list):
            p_entry.destroy()
            q_entry.destroy()
            pr_entry.destroy()
        
        self.show_page('home_page')

        self.p_e_list.clear()
        self.q_e_list.clear()
        self.pr_e_list.clear()
   
    def exit(self):
        self.window.destroy()

    def create_excel_sheet_page(self):
        excel_sheet_page = Frame(self.window)
        excel_sheet_page.config(bg=PAGE_LABEL_BG)

        def create_excel_sheet():
            data_file = pandas.DataFrame(columns=["Name", "Phone No", "Product",'Quantity','Price'])

            file_name = file_name_entry.get()
            
            if len(file_name) == 0 :
                messagebox.showinfo(title='Oops!!', message='Please make sure you haven\'t left any fields empty.')
            else:    
                if not file_name.endswith('.csv'):
                    file_name += '.csv'

                data_file.to_csv(file_name, index=False)

                messagebox.showinfo(title='',message=f'Excel sheet {file_name} created successfully')
                file_name_entry.delete(0,END)
            
        #Label
        file_name_label = Label(excel_sheet_page, text="Enter Excel File Name:",font=L_FONT,bg=PAGE_LABEL_BG,fg='White')
        file_name_label.grid(row=1, column=1)

        #entry
        file_name_entry = Entry(excel_sheet_page)
        file_name_entry.grid(row=2, column=1)

        #Button
        back_button = Button(excel_sheet_page, text='Home Page', bg=BUTTON_BG,command=lambda: self.show_page('home_page'))
        back_button.grid(row=0, column=0)

        create_excel_button = Button(excel_sheet_page, text='Create',bg=BUTTON_BG, command=create_excel_sheet)
        create_excel_button.grid(row=0, column=2)

        return excel_sheet_page

    def show_page(self, page):
        # Hides all pages
        for p in self.pages.values():
            p.pack_forget()

        # Show the selected page
        self.pages[page].pack()

root = Brain()