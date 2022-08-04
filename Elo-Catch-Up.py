import random
#https://github.com/ddm7018/Elo
from elosports.elo import Elo
import sys
import matplotlib.pyplot as plt
import statistics
from matplotlib.pyplot import cm
import numpy as np


base_elo = 1000
real_elo  = 2000
nb_match = 500
player0 = "0"
player1 = "1"
color = iter(cm.rainbow(np.linspace(0, 1, len(range (0,7)))))


x_data=[]
y_data=[]
#plot target
for i in range(1,nb_match):
    x_data.append(i)
    y_data.append(real_elo)
    
plt.plot(x_data, y_data, c=next(color), label='target=%d elo' % real_elo)


for k_factor in (2**(i/1.0) for i in range (0,6)):
    eloLeague = Elo(k = k_factor , homefield = 0)
    eloLeague.addPlayer(player0, rating = base_elo)
    eloLeague.addPlayer(player1, rating = base_elo)
    x_data=[]
    y_data=[]
    

    for i in range(1,nb_match):
        current_guy_elo = eloLeague.ratingDict[player0]
        current_proba = eloLeague.expectResult(real_elo,current_guy_elo)
        print("Start match %d, current_guy_elo=%.2f, current_proba=%.2f%%" % (i , current_guy_elo, 100*current_proba ))
        if random.uniform(0, 1) < current_proba :
            eloLeague.gameOver(player0, player1,  winnerHome = True)
        else:
            eloLeague.gameOver(player1, player0,  winnerHome = True)
            
        #update oponent to current elo
        #print("before", eloLeague.ratingDict[player0],eloLeague.ratingDict[player1])
        eloLeague.ratingDict[player1]=eloLeague.ratingDict[player0]
        #print("after", eloLeague.ratingDict[player0],eloLeague.ratingDict[player1])
        x_data.append(i)
        y_data.append(eloLeague.ratingDict[player1])
    
    plt.plot(x_data, y_data, c=next(color), label='k_factor=%.2f' % k_factor)
        
        
plt.title("Catch up to real_elo=%d" % real_elo)
plt.xlabel("matches")
plt.ylabel("elo")
plt.legend(loc='best')
plt.show()
    


