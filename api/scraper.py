from bs4 import BeautifulSoup
import requests



class PlayerStats:

    '''
    A class that scrapes player data from premierleague.com/players/ and returns player data.

    -----
    Methods
    -----

    get_type: Returns the type of the Player (Fwd/Mid/Def/GK)

    get_name: Returns name of the player

    get_jersey_number: Returns the jersey number of the player

    get_club: Returns the club of the player

    get_nationality: Returns the name of the country

    get_career: Returns a dictionary of data of the players career stats per season

                season: Returns the season timeline
                club: Returns the club player eas playing for that partiular season
                apps: Appearences for that season
                Goals: Goals scored for that particular season

    get_apperances: Returns the total number of appearances

    get_goals: Returns goals scored by the player

    get_wins: Returns total wins

    get_losses: Returns total losses



    '''
    
    def __init__(self,url):

        self.url = url
        self.player_names = []
        self.player_urls = []
        self.player_stats_urls = []

        req = requests.get(url)
        self.soup = BeautifulSoup(req.content,'html.parser')
        tags = self.soup.find_all('a', class_='playerName')

        for url in tags:            
            player_url = "https://www.premierleague.com"+ url.get('href')
            self.player_urls.append(player_url)

            temp = player_url.split("/")[:-1]
            stats_url = f"{'/'.join(temp)}/stats"
            self.player_stats_urls.append(stats_url)        
    
    
    def get_player_type(self):
        player_type = self.soup.find_all('div', class_="info")[1].get_text()
        return player_type


    def get_name(self):
        player_name = self.soup.find('div', class_="name t-colour").get_text()
        self.player_names.append(player_name)        
        return self.player_names

    def get_jersery_number(self):
        player_jersey_number = self.soup.find('div', class_="number t-colour").get_text()
        return player_jersey_number

    def get_club(self):
        pass

    def get_nationality(self):
        player_nationality = self.soup.find('span', class_="playerCountry").get_text()
        return player_nationality

    def get_apperances(self):
        player_appearances = self.soup.find('span', class_="allStatContainer statappearances").get_text()
        return player_appearances

    def get_goals(self):
        pass

    def get_wins(self):
        pass

    def get_losses(self):
        pass


    # def create_instance(self):
    #     names = []
    #     for url in self.player_urls:
    #         req = requests.get(url)
    #         self.soup = BeautifulSoup(req.content, 'html.parser')
    #         name = self.get_name()
    #         names.append(name)
    #     return names

       
            
