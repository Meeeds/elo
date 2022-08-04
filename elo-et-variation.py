import random
#https://github.com/ddm7018/Elo
from elosports.elo import Elo
import sys
import matplotlib.pyplot as plt
import statistics
from matplotlib.pyplot import cm
import numpy as np


base_elo = 1000
nb_round_robin = 3
k_factor = 32
#Number of bins in the histogram



iter_nb_players = range(200,2400,1000)
color = iter(cm.rainbow(np.linspace(0, 1, len(iter_nb_players))))

for nb_players in iter_nb_players:
    print("Computing ecart_t for nb_players=%d" %(nb_players))
    eloLeague = Elo(k = k_factor , homefield = 0)
    x_data=[]
    y_data=[]
    for i in range(nb_players):
        eloLeague.addPlayer(str(i), rating = base_elo)
        
    for r in range(nb_round_robin):
        print("Running round %d/%d k=%d" %(r+1,nb_round_robin,k_factor))
        for i in range(nb_players):
            for j in range(nb_players):
                if i != j :
                    if random.randrange(2)==0:
                        eloLeague.gameOver(winner  = str(i), loser = str(j),  winnerHome = True)
                    else:
                        eloLeague.gameOver(loser  = str(i), winner = str(j),  winnerHome = True)
        current_ecart_t = statistics.stdev((eloLeague.ratingDict.values()))
        print("\tAfter round %d/%d elo ecart_t=%f" % (r+1,nb_round_robin,current_ecart_t))
        x_data.append(r)
        y_data.append(current_ecart_t)
        
    plt.plot(x_data, y_data, '--.', c=next(color), label='nb_players=%d' % nb_players)


# Plotting the Graph
plt.title("Evolution of ET per round for different nb_players")
plt.xlabel("round")
plt.ylabel("ecart-type")
plt.legend(loc='best')
plt.show()