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
	recipe_book.add_recipe(RECIPE_FOLDER + file_name)

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
ingredient_list = sg.Listbox([], size=(50, 40), pad=((0, 0), (20, 0)), no_scrollbar=True, key="_INGREDIENTS_")

# Layout for the meals tab
layout_meals = [[
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
	[sg.Text("Pantry tab in progress...")]
]

tab_meals = sg.Tab(
	"Meals", 
	layout_meals,
	)

tab_pantry = sg.Tab(
	"Pantry",
	layout_pantry,
	)

# Complete layout for the window
layout = [[sg.TabGroup([
	[tab_meals,
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
	print(f"Event: {event}\nValues: {values}")

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

	# End program if user closes window
	if event == sg.WIN_CLOSED:
		break

window.close()