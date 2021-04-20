from .scraper import PlayerStats
from .models import (PlayerInfo, 
                     PlayerSeasonWiseStats, 
                     AttackingStats, 
                     DefensiveStats, 
                     DisciplinaryStats, 
                     TeamPlayStats, 
                     GoalkeepingStats,
                     )

def update_model():
    
    url = "https://www.premierleague.com/players/"


    data = PlayerStats(url)
    data_library = data.get_data()
    PlayerInfo.objects.all().delete()  
    for item in data_library: 
        
        player = PlayerInfo(
                            name=item['Name'],
                            jersey_no=item["Jersey No"],
                            current_club= item["Current Club"],
                            nationality= item["Nationality"],
                            position= item["Position"],
                            apps= item["Appearances"],
                            wins = item["Total Wins"],
                            losses = item["Total Losses"]
                            )
        player.save()
        for stat in item['Career']:
            player_season = PlayerSeasonWiseStats(
                            name= player,
                            season = stat['Season'],
                            club = stat['Club'],
                            apps = stat['Apps'],
                            goals = stat['Goals']
            )
            player_season.save()          

        if item["Position"] == "Goalkeeper":
            goalkeepingstat = GoalkeepingStats(
                                name = player,
                                saves = item["Goalkeeping"]["Saves"],
                                clean_sheets = item["Clean Sheets"],
                                penalties_saved = item["Goalkeeping"]["Penalties Saved"],
                                punches = item["Goalkeeping"]["Punches"],
                                high_claims = item["Goalkeeping"]["High Claims"],
                                catches = item["Goalkeeping"]["Catches"],
                                sweeper_clearance = item["Goalkeeping"]["Sweeper Clearances"],
                                throw_outs = item["Goalkeeping"]["Throw outs"],
                                goal_kicks = item["Goalkeeping"]["Goal Kicks"]
            )
            disciplinary_stat = DisciplinaryStats(
                                name = player,
                                yellow_cards = item["Disciplinary Stats"]["Yellow Card"],
                                red_cards = item["Disciplinary Stats"]["Red Card"],
                                fouls = item["Disciplinary Stats"]["Fouls"]
            )
            team_play_stats = TeamPlayStats(
                                name = player,
                                assists = item["Team Play Stats"]["Assists"],
                                total_passes = item["Team Play Stats"]["Passes"],
                                passes_per_match = item["Team Play Stats"]["Passes per match"],
                                long_balls = item["Team Play Stats"]["Accurate long balls"],
                                
            )
            defensive_stats = DefensiveStats(
                                name = player,
                                goals_conceded = item["Defensive Stats"]["Goals conceded"],
                                own_goals = item["Defensive Stats"]["Own Goals"]
            )
            goalkeepingstat.save()         
        else:
            if item["Position"] == "Forward" or item["Position"] == "Midfielder":
                attacking_stats = AttackingStats(
                                name = player,                           
                                goals = item["Attacking Stats"]["Goals"],
                                headers= item["Attacking Stats"]["Headers"],
                                right_foot_goals= item["Attacking Stats"]["Right Foot Goals"],
                                left_foot_goals= item["Attacking Stats"]["Left Foot Goals"],
                                hit_woodwork= item["Attacking Stats"]["Hit Woodwork"], 
                                penalties= item["Attacking Stats"]["Penalties"],
                                freekicks= item["Attacking Stats"]["Freekicks"],
                                shots = item["Attacking Stats"]["Shots"],
                                shots_on_target= item["Attacking Stats"]["Shots on target"],
                                accuracy= item["Attacking Stats"]["Accuracy %"],
                                
                )
            else:
                attacking_stats = AttackingStats(
                                name = player,                           
                                goals = item["Attacking Stats"]["Goals"],
                                headers= item["Attacking Stats"]["Headers"],
                                right_foot_goals= item["Attacking Stats"]["Right Foot Goals"],
                                left_foot_goals= item["Attacking Stats"]["Left Foot Goals"],
                                hit_woodwork= item["Attacking Stats"]["Hit Woodwork"],                         

                )
            disciplinary_stat = DisciplinaryStats(
                                name = player,
                                yellow_cards = item["Disciplinary Stats"]["Yellow Card"],
                                red_cards = item["Disciplinary Stats"]["Red Card"],
                                fouls = item["Disciplinary Stats"]["Fouls"],
                                offsides = item["Disciplinary Stats"]["Offsides"]
            )
            if item["Position"] == "Forward":

                team_play_stats = TeamPlayStats(
                                    name = player,
                                    assists = item["Team Play Stats"]["Assists"],
                                    total_passes = item["Team Play Stats"]["Total Passes"],
                                    passes_per_match = item["Team Play Stats"]["Passes per match"],
                                    chances_created = item["Team Play Stats"]["Big Chances Created"],
                                    crosses = item["Team Play Stats"]["Crosses"]
                )
                defensive_stats = DefensiveStats(
                                    name = player,
                                    tackles = item["Defensive Stats"]["Tackles"],
                                    blocked_shots = item["Defensive Stats"]["Blocked Shots"],
                                    interceptions = item["Defensive Stats"]["Interceptions"],
                                    clearances = item["Defensive Stats"]["Clearances"],                               
                                    
                )
            else:
                team_play_stats = TeamPlayStats(
                                    name = player,
                                    assists = item["Team Play Stats"]["Assists"],
                                    total_passes = item["Team Play Stats"]["Total Passes"],
                                    passes_per_match = item["Team Play Stats"]["Passes per match"],
                                    chances_created = item["Team Play Stats"]["Big Chances Created"],
                                    crosses = item["Team Play Stats"]["Crosses"],
                                    cross_accuracy = item["Team Play Stats"]["Cross Accuracy"],
                                    through_balls = item["Team Play Stats"]["Through Balls"],
                                    long_balls = item["Team Play Stats"]["Long Balls"]
                )
                if item["Position"] == "Midfielder":
                    defensive_stats = DefensiveStats(
                                            name = player,
                                            tackles = item["Defensive Stats"]["Tackles"],
                                            tacles_success_rate = item["Defensive Stats"]["Tackle success %"],
                                            blocked_shots = item["Defensive Stats"]["Blocked Shots"],
                                            interceptions = item["Defensive Stats"]["Interceptions"],
                                            clearances = item["Defensive Stats"]["Clearances"],
                                            recoveries = item["Defensive Stats"]["Recoveries"],
                                            duels_won = item["Defensive Stats"]["Duels Wons"],
                                            dues_lost = item["Defensive Stats"]["Duels Lost"],
                                            successful_50_50 = item["Defensive Stats"]["Successful 50/50s"],
                                            aerial_battles_won = item["Defensive Stats"]["Aerial battles won"],
                                            aerial_battles_lost = item["Defensive Stats"]["Aerial battles lost"],
                                            
                    )
                else:
                    defensive_stats = DefensiveStats(
                                            name = player,
                                            clean_sheets= item["Defensive Stats"]["Clean Sheets"],
                                            goals_conceded= item["Defensive Stats"]["Goals conceded"],
                                            tackles = item["Defensive Stats"]["Tackles"],
                                            tacles_success_rate = item["Defensive Stats"]["Tackle success %"],
                                            blocked_shots = item["Defensive Stats"]["Blocked Shots"],
                                            interceptions = item["Defensive Stats"]["Interceptions"],
                                            clearances = item["Defensive Stats"]["Clearances"],
                                            recoveries = item["Defensive Stats"]["Recoveries"],
                                            duels_won = item["Defensive Stats"]["Duels Wons"],
                                            dues_lost = item["Defensive Stats"]["Duels Lost"],
                                            successful_50_50 = item["Defensive Stats"]["Successful 50/50s"],
                                            aerial_battles_won = item["Defensive Stats"]["Aerial battles won"],
                                            aerial_battles_lost = item["Defensive Stats"]["Aerial battles lost"],
                                            own_goals= item["Defensive Stats"]["Own Goals"]
                                            
                    )

            
            attacking_stats.save()
        
        defensive_stats.save()
        team_play_stats.save()
        disciplinary_stat.save()
    
    return "OK"



