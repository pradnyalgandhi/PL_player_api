from bs4 import BeautifulSoup
import pprint, re, time
import requests, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.premierleague.com/players/"
file_path = "F:/Python/Django/PL Player API/pl_players_api/api/cd/chromedriver.exe"
option = Options()
option.headless = True
driver = webdriver.Chrome(executable_path= file_path, options= option)


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
        driver.get("https://www.premierleague.com/players/")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)
        req = driver.page_source

        # req = requests.get(url)
        self.soup = BeautifulSoup(req, features='html.parser')

        #Extracting player URLs
        tags = self.soup.find_all('a', class_='playerName')

        for url in tags:            

            player_url = "https:" + url.get('href')
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

        driver.quit()        
 

    def get_name(self):
        '''
            Returns the name of the player
        '''
        player_name = self.soup.find('div', class_="name t-colour").get_text()
        return player_name

    def get_jersey_number(self):
        '''
            Returns the Jersey Number of the player
        '''
        player_jersey_number = self.soup.find('div', class_="number t-colour")
        if player_jersey_number:
            return player_jersey_number.get_text()
        else:
            return "Not assigned"

    def get_club(self):
        '''
            Returns the current club of the Player
        '''        
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
        '''
            Returns the Nationality of the Player
            Note : Nationality of someplayers have not been updated on the website.
        '''
        player_nationality = self.soup.find_all('span', class_="playerCountry")
        if player_nationality:
            return player_nationality[0].get_text()
        else:
            return "Not Available"
    
    def get_apperances(self):
        '''
            Returns the Total No. of Apps of the player
        '''
        player_appearances = self.soup.find('span', class_="allStatContainer statappearances")
        if player_appearances:
            return player_appearances.get_text().replace(" ","").replace("\n","")
        else:
            return "Not Available"

    def get_goals(self):
        '''
            Returns the Total No. of Goals scored by the player
            Note: Applicable for Fwd,Mid,Def
        '''
        player_goals = self.soup.find('span', class_="allStatContainer statgoals").get_text()
        return player_goals

    def get_clean_sheets(self):
        '''
            Returns the Total Number of Cleansheets by a Goalkeeper
            Note: Applicable for only Goalkeepers
        '''
        player_clean_sheets = self.soup.find('span', class_="allStatContainer statclean_sheet").get_text()
        return player_clean_sheets

    def get_wins(self):
        '''
            Returns Total No. of wins of the Player
        '''
        player_wins = self.soup.find('span', class_="allStatContainer statwins").get_text()
        return player_wins

    def get_losses(self):
        '''
            Returns Total No. of losses of the Player
        '''
        player_losses = self.soup.find('span', class_="allStatContainer statlosses").get_text()
        return player_losses

    def get_career_stats(self):
        '''
            Returns a library of Player Stats by every season
            Season--Club--Apps(Sub Apps)--Goals Scored
        '''

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

    def get_forward_stats(self):
        '''
            Returns a library of Stats for a Forward            
        '''
        stats = []
        attacking_stats = {}
        attacking_stats["Goals"] = self.soup.find('span', class_="allStatContainer statgoals").get_text()
        attacking_stats["Headers"] = self.soup.find('span',class_="allStatContainer statatt_hd_goal").get_text()
        attacking_stats["Right Foot Goals"] = self.soup.find('span',class_="allStatContainer statatt_rf_goal").get_text()
        attacking_stats["Left Foot Goals"] = self.soup.find('span',class_="allStatContainer statatt_lf_goal").get_text()
        attacking_stats["Penalties"] = self.soup.find('span',class_="allStatContainer statatt_pen_goal").get_text()
        attacking_stats["Freekicks"] = self.soup.find('span',class_="allStatContainer statatt_freekick_goal").get_text()
        attacking_stats["Shots"] = self.soup.find('span',class_="allStatContainer stattotal_scoring_att").get_text()
        attacking_stats["Shots on target"] = self.soup.find('span',class_="allStatContainer statontarget_scoring_att").get_text()
        attacking_stats["Accuracy %"] = self.soup.find('span',class_="allStatContainer statshot_accuracy").get_text()
        attacking_stats["Hit Woodwork"] = self.soup.find('span',class_="allStatContainer stathit_woodwork").get_text()

        for k,v in attacking_stats.items():
            attacking_stats.update({k:v.replace(" ","").replace("\n","")})
        
        stats.append(attacking_stats)

        team_play_stats = {}
        team_play_stats["Assists"] = self.soup.find('span', class_="allStatContainer statgoal_assist").get_text()
        team_play_stats["Total Passes"] = self.soup.find('span', class_="allStatContainer stattotal_pass").get_text()
        team_play_stats["Passes per match"] = self.soup.find('span', class_="allStatContainer stattotal_pass_per_game").get_text()
        team_play_stats["Big Chances Created"] = self.soup.find('span', class_="allStatContainer statbig_chance_created").get_text()
        team_play_stats["Crosses"] = self.soup.find('span', class_="allStatContainer stattotal_cross").get_text()
        for k,v in team_play_stats.items():
            team_play_stats.update({k:v.replace(" ","").replace("\n","")})

        stats.append(team_play_stats)

        defense_stats = {}
        defense_stats["Tackles"] = self.soup.find('span', class_="allStatContainer stattotal_tackle").get_text()
        defense_stats["Blocked Shots"] = self.soup.find('span', class_="allStatContainer statblocked_scoring_att").get_text()
        defense_stats["Interceptions"] = self.soup.find('span', class_="allStatContainer statinterception").get_text()
        defense_stats["Clearances"] = self.soup.find('span', class_="allStatContainer stattotal_clearance").get_text()
        defense_stats["Headed Clearance"] = self.soup.find('span', class_="allStatContainer stateffective_head_clearance").get_text()
        for k,v in defense_stats.items():
            defense_stats.update({k:v.replace(" ","").replace("\n","")})

        stats.append(defense_stats)

        return stats
    
    def get_midfielder_stats(self):
        '''
            Returns a library of Stats for a Midfielder           
        '''
        
        defensive_stats = {}
        defensive_stats["Tackles"] = self.soup.find('span',class_="allStatContainer stattotal_tackle").get_text()
        defensive_stats["Tackle success %"] = self.soup.find('span',class_="allStatContainer stattackle_success").get_text()
        defensive_stats["Blocked Shots"] = self.soup.find('span',class_="allStatContainer statblocked_scoring_att").get_text()
        defensive_stats["Interceptions"] = self.soup.find('span',class_="allStatContainer statinterception").get_text()
        defensive_stats["Clearances"] = self.soup.find('span',class_="allStatContainer stattotal_clearance").get_text()
        defensive_stats["Recoveries"] = self.soup.find('span',class_="allStatContainer statball_recovery").get_text()
        defensive_stats["Duels Wons"] = self.soup.find('span',class_="allStatContainer statduel_won").get_text()
        defensive_stats["Duels Lost"] = self.soup.find('span',class_="allStatContainer statduel_lost").get_text()
        defensive_stats["Successful 50/50s"] = self.soup.find('span',class_="allStatContainer statwon_contest").get_text()
        defensive_stats["Aerial battles won"] = self.soup.find('span',class_="allStatContainer stataerial_won").get_text()
        defensive_stats["Aerial battles lost"] = self.soup.find('span',class_="allStatContainer stataerial_lost").get_text()

        for k,v in defensive_stats.items():
            defensive_stats.update({k:v.replace(" ","").replace("\n","")})

        return defensive_stats
    
    def get_defender_stats(self):
        '''
            Returns a library of Stats for a Defender          
        '''
        stats = []

        attacking_stats = {}
        attacking_stats["Goals"] = self.soup.find('span', class_="allStatContainer statgoals").get_text()
        attacking_stats["Headers"] = self.soup.find('span', class_="allStatContainer statatt_hd_goal").get_text()
        attacking_stats["Right Foot Goals"] = self.soup.find('span', class_="allStatContainer statatt_rf_goal").get_text()
        attacking_stats["Left Foot Goals"] = self.soup.find('span', class_="allStatContainer statatt_lf_goal").get_text()
        attacking_stats["Hit Woodwork"] = self.soup.find('span', class_="allStatContainer stathit_woodwork").get_text()
        for k,v in attacking_stats.items():
            attacking_stats.update({k:v.replace(" ","").replace("\n","")})

        stats.append(attacking_stats)

        team_play_stats = {}
        team_play_stats["Assists"] = self.soup.find('span', class_="allStatContainer statgoal_assist").get_text()
        team_play_stats["Total Passes"] = self.soup.find('span', class_="allStatContainer stattotal_pass").get_text()
        team_play_stats["Passes per match"] = self.soup.find('span', class_="allStatContainer stattotal_pass_per_game").get_text()
        team_play_stats["Big Chances Created"] = self.soup.find('span', class_="allStatContainer statbig_chance_created").get_text()
        team_play_stats["Crosses"] = self.soup.find('span', class_="allStatContainer stattotal_cross").get_text()
        team_play_stats["Cross Accuracy"] = self.soup.find('span', class_="allStatContainer statcross_accuracy").get_text()
        team_play_stats["Through Balls"] = self.soup.find('span', class_="allStatContainer stattotal_through_ball").get_text()
        team_play_stats["Long Balls"] = self.soup.find('span', class_="allStatContainer stataccurate_long_balls").get_text()
        for k,v in team_play_stats.items():
            team_play_stats.update({k:v.replace(" ","").replace("\n","")})

        stats.append(team_play_stats)

        defensive_stats = {}
        defensive_stats["Clean Sheets"] = self.soup.find('span', class_="allStatContainer statclean_sheet").get_text()
        defensive_stats["Goals conceded"] = self.soup.find('span',class_="allStatContainer statgoals_conceded").get_text()
        defensive_stats["Tackles"] = self.soup.find('span',class_="allStatContainer stattotal_tackle").get_text()
        defensive_stats["Tackle success %"] = self.soup.find('span',class_="allStatContainer stattackle_success").get_text()
        defensive_stats["Blocked Shots"] = self.soup.find('span',class_="allStatContainer statblocked_scoring_att").get_text()
        defensive_stats["Interceptions"] = self.soup.find('span',class_="allStatContainer statinterception").get_text()
        defensive_stats["Clearances"] = self.soup.find('span',class_="allStatContainer stattotal_clearance").get_text()
        defensive_stats["Recoveries"] = self.soup.find('span',class_="allStatContainer statball_recovery").get_text()
        defensive_stats["Duels Wons"] = self.soup.find('span',class_="allStatContainer statduel_won").get_text()
        defensive_stats["Duels Lost"] = self.soup.find('span',class_="allStatContainer statduel_lost").get_text()
        defensive_stats["Successful 50/50s"] = self.soup.find('span',class_="allStatContainer statwon_contest").get_text()
        defensive_stats["Aerial battles won"] = self.soup.find('span',class_="allStatContainer stataerial_won").get_text()
        defensive_stats["Aerial battles lost"] = self.soup.find('span',class_="allStatContainer stataerial_lost").get_text()
        defensive_stats["Own Goals"] = self.soup.find('span',class_="allStatContainer statown_goals").get_text()

        for k,v in defensive_stats.items():
            defensive_stats.update({k:v.replace(" ","").replace("\n","")})
        
        stats.append(defensive_stats)     

        return stats

    def get_goalkeeper_stats(self):
        '''
            Returns a library of Stats for a Goalkeeper        
        '''
        stats = []

        goalkeeping_stats = {}
        goalkeeping_stats["Saves"] = self.soup.find('span', class_="allStatContainer statsaves").get_text()
        goalkeeping_stats["Penalties Saved"] = self.soup.find('span', class_="allStatContainer statpenalty_save").get_text()
        goalkeeping_stats["Punches"] = self.soup.find('span', class_="allStatContainer statpunches").get_text()
        goalkeeping_stats["High Claims"] = self.soup.find('span', class_="allStatContainer statgood_high_claim").get_text()
        goalkeeping_stats["Catches"] = self.soup.find('span', class_="allStatContainer statcatches").get_text()
        goalkeeping_stats["Sweeper Clearances"] = self.soup.find('span', class_="allStatContainer stattotal_keeper_sweeper").get_text()
        goalkeeping_stats["Throw outs"] = self.soup.find('span', class_="allStatContainer statkeeper_throws").get_text()
        goalkeeping_stats["Goal Kicks"] = self.soup.find('span', class_="allStatContainer statgoal_kicks").get_text()
        for k,v in goalkeeping_stats.items():
            goalkeeping_stats.update({k:v.replace(" ","").replace("\n","")})
        
        stats.append(goalkeeping_stats)

        defensive_stats = {}
        defensive_stats["Clean Sheets"] = self.soup.find('span', class_="allStatContainer statclean_sheet").get_text()
        defensive_stats["Goals conceded"] = self.soup.find('span', class_="allStatContainer statgoals_conceded").get_text()
        defensive_stats["Errors"] = self.soup.find('span', class_="allStatContainer staterror_lead_to_goal").get_text()
        defensive_stats["Own Goals"] = self.soup.find('span', class_="allStatContainer statown_goals").get_text()
        
        for k,v in defensive_stats.items():
            defensive_stats.update({k:v.replace(" ","").replace("\n","")})
        
        stats.append(defensive_stats)

        discipline_stats = {}
        discipline_stats["Yellow Card"] = self.soup.find('span', class_="allStatContainer statyellow_card").get_text()
        discipline_stats["Red Card"] = self.soup.find('span', class_="allStatContainer statred_card").get_text()
        discipline_stats["Fouls"] = self.soup.find('span', class_="allStatContainer statfouls").get_text()

        for k,v in discipline_stats.items():
            discipline_stats.update({k:v.replace(" ","").replace("\n","")})
        
        stats.append(discipline_stats)

        team_play_stats = {}
        team_play_stats["Goals"] = self.soup.find('span', class_="allStatContainer statgoals").get_text()
        team_play_stats["Assists"] = self.soup.find('span', class_="allStatContainer statgoal_assist").get_text()
        team_play_stats["Passes"] = self.soup.find('span', class_="allStatContainer stattotal_pass").get_text()
        team_play_stats["Passes per match"] = self.soup.find('span', class_="allStatContainer stattotal_pass_per_game").get_text()
        team_play_stats["Accurate long balls"] = self.soup.find('span', class_="allStatContainer stataccurate_long_balls").get_text()

        for k,v in team_play_stats.items():
            team_play_stats.update({k:v.replace(" ","").replace("\n","")})
        
        stats.append(team_play_stats)

        return stats

    def get_team_play_stats(self):
        '''
            Returns team playing stats of a player            
        '''

        team_play_stats = {}
        team_play_stats["Assists"] = self.soup.find('span', class_="allStatContainer statgoal_assist").get_text()
        team_play_stats["Total Passes"] = self.soup.find('span', class_="allStatContainer stattotal_pass").get_text()
        team_play_stats["Passes per match"] = self.soup.find('span', class_="allStatContainer stattotal_pass_per_game").get_text()
        team_play_stats["Big Chances Created"] = self.soup.find('span', class_="allStatContainer statbig_chance_created").get_text()
        team_play_stats["Crosses"] = self.soup.find('span', class_="allStatContainer stattotal_cross").get_text()
        team_play_stats["Cross Accuracy"] = self.soup.find('span', class_="allStatContainer statcross_accuracy").get_text()
        team_play_stats["Through Balls"] = self.soup.find('span', class_="allStatContainer stattotal_through_ball").get_text()
        team_play_stats["Long Balls"] = self.soup.find('span', class_="allStatContainer stataccurate_long_balls").get_text()
        for k,v in team_play_stats.items():
            team_play_stats.update({k:v.replace(" ","").replace("\n","")})
        
        return team_play_stats


    def get_discipline_stats(self):
        '''
            Returns disciplinary stats of a player           
        '''

        discipline_stats = {}
        discipline_stats["Yellow Card"] = self.soup.find('span', class_="allStatContainer statyellow_card").get_text()
        discipline_stats["Red Card"] = self.soup.find('span', class_="allStatContainer statred_card").get_text()
        discipline_stats["Fouls"] = self.soup.find('span', class_="allStatContainer statfouls").get_text()
        discipline_stats["Offsides"] = self.soup.find('span', class_="allStatContainer stattotal_offside").get_text()
        for k,v in discipline_stats.items():
            discipline_stats.update({k:v.replace(" ","").replace("\n","")})

        return discipline_stats

    def get_data(self):
        '''
            A method to call all the functions and return unified data for all the players.
        '''
        player = []
        # Change loop 
        for i in range(150, 160):

            player_info = {}
            req = requests.get(self.player_urls[i])
            soup_overview = BeautifulSoup(req.content, 'html.parser')
            self.soup = soup_overview

            player_info['Name'] = self.get_name()
            print(player_info['Name'])
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

            if self.player_position[i] == 'Forward':
                player_info["Attacking Stats"] = self.get_forward_stats()[0]
                player_info["Team Play Stats"] = self.get_forward_stats()[1]
                player_info["Disciplinary Stats"] = self.get_discipline_stats()
                player_info["Defensive Stats"] = self.get_forward_stats()[2]

            elif self.player_position[i] == "Defender":
                player_info["Attacking Stats"] = self.get_defender_stats()[0]
                player_info["Team Play Stats"] = self.get_team_play_stats()
                player_info["Disciplinary Stats"] = self.get_discipline_stats()
                player_info["Defensive Stats"] = self.get_defender_stats()[2]
            
            elif self.player_position[i] == "Midfielder":
                player_info["Attacking Stats"] = self.get_forward_stats()[0]
                player_info["Team Play Stats"] = self.get_team_play_stats()
                player_info["Disciplinary Stats"] = self.get_discipline_stats()
                player_info["Defensive Stats"] = self.get_midfielder_stats()

            else:
                player_info["Goalkeeping"] = self.get_goalkeeper_stats()[0]
                player_info["Defensive Stats"] = self.get_goalkeeper_stats()[1]
                player_info["Disciplinary Stats"] = self.get_goalkeeper_stats()[2]
                player_info["Team Play Stats"] = self.get_goalkeeper_stats()[3]

            player.append(player_info)
        return player
        
# inst = PlayerStats(url)
# print(inst.get_data())