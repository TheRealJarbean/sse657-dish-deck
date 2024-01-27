import json
from typing import Literal
from dishdeck_dataclasses import *

class Pantry:
	# This is a collection of ingredients, along with their quantities and units
	# Each ingredient is a dictionary entry, with the key being the ingredient's name (normalized)
	# Each entry contains an Ingredient object with name, qty, and unit
	# qty and unit do not need to be specified, but qty must be specified if unit is specifie

	def __init__(self):
		self._ingredients: dict[Ingredient] = {}

	def load_ingredients(self, filepath: str):
		with open(filepath, 'r') as file:
			ingredients_as_lists: dict = json.loads(file.read())
		self._ingredients = {key: Ingredient(ing[0], ing[1], ing[2]) for key, ing in ingredients_as_lists.items()}

	def save_ingredients(self, filepath: str):
		ingredients_as_lists = {key: [ing.name, ing.quantity, ing.unit] for key, ing in self._ingredients.items()}
		with open(filepath, 'w') as file:
			file.write(json.dumps(ingredients_as_lists))

	def add_ingredient(self, name: str, qty: float = None, unit: str = None):
		name_normalized = name.lower().replace(' ', '')
		if name_normalized not in self._ingredients:
			self._ingredients[name_normalized] = Ingredient(name, qty, unit)
			return
		raise KeyError('Ingredient with that name already exists.')

	# Removes the Ingredient object associated with the input name from the pantry, if there is one
	def remove_ingredient(self, name: str):
		name_normalized = name.lower().replace(' ', '')
		if name_normalized in self._ingredients:
			del self._ingredients[name_normalized]
			return
		raise KeyError('Ingredient with that name not in pantry.')

	# Returns the Ingredient object associated with the input name, if there is one
	# Otherwise returns None
	def get_ingredient(self, name: str) -> list[Ingredient] | None:
		name_normalized = name.lower().replace(' ', '')
		if name_normalized in self._ingredients:
			return self._ingredients[name_normalized]
		return None
	
	# Returns a list of Ingredient objects containing every ingredient in the pantry
	# Or an empty list if there are none
	def get_all_ingredients(self) -> list[Ingredient]:
		return list(self._ingredients.values())
	
	def edit_ingredient(self, name: str, field: Literal['name', 'qty', 'unit'], value: str | float):
		name_normalized = name.lower().replace(' ', '')
		if name_normalized not in self._ingredients:
			raise KeyError("Ingredient not found in pantry")
		
		if field == 'name':
			if not isinstance(value, str):
				raise TypeError('Value must be a string when editing name')
			value_normalized = value.lower().replace(' ', '')
			if value_normalized in self._ingredients:
				raise KeyError('Ingredient with this name already exists')
			self._ingredients[value_normalized] = self._ingredients[name_normalized]
			del self._ingredients[name_normalized]
			self._ingredients[value_normalized].name = value

		if field == 'qty':
			if not isinstance(value, float | int):
				raise TypeError('Value must be a float when editing quantity')
			self._ingredients[name_normalized].quantity = float(value)

		if field == 'unit':
			if not isinstance(value, str):
				raise TypeError('Value must be a string when editing unit')
			if self._ingredients[name_normalized].quantity == None:
				raise ValueError('Unit cannot be added when Quantity has value None')
			self._ingredients[name_normalized].unit = value