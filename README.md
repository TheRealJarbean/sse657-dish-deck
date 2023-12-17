# Dish Deck
*The simplest way to organize your recipes.*

## Requirements
- Python 3.10+
- PySimpleGUI (pip install PySimpleGUI)
- python-docx (pip install PySimpleGUI)

## Installation Command
```bash
git clone https://github.com/TheRealJarbean/sse657-dish-deck.git
```

## Usage Instructions

1. Navigate to the directory to which you cloned the project files. Start the program by running the following in your command line: 
```bash
python src/uiux.py
```
2. Add recipes to the recipe book by navigating to the **Add Recipe** tab and filling out the requisite fields. The required fields are "name", "description", "ingredients", and "instructions". Once at least those fields have been filled, click **Add Recipe** to save the recipe to the Recipe Book (and the local disk).
3. Add ingredients to the pantry by navigating to the **Pantry** tab and filling out the requisite fields, then clicking **Add**. Pantry items can be removed by clicking on them in the list. Clicking **Save Pantry** will save pantry data to the local disk so that it can be loaded on future program launches.
4. Browse recipes by navigating to the **Recipe Book** tab. Clicking a recipe's thumbnail or description text will open its full description. Recipes can be searched by name or by *tags*. Multiple search terms can be used by separating them with ", ". Checking the box next to a recipe will add it's ingredients to the ingredients list on the right. An ingredient's box will be ticked if the ingredient is present and above the requisite quantity in the pantry. The recipe's name will be added to the selected recipes list below the ingredients list. Clicking a recipe in the recipe list will pull it up in the recipe browser space.
5. Click the **Export Groceries** button to generate a printable docx file that matches the listed ingredients and their checkboxes.

> [!CAUTION]
> We do not store or track your data, but that does not mean your own machine is completely protected. Do not include any sensitive personal information when entering recipe or ingredient information.

## Features Not Yet Implemented
- Custom recipe thumbnails

## Pydocs

<details>
<summary>dishdeck_dataclasses.py pydoc</summary>
Help on module dishdeck_dataclasses:

NAME
    dishdeck_dataclasses

CLASSES
    builtins.object
        Ingredient
        Recipe

    class Ingredient(builtins.object)
     |  Ingredient(name: 'str', quantity: 'int' = None, unit: 'str' = None) -> None
     |
     |  Ingredient(name: 'str', quantity: 'int' = None, unit: 'str' = None)
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __init__(self, name: 'str', quantity: 'int' = None, unit: 'str' = None) -> None
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __annotations__ = {'name': 'str', 'quantity': 'int', 'unit': 'str'}
     |
     |  __dataclass_fields__ = {'name': Field(name='name',type='str',default=<...
     |
     |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
     |
     |  __hash__ = None
     |
     |  __match_args__ = ('name', 'quantity', 'unit')
     |
     |  quantity = None
     |
     |  unit = None

    class Recipe(builtins.object)
     |  Recipe(name: 'str', tags: 'list[str]', source: 'str | None', description: 'str', ingredients: 'list[Ingredient]', instructions: 'list[str]') -> None
     |
     |  Recipe(name: 'str', tags: 'list[str]', source: 'str | None', description: 'str', ingredients: 'list[Ingredient]', instructions: 'list[str]')
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __init__(self, name: 'str', tags: 'list[str]', source: 'str | None', description: 'str', ingredients: 'list[Ingredient]', instructions: 'list[str]') -> None
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  delete(self, directory: 'str')
     |
     |  save(self, directory: 'str')
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __annotations__ = {'description': 'str', 'ingredients': 'list[Ingredie...
     |
     |  __dataclass_fields__ = {'description': Field(name='description',type='...
     |
     |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
     |
     |  __hash__ = None
     |

FUNCTIONS
    remove(path, *, dir_fd=None)
        Remove a file (same as unlink()).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

DATA
    annotations = _Feature((3, 7, 0, 'beta', 1), (3, 11, 0, 'alpha', 0), 1...

FILE
    c:\users\jarbe\documents\projects\sse657-dish-deck\src\dishdeck_dataclasses.py


PS C:\Users\jarbe\Documents\Projects\sse657-dish-deck> python -m pydoc .\src\dishdeck_dataclasses.py
Help on module dishdeck_dataclasses:

NAME
    dishdeck_dataclasses

CLASSES
    builtins.object
        Ingredient
        Recipe

    class Ingredient(builtins.object)
     |  Ingredient(name: 'str', quantity: 'int' = None, unit: 'str' = None) -> None
     |
     |  Ingredient(name: 'str', quantity: 'int' = None, unit: 'str' = None)
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __init__(self, name: 'str', quantity: 'int' = None, unit: 'str' = None) -> None
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __annotations__ = {'name': 'str', 'quantity': 'int', 'unit': 'str'}
     |
     |  __dataclass_fields__ = {'name': Field(name='name',type='str',default=<...
     |
     |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
     |
     |  __hash__ = None
     |
     |  __match_args__ = ('name', 'quantity', 'unit')
     |
     |  quantity = None
     |
     |  unit = None

    class Recipe(builtins.object)
     |  Recipe(name: 'str', tags: 'list[str]', source: 'str | None', description: 'str', ingredients: 'list[Ingredient]', instructions: 'list[str]') -> None
     |
     |  Recipe(name: 'str', tags: 'list[str]', source: 'str | None', description: 'str', ingredients: 'list[Ingredient]', instructions: 'list[str]')
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __init__(self, name: 'str', tags: 'list[str]', source: 'str | None', description: 'str', ingredients: 'list[Ingredient]', instructions: 'list[str]') -> None
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  delete(self, directory: 'str')
     |
     |  save(self, directory: 'str')
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __annotations__ = {'description': 'str', 'ingredients': 'list[Ingredie...
     |
     |  __dataclass_fields__ = {'description': Field(name='description',type='...
     |
     |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
     |
     |  __hash__ = None
     |
</details>

<details>
<summary>pantry.py pydoc</summary>
Help on module pantry:

NAME
    pantry

CLASSES
    builtins.object
        Pantry

    class Pantry(builtins.object)
     |  Methods defined here:
     |
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  add_ingredient(self, name: str, qty: float = None, unit: str = None)
     |
     |  edit_ingredient(self, name: str, field: Literal['name', 'qty', 'unit'], value: str | float)
     |
     |  get_all_ingredients(self) -> list[dishdeck_dataclasses.Ingredient]
     |      # Returns a list of Ingredient objects containing every ingredient in the pantry
     |      # Or an empty list if there are none
     |
     |  get_ingredient(self, name: str) -> list[dishdeck_dataclasses.Ingredient] | None
     |      # Returns the Ingredient object associated with the input name, if there is one
     |      # Otherwise returns None
     |
     |  load_ingredients(self, filepath: str)
     |
     |  remove_ingredient(self, name: str)
     |      # Removes the Ingredient object associated with the input name from the pantry, if there is one
     |
     |  save_ingredients(self, filepath: str)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    remove(path, *, dir_fd=None)
        Remove a file (same as unlink()).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

DATA
    Literal = typing.Literal
        Special typing form to define literal types (a.k.a. value types).

        This form can be used to indicate to type checkers that the corresponding
        variable or function parameter has a value equivalent to the provided
        literal (or one of several literals):

          def validate_simple(data: Any) -> Literal[True]:  # always returns True
              ...

FILE
    c:\users\jarbe\documents\projects\sse657-dish-deck\src\pantry.py
</details>

<details>
<summary>recipebook.py pydoc</summary>
Help on module recipebook:

NAME
    recipebook

CLASSES
    builtins.object
        RecipeBook

    class RecipeBook(builtins.object)
     |  Methods defined here:
     |
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  add_recipe(self, directory: str, name: str, tags: list[str], source: str | None, description: str, ingredients: list[dishdeck_dataclasses.Ingredient], instructions: list[str])
     |
     |  get_recipe(self, recipe_name)
     |      #Get recipe object
     |
     |  get_recipe_desc(self, recipe_name: str)
     |
     |  get_recipe_ingredients(self, recipe_name: str)
     |
     |  get_recipe_names(self, ingredients=None, strict=False)
     |      # TODO: Add filtering, i.e. make parameters ingredients and strict functional
     |      #               strict=True means ONLY the listed ingredients can be in returned recipes, no others
     |
     |  import_recipe(self, filepath: str)
     |
     |  search_recipes(self, search_terms: list[str]) -> list[dishdeck_dataclasses.Recipe]
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

DATA
    annotations = _Feature((3, 7, 0, 'beta', 1), (3, 11, 0, 'alpha', 0), 1...

FILE
    c:\users\jarbe\documents\projects\sse657-dish-deck\src\recipebook.py
</details>

<details>
<summary>uiux.py pydoc</summary>
Help on module uiux:

NAME
    uiux

FUNCTIONS
    create_recipe_preview(recipe_name: str)
        # Each recipe preview consists of a thumbnail, and as much of the
        # description as will fit in the remaining space in the element

    remove(path, *, dir_fd=None)
        Remove a file (same as unlink()).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

DATA
    GROCERY_FILE = 'data/grocerylist.docx'
    PANTRY_FILE = 'data/pantry.json'
    RECIPE_FOLDER = 'data/recipes/'
    THUMB_FOLDER = 'data/thumb/'
    annotations = _Feature((3, 7, 0, 'beta', 1), (3, 11, 0, 'alpha', 0), 1...
    data_pantry = []
    file_name = 'Test Recipe.md'
    file_names = ['Example Recipe.md', 'Experiment.md', 'fasfafsfaf.md', '...
    ingredient_list = <PySimpleGUI.PySimpleGUI.Listbox object>
    layout = [[<PySimpleGUI.PySimpleGUI.TabGroup object>]]
    c:\users\jarbe\documents\projects\sse657-dish-deck\src\uiux.py
</details>

<details>
<summary>test/test_dataclasses.py pydoc</summary>
Help on module test_dataclasses:

NAME
    test_dataclasses

FUNCTIONS
    ex_ing()

    ex_recipe()

    remove(path, *, dir_fd=None)
        Remove a file (same as unlink()).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
DATA
    annotations = _Feature((3, 7, 0, 'beta', 1), (3, 11, 0, 'alpha', 0), 1...

FILE
    c:\users\jarbe\documents\projects\sse657-dish-deck\src\test\test_dataclasses.py
</details>