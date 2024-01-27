from dishdeck_dataclasses import *

class RecipeBook:
	def __init__(self):
		
		# This is a dictionary of Recipes.
		# Each recipe name points to a Recipe object containing:
		# name, source, description, ingredients, and instructions
		self._recipes: dict[Recipe] = {}

	def import_recipe(self, filepath: str):
		recipe_data = {
			"name": "",
			"tags": [],
			"source": "",
			"description": "",
			"ingredients": [], # Each element should be in the form: [name, quantity]
			"instructions": []
		}
		with open(filepath, 'r') as file:
			lines = file.readlines()

			recipe_data["name"] = lines[0].strip()[2:]
			if lines[1].startswith('#'):
				recipe_data["tags"] = lines[1].split(', ')
				source_line = 2
			else:
				recipe_data["tags"] = None
				source_line = 1
			if lines[source_line].startswith('['):
				recipe_source = lines[source_line].strip()
				# Trim off the markdown link label and parenthesis
				recipe_data["source"] = recipe_source.split("(")[1][:-1]
			else:
				recipe_data["source"] = None

			key = ""
			for line in lines[2:]:
				current_line = line.strip()
				if current_line == "":
					continue
				if line[:2] == "##":
					key = current_line [3:] # Trim header identifier
					continue
				if key == "Description":
					recipe_data["description"] += current_line
					continue
				if key == "Ingredients":
					current_line = current_line[6:] # Trim checkbox and spaces
					ingredient_data = current_line.split(' | ') # Separate ingredient name and qty/unit
					if len(ingredient_data) != 1:
						ingredient_data = [ingredient_data[0]] + ingredient_data[1].split() # Separate qty and unit
					recipe_data["ingredients"].append(Ingredient(*tuple(ingredient_data)))
					continue
				if key == "Instructions":
					current_line = current_line[3:] # Trim instruction number
					recipe_data["instructions"].append(current_line)
		
		new_recipe = Recipe(recipe_data["name"], recipe_data["tags"], None, recipe_data["description"], recipe_data["ingredients"], recipe_data["instructions"])
		self._recipes[recipe_data["name"].lower()] = new_recipe

	def add_recipe(self, directory: str, name: str, tags: list[str], source: str | None, description: str, ingredients: list[Ingredient], instructions: list[str]):
		new_recipe = Recipe(name, tags, source, description, ingredients, instructions)
		new_recipe.save(directory)
		self._recipes[name] = new_recipe

	#Get recipe object
	def get_recipe(self, recipe_name):
		if recipe_name in self._recipes:
			return self._recipes[recipe_name]
		else:
			return None

	def get_recipe_names(self):
		return list(self._recipes.keys())

	def get_recipe_desc(self, recipe_name: str):
		if recipe_name in self.get_recipe_names():
			return self._recipes[recipe_name].description
		
	def get_recipe_ingredients(self, recipe_name: str):
		if recipe_name in self.get_recipe_names():
			return self._recipes[recipe_name].ingredients
		
	def search_recipes(self, search_terms: list[str]) -> list[Recipe]:
		# Separate tags so they can be treated differently
		tags = [term for term in search_terms if term.startswith('#')]
		search_terms = [term for term in search_terms if term not in tags]
		results = []
		for key, recipe in self._recipes.items():
			if all(tag in recipe.tags for tag in tags) and all(term.lower() in recipe.name.lower() for term in search_terms):
				results.append(key)
		return results