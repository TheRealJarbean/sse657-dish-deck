"""
"""

# External modules
import PySimpleGUI as sg
import os
# Local modules
from recipebook import RecipeBook

sg.theme('dark')

RECIPE_FOLDER = "data/recipes/"
THUMB_FOLDER = "data/thumb/"

## Set the cwd to the folder above src
script_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.dirname(script_directory)
os.chdir(src_directory)

# Create master RecipeBook object
recipe_book = RecipeBook()

# Load all recipes saved in local recipes folder
file_names = os.listdir(RECIPE_FOLDER)
for file_name in file_names:#
	#TODO: Make sure there are no duplicate recipes
	recipe_book.import_recipe(RECIPE_FOLDER + file_name)

# Each recipe preview consists of a thumbnail, and as much of the
# description as will fit in the remaining space in the element
def create_recipe_preview(recipe_name: str):
	# TODO: maybe check to make sure the recipe exists in the book
	checkbox_row = sg.Checkbox(
		recipe_name.title(), 
		font=["consolas", 15, "bold"], 
		pad=(0, 10),
		enable_events=True,
		key=recipe_name + "check"
		)

	# Default to missing image thumbnail
	# If a thumbnail is found for the recipe, use that instead
	thumb_name = "Missing Image.png"
	file_names = os.listdir(THUMB_FOLDER)
	for file_name in file_names:
		base_name, ext = os.path.splitext(file_name)
		if base_name == recipe_name:
			thumb_name = file_name
			break

	# Add folder path for full path to thumbnail
	thumb_path = THUMB_FOLDER + thumb_name
	description_thumbnail = sg.Image(filename=(thumb_path))
	description_text = sg.Text(recipe_book.get_recipe_desc(recipe_name), size=(50, 9), justification="left")
	# Each call creates a new object, avoids duplicate element restriction in PySimpleGUI
	separator = lambda: sg.HorizontalSeparator(color="#FFFFFF", pad=(0, 10)) 
	return sg.pin(sg.Column(
		[[separator()], [checkbox_row], [description_thumbnail, description_text], [separator()]],
		vertical_alignment="top",
		expand_x=True,
		key=recipe_name
		))

# Individual elements of the UI
search_bar = sg.Input(do_not_clear=True, size=(100, 1), pad=((0, 0), (20, 0)), enable_events=True, key="_SEARCH_")
ingredient_list = sg.Listbox([], size=(500, 500), pad=((0, 0), (20, 0)), select_mode="multiple", font=["consolas", 10], no_scrollbar=True, key="_INGREDIENTS_")

# Layout for the recipebook tab
layout_recipebook = [[
	sg.Column(
		[[search_bar], [
			sg.Column(
				[[create_recipe_preview(recipe_name)] for recipe_name in recipe_book.get_recipe_names()],
				scrollable=True,
				vertical_scroll_only=True,
				pad=((0, 10), (10, 0)),
				vertical_alignment="top",
				element_justification="left",
				size=(None, 600),
				expand_x=True,
				key="_RECIPELIST_"
			)
		]],
		pad=((0, 10), (0, 0)),
		vertical_alignment="top",
		size=(700, None),
		expand_y=True
	),
	sg.Column(
		[[ingredient_list]],
		pad=((0, 0), (0, 0)),
	)
]]

# Layout for the pantry tab
layout_pantry = [
	sg.Input(do_not_clear=True, size=(100, 1), pad=((0, 0), (20, 0)), enable_events=True, key="_PANTRYADD_")
]

tab_recipebook = sg.Tab(
	"Recipe Book", 
	layout_recipebook,
	)

tab_pantry = sg.Tab(
	"Pantry",
	layout_pantry,
	)

# Complete layout for the window
layout = [[sg.TabGroup([
	[tab_recipebook,
	tab_pantry]],
	font=["consolas", 20, "bold"],
	border_width=0,
	tab_border_width=2,
	expand_x=True,
	expand_y=True)]
]

# Create the Window
window = sg.Window(
	"Demo",
	layout,
	size=(1000, 700), 
)

# Event loop
while True:
	event, values = window.read()

	if values['_SEARCH_'] != '':
		search = values['_SEARCH_'].lower()
		matches = [name for name in recipe_book.get_recipe_names() if search in name]
		misses = [name for name in recipe_book.get_recipe_names() if name not in matches]
		for key in matches:
			window[key].Update(visible=True)
		for key in misses:
			window[key].Update(visible=False)
	else:
		for key in recipe_book.get_recipe_names():
			window[key].Update(visible=True)

	# Update ingredients list based on selected recipes
	ingredients = []
	for name in recipe_book.get_recipe_names():
		if values[name + "check"]:
			# TODO: Combine similar ingredients and update quantities
			# TODO: Make [ ] into [x] if ingredient in pantry
			# TODO: Somehow indicate if pantry has partial amount of ingredient
			max_len = 36
			ingredients += [f"[ ] {x[0]} | {x[1]}" for x in recipe_book.get_recipe_ingredients(name)]
	
	if ingredients != []:
		max_len = 36 # Max length allowed in listbox boundary
		ing = lambda s: s[:s.find('|')] # Returns ingredient name part of string
		qty = lambda s: s[s.find('|'):] # Returns ingredient quantity part of string
		# Pad quantity parts of ingredient strings to equal length
		ingredients = [ing(s) + qty(s).ljust(max(len(qty(s)) for s in ingredients)) for s in ingredients]
		# Trim any long ingredient strings to listbox width
		ingredients = [ing(s)[:(max_len - len(qty(s)) - 4)] + "... " + qty(s) if len(s) > max_len else s for s in ingredients]
		# Extend rest of ingredient strings to fill listbox width
		ingredients = [ing(s) + (" " * (max_len - len(s))) + qty(s) for s in ingredients]

	window["_INGREDIENTS_"].Update(ingredients)

	# End program if user closes window
	if event == sg.WIN_CLOSED:
		break

window.close()