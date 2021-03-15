from bs4 import BeautifulSoup
import pprint, re
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
        self.player_position = []

        req = requests.get(url)
        self.soup = BeautifulSoup(req.content,'html.parser')

        #Extracting player URLs
        tags = self.soup.find_all('a', class_='playerName')

        for url in tags:            

            player_url = "https://www.premierleague.com"+ url.get('href')
            self.player_urls.append(player_url)            

            temp = player_url.split("/")[:-1]
            stats_url = f"{'/'.join(temp)}/stats"
            self.player_stats_urls.append(stats_url)

        #Extracting player Position      
        position = self.soup.find_all('td', class_='hide-s')
        for pos in position:            
            temp = re.search(r'(\"\>)(\w*)(\<\/td)', str(pos))
            if temp:         
                posi = temp.group(2)
                self.player_position.append(posi)            
 
    def get_type(self):
        player_type = self.soup.find("td", class_="hide-s").get_text()
        return player_type

    def get_name(self):
        player_name = self.soup.find('div', class_="name t-colour").get_text()               
        return player_name

    def get_jersey_number(self):
        player_jersey_number = self.soup.find('div', class_="number t-colour")
        if player_jersey_number:
            return player_jersey_number.get_text()
        else:
            return "Not assigned"

    def get_club(self):
        
        player_club = self.soup.find('div', class_="info")        
        if player_club:
            player_club = player_club.get_text().replace(" ","").replace("\n","")
            if (player_club == 'Forward' or player_club == "Midfielder" or player_club == "Defender" or player_club == "Goalkeeper"):
                return "Not Available"
            else:
                return player_club
        else:
            "Not Available"

    def get_nationality(self):
        player_nationality = self.soup.find_all('span', class_="playerCountry")
        if player_nationality:
            return player_nationality[0].get_text()
        else:
            return "Not Available"
    
    def get_apperances(self):
        player_appearances = self.soup.find('span', class_="allStatContainer statappearances").get_text().replace(" ","").replace("\n","")
        return player_appearances

    def get_goals(self):
        player_goals = self.soup.find('span', class_="allStatContainer statgoals").get_text()
        return player_goals

    def get_clean_sheets(self):
        player_clean_sheets = self.soup.find('span', class_="allStatContainer statclean_sheet").get_text()
        return player_clean_sheets

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
            player_info['Current Club'] = self.get_club()      
            player_info['Nationality'] = self.get_nationality()
            player_info['Position'] = self.player_position[i]
            player_info['Jersey No'] = self.get_jersey_number()            
            player_info['Career'] = self.get_career_stats()

            req = requests.get(self.player_stats_urls[i])
            soup_stats = BeautifulSoup(req.content, 'html.parser')
            self.soup = soup_stats

            player_info['Appearances'] = self.get_apperances()
            if self.player_position[i] == 'Goalkeeper':
                player_info['Clean Sheets'] = self.get_clean_sheets().replace(" ", "").replace("\n","")
            else:
                player_info['Goals'] = self.get_goals().replace(" ", "").replace("\n","")
            player_info['Total Wins'] = self.get_wins().replace(" ", "").replace("\n","")
            player_info['Total Losses'] = self.get_losses().replace(" ", "").replace("\n","")

            player.append(player_info)
        return player
        
pp = pprint.PrettyPrinter()
inst = PlayerStats(url)
pp.pprint(inst.create_instance())


# url1 = "https://www.premierleague.com/players/"
# inst = PlayerStats(url1)
# print(len(inst.player_position))

