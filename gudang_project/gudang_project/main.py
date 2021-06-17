import tkinter as tk
from tkinter import messagebox as msg

from settings import Settings
from product import Product
from loginPage import LoginPage
from registerPage import RegisterPage


class Window(tk.Tk):

	def __init__(self, Product):
		self.product = Product
		self.settings = Product.settings

		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_menus()
		self.create_container()
		self.pages = {}
		self.create_Product()
		self.creater_registerPage()
		self.create_loginPage()

	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)

	def create_menus(self):
		self.menuBar = tk.Menu(self)
		self.configure(menu=self.menuBar)

		self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
		self.fileMenu.add_command(label="New Product")
		self.fileMenu.add_command(label="Exit", command=self.exit_program)

		self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
		self.helpMenu.add_command(label="About", command=self.show_about_info)

		self.menuBar.add_cascade(label="File", menu=self.fileMenu)
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)

	def create_Product(self):
		self.pages['product'] = Product(self.container, self.product)

	def create_loginPage(self):
		self.pages['loginPage'] = LoginPage(self.container, self.product)

	def creater_registerPage(self):
		self.pages["register_page"] = RegisterPage(self.container, self.product)

	def show_about_info(self):
		msg.showinfo("About Product App", "This apps created by\n1. Admin1\n2. Admin2\n\nCopyright 2021")

	def exit_program(self):
		respond = msg.askyesnocancel("Exit Program", "Are you sure and really sure to close the program ?")
		print(respond)

class FoodProduct:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

		self.loaded_users = self.settings.load_data(self.settings.users_path)

	def auth_login(self):
		username = self.window.pages['loginPage'].var_username.get()
		password = self.window.pages['loginPage'].var_password.get()

		granted = self.settings.login(username, password)
		if granted:
			self.change_page('product')
		else:
			self.window.pages['loginPage'].false_msg.pack(pady= 5)

	def auth_register(self):
		username = self.window.pages['register_page'].var_username.get()
		password = self.window.pages['register_page'].var_password.get()
		confirmed_password = self.window.pages['register_page'].var_confirmPassword.get()

		if password == confirmed_password:
			self.loaded_users[username] = {
				"password" : password,
				"level" : "worker"
			}
			self.change_page("loginPage")
			self.window.pages["loginPage"].success_register.pack(pady = 3)
			self.settings.save_data_user(self.loaded_users)
		else:
			self.window.pages["register_page"].error_msg.pack(pady = 3)

	def change_page(self, page):
		self.window.pages[page].tkraise()

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	myFoodProduct = FoodProduct()
	myFoodProduct.run()