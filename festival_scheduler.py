#Hard code variables for code development
user_genre = ["Alternative", "Blues", "Christian", "Classical", "Country", "EDM", "Folk", "Hip Hop", "Indie", "Jazz", "Pop", "Rap", "Reggae", "Rock", "R&B"]
user_locations = ["Austin", "New York", "Dallas", "San Francisco", "Santa Fe", "New Orleans"]
user_times = [1, 13.5, 14, 22, 19.25, 20.5, 13.5, 27, 0, 24, -1.5, 22] #has 27, 0, 24, -1 to test that the times are greater than or equal to 0 and less than 24, and has duplicates to test conflicting times


#Fetches the genre from the user
def get_location(user_location):
	return user_location

#Fetches the genre from the user
def get_genre(user_genre):
	return user_genre

#Function that, given a location and genre, makes a list of possible festivals that the user would want to attend (including time conflicts, they will be accounted for in the scheduler)
def select_festival(location, genre):
	possible_festivals = []	
	for festival in list_of_festivals:
		if (festival.location == location) and (genre in festival.genres):
			possible_festivals.append(festival)

	return possible_festivals


#can be commented out when the time comes to use it with GUI
def main():

location = get_location(user_locations[0])
genre = get_genre(user_genre[0])

possible_festivals = choose_festival(location, genre)

schedule = schedule_no_conflicts(possible_festivals)

main()