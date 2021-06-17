import tkinter as tk
from PIL import Image, ImageTk

class LoginPage(tk.Frame):
	def __init__(self, parent, Product):
		self.product = Product
		self.settings = Product.settings

		super().__init__(parent)
		self.configure(bg="white")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, height=self.settings.height, width=self.settings.width, bg="white")
		self.main_frame.pack(expand=True)

		image = Image.open(self.settings.ikon)
		image_w, image_h = image.size
		ratio = image_w/self.settings.width
		image = image.resize((int(image_w//ratio-60),int(image_h//ratio//2)))

		self.ikon = ImageTk.PhotoImage(image)
		self.label_ikon = tk.Label(self.main_frame, image=self.ikon)
		self.label_ikon.pack(pady=5)

		self.label_username = tk.Label(self.main_frame, text="username", font=("Arial", 18, "bold"), bg="yellow", fg="black")
		self.label_username.pack(pady=5)

		self.var_username = tk.StringVar()
		self.entry_username = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), textvariable=self.var_username)
		self.entry_username.pack(pady=5)


		self.label_password = tk.Label(self.main_frame, text="password", font=("Arial", 18, "bold"), bg="yellow", fg="black")
		self.label_password.pack(pady=5)

		self.var_password = tk.StringVar()
		self.entry_password = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), show="*", textvariable=self.var_password)
		self.entry_password.pack(pady=5)

		self.btn_login = tk.Button(self.main_frame, text="LOGIN", font=("Arial", 18, "bold"), command=lambda:self.product.auth_login())
		self.btn_login.pack(pady=5)

		self.btn_register = tk.Button(self.main_frame, text = "Register", font = ("Arial", 18, "bold"), command = lambda:self.product.change_page("register_page"))
		self.btn_register.pack(pady = 5)

		self.success_register = tk.Label(self.main_frame, text = "Register success, please re-enter username and password", font = ('Arial', 14))

		self.false_msg = tk.Label(self.main_frame, text = "WRONG PASSWORD / USERNAME", font = ("Arial", 12, "bold"), bg="yellow", fg="black")