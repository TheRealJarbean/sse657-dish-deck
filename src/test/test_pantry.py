import pytest
from pantry import *
import os

'''Testing Error Handling'''

@pytest.fixture
def bad_filepath():
    return "../data/recip3/diff.md"

@pytest.fixture
def used_name():
    return{
        'name' : 'flour'
    }

@pytest.fixture
def ex_ingredient():
    return{
        'name': 'flour',
        'qty': '300',
        'unit': 'grams'
    }

#Save ingredients
@pytest.mark.dependency
def test_save_ingredients(tmp_path, bad_filepath):
    good_filepath = tmp_path / 'ingredients.json'
    pantry = Pantry()
    pantry.save_ingredients(good_filepath)
    assert os.path.isfile(good_filepath)
    try:
        pantry.save_ingredients(bad_filepath)
    except FileNotFoundError as error:
        pytest.fail(f"Exception raised: {error}")

#Load Ingredients
@pytest.mark.dependency(depends=['test_save_ingredients'])
def test_load_ingredients(tmp_path, bad_filepath, ex_ingredient):
    good_filepath = tmp_path / 'ingredients.json'
    pantry = Pantry()
    pantry.add_ingredient(ex_ingredient['name'], ex_ingredient['qty'], ex_ingredient['unit'])
    pantry.save_ingredients(good_filepath)
    savedPantry = Pantry()
    savedPantry.load_ingredients(good_filepath)
    assert savedPantry.get_all_ingredients() == pantry.get_all_ingredients()
    try:
        pantry.load_ingredients(bad_filepath)
    except FileNotFoundError as error:
        pytest.fail(f"Exception raised: {error}")

#Add Ingredients
def test_add_ingredient(ex_ingredient):
    pantry = Pantry()
    pantry.add_ingredient(ex_ingredient['name'], ex_ingredient['qty'], ex_ingredient['unit'])
    storedIng = pantry._ingredients[ex_ingredient['name']]
    assert storedIng.name == ex_ingredient['name']
    assert storedIng.quantity == ex_ingredient['qty']
    assert storedIng.unit == ex_ingredient['unit']

    with pytest.raises(KeyError):
        pantry.add_ingredient(ex_ingredient['name'])