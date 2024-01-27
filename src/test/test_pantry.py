import pytest
from pantry import *

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


#Load Ingredients
def test_load_ingredients(bad_filepath):
    pantry = Pantry()
    try:
        pantry.load_ingredients(bad_filepath)
    except FileNotFoundError as error:
        pytest.fail(f"Exception raised: {error}")

#Save ingredients
def test_save_ingredients(bad_filepath):
    pantry = Pantry()
    
    try:
        pantry.save_ingredients(bad_filepath)
    except FileNotFoundError as error:
        pytest.fail(f"Exception raised: {error}")

#Add Ingredients
def test_add_ingredient(ex_ingredient):
    pantry = Pantry()
    pantry.add_ingredient(ex_ingredient['name'],ex_ingredient['qty'],ex_ingredient['unit'])

    storedIng = pantry._ingredients[ex_ingredient['name']]
    assert storedIng.name == ex_ingredient['name']
    assert storedIng.quantity == ex_ingredient['qty']
    assert storedIng.unit == ex_ingredient['unit']

    with pytest.raises(KeyError):
        pantry.add_ingredient(ex_ingredient['name'])