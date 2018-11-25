#Hard code variables for code development
user_genre = ["Alternative", "Blues", "Christian", "Classical", "Country", "EDM", "Folk", "Hip Hop", "Indie", "Jazz", "Pop", "Rap", "Reggae", "Rock", "R&B"]
user_locations = ["Austin", "New York", "Dallas", "San Francisco", "Santa Fe", "New Orleans", "New York"]
user_times = [1, 13.5, 14, 22, 19.25, 20.5, 13.5, 27, 0, 24, -1.5, 22] #has 27, 0, 24, -1 to test that the times are greater than or equal to 0 and less than 24, and has duplicates to test conflicting times


#Function to select the location that the user wants and output the festivals in that location
def select_location(user_location):



#Function to select the genre the user wants and output the festivals with that genre in the previously selected city 
def select_genre(user_genre):



#Function to schedule festivals for the user with no conflicts-- outputs error if there are conflicting festivals and presents the user an option to select one of the conflicting festivals only
def schedule_no_conflicts(user_times):

def main():

main()