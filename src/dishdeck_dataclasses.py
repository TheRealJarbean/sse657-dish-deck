from __future__ import annotations
from dataclasses import dataclass
from os import remove

#Creates all the classes for the project

@dataclass
class Ingredient:
	name: str
	quantity: int = None
	unit: str = None

	def __str__(self):
		if self.unit != None:
			return f'{self.name} | {self.quantity} {self.unit}'
		
		if self.quantity != None:
			return f'{self.name} | {self.quantity}'
		
		return f'{self.name}'

@dataclass
class Recipe:
	name: str
	tags: list[str]
	source: str | None
	description: str
	ingredients: list[Ingredient]
	instructions: list[str]

	def __str__(self):
		string = ''
		string += f'# {self.name}\n'
		if self.tags != None:
			string += ', '.join(self.tags) + '\n'
		string += f'[Source]({self.source})\n\n' if self.source != None else '\n'
		string += f'## Description\n\n{self.description}\n\n'
		string += '## Ingredients\n\n'
		for ing in self.ingredients:
			string += f'- [ ] {ing}\n'
		string += '\n## Instructions\n\n'
		for i, inst in enumerate(self.instructions):
			string += f'{i + 1}. {inst}\n\n'

		return string
	
	def save(self, directory: str):
		filepath = directory + '/' + self.name + '.md'
		with open(filepath, 'w') as file:
			file.write(self.__str__())

	def delete(self, directory: str):
		filepath = directory + '/' + self.name + '.md'
		try:
			remove(filepath)
			return 'Recipe successfully deleted.'
		except FileNotFoundError:
			return 'Recipe file not found.'