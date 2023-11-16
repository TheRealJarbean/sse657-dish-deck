class RecipeBook:
	def __init__(self):
		
		# This is a dictionary of dictionaries.
		# Each recipe name points to a dictionary containing:
		# source, description, ingredients, and instructions
		self.__recipes = {}

	def add_recipe(self, filepath: str):
		recipe_name = ""
		recipe_data = {
			"source": "",
			"description": "",
			"ingredients": [], # Each element should be in the form: [name, quantity]
			"instructions": []
		}
		with open(filepath, 'r') as file:
			lines = file.readlines()

			recipe_name = lines[0].strip()[2:]
			recipe_source = lines[1].strip()
			if recipe_source != "":
				# Trim off the markdown link label and parenthesis
				recipe_data["source"] = recipe_source.split("(")[1][:-1]

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
					recipe_data["ingredients"].append(current_line.split(" | "))
					continue
				if key == "Instructions":
					current_line = current_line[3:] # Trim instruction number
					recipe_data["instructions"].append(current_line)
		
		self.__recipes[recipe_name.lower()] = recipe_data

	def get_recipe_names(self):
		return list(self.__recipes.keys())

	def get_recipe_desc(self, recipe_name: str):
		# TODO: replace with try/catch for error handling
		if recipe_name in self.get_recipe_names():
			return self.__recipes[recipe_name]["description"]