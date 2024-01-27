import pytest
from pantry import *

'''Testing Error Handling'''

pantry = Pantry()
@pytest.fixture
def bad_filepath():
    return{
        'filepath' : '../data/recip3/diff.md'
    }

@pytest.fixture
def bad_name():
    return{
        'name' : 'spinach'
    }
#Load Ingredients
def test_load_ingredients():
    try:
        load_ingredients(bad_filepath)
    except FileNotFoundError as error:
        pytest.fail(f"Execption raised: {error}")

#Save ingredients
def test_save_ingredients():
    try:
        save_ingredients(bad_filepath)
    except FileNotFoundError as error:
        pytest.fail(f"Execption raised: {error}")

#Add Ingredients
def test_add_ingredient():
    pantry.load_ingredients("test_file")
    try:
        pantry.add_ingredient(bad_name)
    except KeyError as error:
        pytest.fail(f"Execption raised: {error}")
        