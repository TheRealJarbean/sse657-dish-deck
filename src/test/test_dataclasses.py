import pytest
import os
from dishdeck_dataclasses import *

@pytest.fixture
def ex_ing():
	return {
		'name': 'cheese wheels',
		'qty': 13742,
		'unit': 'wheels'
	}

@pytest.fixture
def ex_recipe():
	return {
		'name': 'Fig Newtons',
		'description': 'It\'s just Fig Newtons',
		'ingredients': [Ingredient('Fig', 2), Ingredient('Newton', 4, 'Whole')],
		'instructions': '1. Add the fig.\n2. Add the Newton.\n3. Enjoy'
	}

# TEST FROM ORIGINAL PROJECT
@pytest.mark.dependency()
def test_ingredient_instantiation(ex_ing):
	ingredient = Ingredient(ex_ing['name'], ex_ing['qty'], ex_ing['unit'])
	assert (
		ingredient.name == ex_ing['name'] and
		ingredient.quantity == ex_ing['qty'] and
		ingredient.unit == ex_ing['unit']
	)

# TEST FROM ORIGINAL PROJECT
@pytest.mark.dependency()
def test_ingredient_instantiation_nounit(ex_ing):
	ingredient = Ingredient(ex_ing['name'], ex_ing['qty'])
	assert (
		ingredient.name == ex_ing['name'] and
		ingredient.quantity == ex_ing['qty'] and
		ingredient.unit == None
	)

# TEST FROM ORIGINAL PROJECT
@pytest.mark.dependency(depends=['test_ingredient_instantiation', 'test_ingredient_instantiation_nounit'])
def test_recipe_instantiation(ex_recipe):
	recipe = Recipe(
		ex_recipe['name'],
		None,
		'https://www.youtube.com',
		ex_recipe['description'],
		ex_recipe['ingredients'],
		ex_recipe['instructions']
	)

	assert (
		recipe.name == ex_recipe['name'] and
		recipe.tags == None and
		recipe.source == 'https://www.youtube.com' and
		recipe.description == ex_recipe['description'] and
		recipe.ingredients == ex_recipe['ingredients'] and
		recipe.instructions == ex_recipe['instructions']
	)

# TEST FROM ORIGINAL PROJECT
@pytest.mark.dependency(depends=['test_ingredient_instantiation', 'test_ingredient_instantiation_nounit'])
def test_recipe_instantiation_nosource(ex_recipe):
	recipe = Recipe(
		ex_recipe['name'],
		None,
		None,
		ex_recipe['description'],
		ex_recipe['ingredients'],
		ex_recipe['instructions']
	)

	assert (
		recipe.name == ex_recipe['name'] and
		recipe.tags == None and
		recipe.source == None and
		recipe.description == ex_recipe['description'] and
		recipe.ingredients == ex_recipe['ingredients'] and
		recipe.instructions == ex_recipe['instructions'] 
	)

# NEW TEST
@pytest.mark.dependency(depends=['test_recipe_instantiation'])
def test_recipe_save(tmp_path, ex_recipe):
	directory = tmp_path / "recipes"
	directory.mkdir()
	recipe = Recipe(
		ex_recipe['name'],
		None,
		'https://www.youtube.com',
		ex_recipe['description'],
		ex_recipe['ingredients'],
		ex_recipe['instructions']
	)
	recipe.save(str(directory))
	assert os.path.isfile(directory / f'{ex_recipe["name"]}.md')

# NEW TEST
@pytest.mark.dependency(depends=['test_recipe_save'])
def test_recipe_delete(tmp_path, ex_recipe):
	directory = tmp_path / f'recipes/{ex_recipe["name"]}.md'
	directory.parent.mkdir()
	directory.touch()
	recipe = Recipe(
		ex_recipe['name'],
		None,
		'https://www.youtube.com',
		ex_recipe['description'],
		ex_recipe['ingredients'],
		ex_recipe['instructions']
	)
	recipe.delete(str(directory))
	assert not os.path.isfile(directory / f'{ex_recipe["name"]}.md')