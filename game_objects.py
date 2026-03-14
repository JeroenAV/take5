class Card:
    max_cards = 104
    
    def __init__(self, number, points):
        self.number = number
        self.points = points
        
    def get_number(self):
        return self.number
    
    def get_points(self):
        return self.points
    
    
class Player:
    number_of_playing_cards = 10
    min_players = 2
    max_players = 10
    
    
    def __init__(self, name ,points):
        self.name = name
        self.points= points
        
        
    def get_points(self):
        return self.points
    
class playField:
    rows = 4






