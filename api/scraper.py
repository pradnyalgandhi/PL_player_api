from bs4 import BeautifulSoup
import pprint
import requests

url = "https://www.premierleague.com/players/"

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
    
    def get_type(self):
        player_type = self.soup.find("td", class_="hide-s").get_text()
        return player_type

    def get_player_type(self):
        player_type = self.soup.find_all('div', class_="info")[1].get_text()
        return player_type

    def get_name(self):
        player_name = self.soup.find('div', class_="name t-colour").get_text()               
        return player_name

    def get_jersey_number(self):
        player_jersey_number = self.soup.find_all('div', class_="t-colour")        
        return player_jersey_number[0].get_text()

    def get_club(self):
        pass

    def get_nationality(self):
        player_nationality = self.soup.find('span', class_="playerCountry").get_text()
        return player_nationality

    def get_apperances(self):
        player_appearances = self.soup.find('span', class_="allStatContainer statappearances").get_text()
        return player_appearances

    def get_goals(self):
        player_goals = self.soup.find('span', class_="allStatContainer statgoals").get_text()
        return player_goals

    def get_wins(self):
        player_wins = self.soup.find('span', class_="allStatContainer statwins").get_text()
        return player_wins

    def get_losses(self):
        player_losses = self.soup.find('span', class_="allStatContainer statlosses").get_text()
        return player_losses

    def get_career_stats(self):

        season_stats = []
        season = self.soup.find_all('td', class_= "season")
        club = self.soup.find_all('span', class_= "long")
        apps = self.soup.find_all('td', class_= "appearances")
        goals = self.soup.find_all('td', class_= "goals")
        
        

        for i in range(0,len(season)):
            career = {}
            career["Season"] = season[i].get_text()
            career["Club"] = club[i].get_text()
            career["Apps"] = apps[i].get_text().replace(" ", "").replace("\n","")
            career["Goals"] = goals[i].get_text().replace(" ", "").replace("\n","")
            season_stats.append(career)
        return season_stats

    def create_instance(self):
        player = []
        for i in range(0, len(self.player_urls)):

            player_info = {}
            req = requests.get(self.player_urls[i])
            soup_overview = BeautifulSoup(req.content, 'html.parser')
            self.soup = soup_overview

            player_info['Name'] = self.get_name()
            player_info['Jersey No'] = self.get_jersey_number()
            player_info['Nationality'] = self.get_nationality()
            
            player_info['Career'] = self.get_career_stats()

            player.append(player_info)
        return player
        
# pp = pprint.PrettyPrinter()
# inst = PlayerStats(url)
# pp.pprint(inst.create_instance())


# url1 = "https://www.premierleague.com/players/13286/Tammy-Abraham/overview"
# inst = PlayerStats(url1)
# print(inst.get_jersey_number())
