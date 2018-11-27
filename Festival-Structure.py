import datetime

class Show(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self, artist, start, end):
        start_str = start
        start_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

        end_str = start
        end_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

        self.artist = artist
        self.start = start_time
        self.end = end_time
        
class Stage(object):
    def def __init__(self, name, shows):
        self.stage_name = name
        self.shows = shows

class Festival(object):
    def def __init__(self, name, stages, genres, city, start, end):
        
        start_str = start
        start_day = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')

        end_str = start
        end_day = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
        

        
        self.festival_name = name
        self.genres = genres
        self.locqtion = city
        self.stages = stages
        self.startday = start_day
        self.endday = end_day
        
