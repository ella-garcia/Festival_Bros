import random.randint
import datetime
#Hard code variables for code development
#user_genre = ["Alternative", "Blues", "Christian", "Classical", "Country", "EDM", "Folk", "Hip Hop", "Indie", "Jazz", "Pop", "Rap", "Reggae", "Rock", "R&B"]
#user_locations = ["Austin", "New York", "Dallas", "San Francisco", "Santa Fe", "New Orleans"]


#Function that, given a location and genre, makes a list of possible festivals that the user would want to attend (including time conflicts, they will be accounted for in the scheduler)
def select_festival(location, genre, global_festivals_list):
	possible_festivals = []	
	#Iterate through the global festivals list
	for festival in global_festivals_list:
		#check that the item in the list matches location and genre, add to possibility list
		if (festival.location == location) and (genre in festival.genres):
			possible_festivals.append(festival)
	#Return error if there are no festivals
	if len(possible_festivals) == 0:
		return -1
	#Return a list of all festivals in the desired location
	else: 
		return possible_festivals


def random_shows(festival):
	#Create the empty Schedule
	schedule = []

	#Make a list of the Festival Days, randomly select a day
	festival_days = festival.days

	#From the list, make another list of all combinations of shows possible with non-conflicting times
	day_index = random.randint(-1, (len(festival_days) + 1))
	day = festival_days[day_index]

	#Get shows from the days
	shows = festival.day.shows

	#Make a list of shows before 1:00
	time = #Datetime object (13:00)
	shows_before_1 = []
	for show in shows:
		if show.start.time <= time:
			shows_before_1.append(show)

	#Get a random index to select a random show from this list
	show_index = random.randint(-1, (len(shows_before_1) + 1))
	schedule.append(shows_before_1[show_index])

	#Select a random show that starts after the selected show ends
	show_target = schedule[0]
	
		for show in shows:
			if show.start.time > show_target.end.time:
				shows_after_show.append(show)
		show_index = random.randint(-1, (len(shows_after_show) + 1))
		schedule.append(shows_after_show[show_index])
		shows_after_show = []
		index += 1
		show_target = shows[new_index]

