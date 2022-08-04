import random
#https://github.com/ddm7018/Elo
from elosports.elo import Elo
import sys
import matplotlib.pyplot as plt
import statistics
from matplotlib.pyplot import cm
import numpy as np

nb_players = 2000
matches_ratio = 0.01
nb_matches = nb_players * nb_players * matches_ratio
base_elo = 1000
plot_step = 10
print_step = plot_step*100
k_factor = 32
number_of_curve = 4

#Number of bins in the histogram
color = iter(cm.rainbow(np.linspace(0, 1, number_of_curve)))

for iteration in range(number_of_curve):
    print("Iteration %d "% iteration)
    eloLeague = Elo(k = k_factor , homefield = 0)
    x_data=[]
    y_data=[]
    for i in range(nb_players):
        eloLeague.addPlayer(str(i), rating = base_elo)
        
    for m in range(int(nb_matches)):
        i,j = random.sample(range(nb_players), 2)
        if random.randrange(2)==0:
            eloLeague.gameOver(winner  = str(i), loser = str(j),  winnerHome = True)
        else:
            eloLeague.gameOver(loser  = str(i), winner = str(j),  winnerHome = True)
            
            
        if m % plot_step == 0 or m < nb_matches * 0.4 :
            current_ecart_t = statistics.stdev((eloLeague.ratingDict.values()))
            x_data.append(m)
            y_data.append(current_ecart_t)
            if m % print_step == 0:
                print("\tAfter nb_matches %d/%d=%.2f%% elo ecart_t=%.2f" % (m+1,nb_matches, 100.0*m/nb_matches, current_ecart_t))
            
        
    plt.plot(x_data, y_data, c=next(color), label='iteration=%d' % iteration)


# Plotting the Graph
plt.title("Evolution of ET per matches nb_players=%d, plot_step=%d" % (nb_players, plot_step))
plt.xlabel("matches")
plt.ylabel("ecart-type")
plt.legend(loc='best')
plt.show()