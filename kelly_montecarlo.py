import numpy as np
import matplotlib.pyplot as plt
from random import choices
import time

t1=time.time()



for k in range(1,100):
    total_winnings=[]
    outcomes=[0,1]
    weights=[0.4,0.6]
    flips=[]
    for e in range(0,2500):
        flips.append(choices(outcomes,weights))
    flips=sum(flips,[])

    

    proportions=(np.arange(0.01,1,0.01).tolist())
    proportions=[round(e,2) for e in proportions]
    for e in proportions:
            bankroll=1000
            for f in flips:
                if f==1:
                    bankroll=bankroll*(1+e)
                elif f==0:
                    bankroll=bankroll*(1-e)
            total_winnings.append(bankroll)
            norm = [float(e)/sum(total_winnings) for e in total_winnings]
    percent_bet=[e*100 for e in proportions]
    plt.plot(percent_bet,norm)
plt.title('Optimal Betting Strategy for Loaded Coin')
plt.xlabel('Percentage of Bankroll Wagered')
plt.ylabel('Normalized Ending Bankroll')
plt.show()
plt.savefig('kellymontecarlo.png')


t2=time.time()
print(t2-t1)