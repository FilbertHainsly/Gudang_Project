from json import load,dump

class Settings:

	def __init__(self):

		self.title = "Food Product"


		
		base = 50
		ratio = (16, 9)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+1000+400"

		self.logo = "img/logo.jpg"
		self.ikon = "img/ikon.jpg"


		self.users_path = "users.json"

		#self.products = None

		self.load_data_from_json()

	def load_data(self, path):
		with open(path, "r") as json_data:
			data = load(json_data)
		return data

	def save_data_user(self, data):
		with open(self.users_path, 'w') as json_data:
			dump(data, json_data)

	def login(self, username, password):
		users = self.load_data(self.users_path)
		if username in users:
			if password == users[username]["password"]:
				return True
			else:
				return False
		else:
			return False


	def load_data_from_json(self):
		with open("data/products.json","r") as file_json:
			self.products = load(file_json)

	def save_data_to_json(self):
		with open("data/products.json", "w") as file_json:
			dump(self.products, file_json)


	