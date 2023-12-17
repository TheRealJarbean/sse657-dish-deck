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
