import pytest
from pantry import *

'''Testing Error Handling'''

@pytest.fixture
def bad_filepath():
    return{
        'filepath' : '../data/recip3/diff.md'
    }

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
    try:
        load_ingredients(bad_filepath)
    except FileNotFoundError as error:
        pytest.fail(f"Execption raised: {error}")

#Save ingredients
def test_save_ingredients(bad_filepath):
    try:
        save_ingredients(bad_filepath)
    except FileNotFoundError as error:
        pytest.fail(f"Execption raised: {error}")

#Add Ingredients
@pytest.mark.dependency(depends=['test_load_ingredients'])
def test_add_ingredient(tmp_path, ex_pantry):
    directory = tmp_path / f'pantry/{ex_pantry["name"]}.json'
    directory.parent.mkdir()
    directory.touch()

    pantry = Pantry()
    pantry.load_ingredients(str(directory))

    try:
        pantry.add_ingredient(used_name)
    except KeyError as error:
        pytest.fail(f"Execption raised: {error}")

def test_add_ingredient(ex_ingredient):
    pantry = Pantry()
    pantry.add_ingredient(ex_ingredient['name'],ex_ingredient['qty'],ex_ingredient['unit'])

    storedIng = pantry.__ingredients[ex_ingredient['name']]
    assert storedIng['name'] == ex_ingredient['name']
    assert storedIng['qty'] == ex_ingredient['qty']
    assert storedIng['unit'] == ex_ingredient['unit']

    try:
        pantry.add_ingredient(ex_ingredient['name'])
    except KeyError as error:
        pytest.fail(f'Execption was raised: {error}')
