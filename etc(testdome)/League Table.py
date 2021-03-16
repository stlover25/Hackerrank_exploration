"""
problem_source : https://www.testdome.com/questions/python/league-table/40262?visibility=3&skillId=9
"""

from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        
        rank -=1
        temp = []
        
        for i in self.standings:
            
            s_score = self.standings[i]['score']
            s_game = self.standings[i]['games_played']
            
            if len(temp) == 0 or (temp[-1][1] > s_score) :
                
                temp.append((i, s_score, s_game))
            
            elif s_score > temp[0][1]:
                
                temp.insert(0, (i, s_score, s_game))
               
            else:
                
                for j in range(len(temp)):
                    
                    if s_score >= temp[j][1]:
                        
                        print(j, temp)
                        if s_score == temp[j][1] and s_game >= temp[j][2]:
                            
                            if j == len(temp)-1:
                                temp.append((i, s_score, s_game))
                            else:
                                continue
                        
                        else:
                            
                            temp.insert(j, (i, s_score, s_game))
                            
                            break
       
        
        return temp[rank][0]

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))
