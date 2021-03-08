from bs4 import BeautifulSoup
import requests

url = "https://www.premierleague.com/players/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
tags = soup.find_all("a",class_='playerName')
overview = []
for tag in tags:
    player_url = "https://www.premierleague.com"+ tag.get('href')
    overview.append(player_url)

player = overview[0]

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

        req = requests.get(url)
        soup = BeautifulSoup(req.content,'html.parser')
        tags = soup.find_all('a', class_='playerName')

        self.player_urls = []
        for url in tags:
            self.player_urls.append(url)
        
    def get_player_type(self):
        for url in self.player_urls:
            soup = BeautifulSoup(url, 'html.parser')
            player_type = soup.find_all('div', class_="info")[1].get_text()
            return player_type


    def get_name(self):
        for url in self.player_urls:
            soup = BeautifulSoup(url, 'html.parser')
            player_name = soup.find('div', class_="name t-colour").get_text()
            return player_name

    def get_jersery_number(self):
        for url in self.player_urls:
            soup = BeautifulSoup(url, 'html.parser')
            player_jersey_number = soup.find('div', class_="number t-colour").get_text()
            return player_jersey_number

    def get_club(self):
        pass

    def get_nationality(self):
        for url in self.player_urls:
            soup = BeautifulSoup(url, 'html.parser')
            player_nationality = soup.find('span', class_="playerCountry").get_text()
            return player_nationality

    def get_apperances(self):
        pass 

    def get_goals(self):
        pass

    def get_wins(self):
        pass

    def get_losses(self):
        pass





def player_overview(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content,'html.parser')

    #Name & Jersey
    name = soup.find(class_='name t-colour').get_text()
    print(name)
    jersey_number = soup.find(class_='number t-colour').get_text()
    print(jersey_number)

    #Nationality
    nationality = soup.find(class_='playerCountry').get_text()
    print(nationality)

    #Age
    age = soup.find(class_='info--light').get_text()
    print(age)


# player_overview(overview[0])

types = soup.find('td', class_='hide-s')
print(types)






# #Stats url
# new_url = player.split("/")[:-1]
# print(f"{'/'.join(new_url)}/stats")

