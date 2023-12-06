class Ingredient:
	def __init__(self, name: str, quantity: int, unit: str):
		self.name = name
		self.quantity = quantity
		self.unit = unit

	def __str__(self):
		return f'{self.name} | {self.quantity} | {self.unit}'

class Recipe:
	def __init__(self, name: str, source: str, description: str, ingredients: list[Ingredient], instructions: list[str]):
		self.name = name
		self.source = source
		self.description = description
		self.ingredients = ingredients
		self.instructions = instructions

	def __str__(self):
		string = ''
		string += f'Name: {self.name}\n'
		string += f'Source: {self.source}\n'
		string += f'Description: {self.description}\n'
		string += 'Ingredients:\n'
		for ing in self.ingredients:
			string += f'{self.ingredient}'
		string += 'Instructions:\n'
		for i, inst in enumerate(self.instructions):
			string += f'{i + 1}: {inst}'

		return string