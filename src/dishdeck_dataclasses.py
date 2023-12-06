from dataclasses import dataclass

@dataclass
class Ingredient:
	name: str
	quantity: int
	unit: str = None

	def __str__(self):
		if self.unit != None:
			return f'{self.name} | {self.quantity} {self.unit}'
		
		return f'{self.name} | {self.quantity}'

@dataclass
class Recipe:
	name: str
	source: str
	description: str
	ingredients: list[Ingredient]
	instructions: list[str]

	def __str__(self):
		string = ''
		string += f'Name: {self.name}\n'
		string += f'Source: {self.source}\n' if self.source != None else ''
		string += f'Description: {self.description}\n'
		string += 'Ingredients:\n'
		for ing in self.ingredients:
			string += f'{self.ingredient}'
		string += 'Instructions:\n'
		for i, inst in enumerate(self.instructions):
			string += f'{i + 1}: {inst}'

		return string