import pytest
from recipebook import *

@pytest.fixture
def ex_recipe_data():
	return {
		'name': 'Fig Newtons',
		'description': 'It\'s just Fig Newtons',
		'ingredients': [Ingredient('Fig', 2), Ingredient('Newton', 4, 'Whole')],
		'instructions': '1. Add the fig.\n2. Add the Newton.\n3. Enjoy'
	}

@pytest.fixture
def ex_recipe(tmp_path, ex_recipe_data):
	recipe = Recipe(
		ex_recipe_data['name'],
		None,
		None,
		ex_recipe_data['description'],
		ex_recipe_data['ingredients'],
		ex_recipe_data['instructions']
	)
	return recipe

@pytest.fixture
def ex_recipebook(tmp_path, ex_recipe_data):
	directory = tmp_path / 'fixture'
	directory.mkdir()
	recipeBook = RecipeBook()
	recipeBook.add_recipe(
		str(directory),
		ex_recipe_data['name'],
		None,
		None,
		ex_recipe_data['description'],
		ex_recipe_data['ingredients'],
		ex_recipe_data['instructions']
	)
	recipeBook.add_recipe(
		str(directory),
		'Another Recipe',
		None,
		None,
		'Another description',
		ex_recipe_data['ingredients'],
		['additional instructions']
	)
	return recipeBook

@pytest.mark.dependency()
def test_add_recipe(tmp_path, ex_recipe_data):
	directory = tmp_path / 'test'
	directory.mkdir()
	recipeBook = RecipeBook()
	recipeBook.add_recipe(
		str(directory),
		ex_recipe_data['name'],
		None,
		None,
		ex_recipe_data['description'],
		ex_recipe_data['ingredients'],
		ex_recipe_data['instructions']
	)

	storedRecipe = recipeBook._recipes[ex_recipe_data['name']]
	assert storedRecipe.name == ex_recipe_data['name']
	assert storedRecipe.tags == None
	assert storedRecipe.source == None
	assert storedRecipe.description == ex_recipe_data['description']
	assert storedRecipe.ingredients == ex_recipe_data['ingredients']
	assert storedRecipe.instructions == ex_recipe_data['instructions']

@pytest.mark.dependency(depends=['test_add_recipe'])
def test_get_recipe(ex_recipebook, ex_recipe, ex_recipe_data):
	assert ex_recipebook.get_recipe(ex_recipe_data['name']) == ex_recipe
	assert ex_recipebook.get_recipe('not found') == None

@pytest.mark.dependency(depends=['test_add_recipe'])
def test_get_recipe_names(ex_recipebook, ex_recipe_data):
	assert ex_recipebook.get_recipe_names() == [ex_recipe_data['name'], 'Another Recipe']

@pytest.mark.dependency(depends=['test_add_recipe'])
def test_get_recipe_desc(ex_recipebook, ex_recipe_data):
	assert ex_recipebook.get_recipe_desc(ex_recipe_data['name']) == ex_recipe_data['description']

@pytest.mark.dependency(depends=['test_add_recipe'])
def test_get_recipe_ingredients(ex_recipebook, ex_recipe_data):
	assert ex_recipebook.get_recipe_ingredients(ex_recipe_data['name']) == ex_recipe_data['ingredients']