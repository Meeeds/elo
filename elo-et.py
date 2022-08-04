import random
#https://github.com/ddm7018/Elo
from elosports.elo import Elo
import sys
import matplotlib.pyplot as plt
import statistics


nb_players = 1000
base_elo = 1000
nb_round_robin = 6

x_data=[]
y_data=[]


for k_factor in (2**(i/2.0) for i in range (0,15)):
    print("Computing ecart_t for k=%.2f" %(k_factor))
    eloLeague = Elo(k = k_factor , homefield = 0)
    average_ecart_t = 0
    for i in range(nb_players):
        eloLeague.addPlayer(str(i), rating = base_elo)
        
    for r in range(nb_round_robin):
        print("Running round %d/%d k=%.2f" %(r+1,nb_round_robin,k_factor))
        for i in range(nb_players):
            for j in range(nb_players):
                if i != j :
                    if random.randrange(2)==0:
                        eloLeague.gameOver(winner  = str(i), loser = str(j),  winnerHome = True)
                    else:
                        eloLeague.gameOver(loser  = str(i), winner = str(j),  winnerHome = True)
        current_ecart_t = statistics.stdev((eloLeague.ratingDict.values()))
        average_ecart_t+=current_ecart_t
        print("\tAfter round %d/%d elo ecart_t=%.2f" % (r+1,nb_round_robin,current_ecart_t))
        
    average_ecart_t = average_ecart_t/nb_round_robin
    x_data.append(k_factor)
    y_data.append(average_ecart_t)


# Plotting the Graph
plt.plot(x_data, y_data, '--bo')
plt.title("Evolution of ET versus K")
plt.xlabel("K")
plt.ylabel("ecart_t")
plt.show()