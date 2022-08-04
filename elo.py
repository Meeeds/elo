import random
#https://github.com/ddm7018/Elo
from elosports.elo import Elo
import sys
import matplotlib.pyplot as plt
import statistics


nb_players = 2500
base_elo = 2000
k_factor = 32
nb_round_robin = 20
#Number of bins in the histogram
number_of_bins = 20

eloLeague = Elo(k = k_factor , homefield = 0)
for i in range(nb_players):
    eloLeague.addPlayer(str(i), rating = base_elo)



for r in range(nb_round_robin):
    print("Running round %d over %d" %(r+1,nb_round_robin))
    for i in range(nb_players):
        for j in range(nb_players):
            if i != j :
                if random.randrange(2)==0:
                    eloLeague.gameOver(winner  = str(i), loser = str(j),  winnerHome = True)
                else:
                    eloLeague.gameOver(loser  = str(i), winner = str(j),  winnerHome = True)
    print("\tAfter round %d/%d elo ecart_t=%f" % (r+1,nb_round_robin,statistics.stdev((eloLeague.ratingDict.values()))))


elo_list=eloLeague.ratingDict.values()
hist_bins = []
current = min(elo_list)
step_elo=(max(elo_list)-min(elo_list))/number_of_bins
while current < max(elo_list):
    hist_bins.append(current)
    current+=step_elo

print(hist_bins)
plt.hist(list(eloLeague.ratingDict.values()), bins=hist_bins)
plt.xlabel('elo min=%f; max=%f; step=%f; mean=%f; ecart_t=%f ' % (min(elo_list), max(elo_list), step_elo, statistics.mean(elo_list), statistics.stdev(elo_list)))
plt.ylabel('#players')
plt.title('%d players; nb_round_robin = %d,  k_factor=%d' % (nb_players, nb_round_robin, k_factor))
plt.show()