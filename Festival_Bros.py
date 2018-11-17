# DECLARE VARIABLES & LISTS
listGenres = ["Alternative, Blues, Christian, Classical, Country, EDM, Folk, Hip Hop, Indie, Jazz, Pop, Rap, Reggae, Rock, R&B"]

# FUNCTION TO DISPLAY MENU & SELECTION
def menu_selection():
	print("Menu:")
	print("1. View All Festivals Around Me")
	print("2. Festivals According to Genre")
	print("3. Festival Randomizer")
	print("Please enter 1-3 for your choice or 4 to exit.")
	numSelect = int("")

	return int

# FUNCTION TO DISPLAY GENRES & SELECTION
def genre_selection(listGenres):
	print("Genres listed below:")
	for genre in listGenres:
		print(genre)
	strSelect = str("Please select the genre you are interested in:")

# FUNCTION THAT PARSES LIST TO SELECT SHOWS
def show_selection(dictShows):
	print
# MAIN
def main():
	genre_selection(listGenres)
main()