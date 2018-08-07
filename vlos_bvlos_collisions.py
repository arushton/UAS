import matplotlib.pyplot as plt
import numpy as np
import seaborn


# Input parapmeters
V_g = 122**3 # in metres assume a volume of 400ft^3
n_v = 5 # number of vlos
n_b = 1 # number of bvlos
s_v = 0.5 # size of vlos in m
s_b = 1 # size of bvlos in m


# distance travel by bvlos
dist_b = 122 # meters


def three_d():
    
    # Occupancy of a BVLOS instance
    V_occ = dist_b * (s_v + s_v + s_b)**2
    
    print("prob. of interaction {:.2}%" .format(n_v*100*V_occ/V_g ))
    # Let assume we have 7e4 bvlos (per day)
    total_bvlos = np.arange(1,7e4,1)
    # The total occupany of green could be:
    total_occ = total_bvlos * V_occ /122
    print(total_occ)
    
    plt.loglog(total_bvlos,0.01/total_occ,label="1%")
    plt.loglog(total_bvlos,0.001/total_occ,label="0.1%")
    plt.loglog(total_bvlos,0.0001/total_occ,label="0.01%")
    plt.xlabel("Number of BVLOS flights per day")
    plt.ylabel(r"Average desnity of VLOS (per m$^3$)")
    plt.axhline(122**-3) # One drone per 122m^3
    plt.axhline(1000**-3) # One drone per 1km^3
    plt.axhline(4000**-3) # One drone per 4km^3  
    plt.legend(title="Probability of collision")


np.sqrt(1e9/122)


def airspace():
    
    
    plt.plot([0,1],[0,1])
    plt.Rectangle(0.5,0.5,0.1,0.1)

    plt.gca()
    plt.Rectangle((  .5,  .5), .1, .4, facecolor="blue")


from matplotlib.patches import Rectangle
#someX, someY = 2, 3
#currentAxis = plt.gca()
#currentAxis.add_patch(Rectangle((someX - .3, someY - .5), 10, 10, facecolor="green", alpha=0.2))

def two_d():
    V_occ = (s_v + s_v + s_b)**2

    total_bvlos = np.arange(1,7e4,1)
    # The total occupany of green could be:
    total_occ = 1e-6* total_bvlos * V_occ
    print(total_occ)
    plt.loglog(total_bvlos,0.01/total_occ,label="1%",ls='-', c='k')
    plt.loglog(total_bvlos,0.001/total_occ,label="0.1%",ls='-.', c='k')
    plt.loglog(total_bvlos,0.0001/total_occ,label="0.01%",ls='--', c='k')
    plt.xlabel("Number of BVLOS flights per day")
    plt.ylabel(r"Average desnity of VLOS (per km$^2$)")
    plt.axhline(0.122**-2,ls=':',c='k',alpha=0.35) # One drone per 122m^3
    plt.axhline(1**-2,ls=':',c='k',alpha=0.35) # One drone per 1km^3
    plt.axhline(10**-2,ls=':',c='k',alpha=0.35) # One drone per 4km^3  
    plt.legend(title="Probability of collision")
    plt.title("Risk of BLVOS-VLOS collision")

two_d()


# Area of England:
A_Eng = 1.3e8 # m
V_Eng = A_Eng *122


# Example in one 122**3 m^3 volume

total_occ = 1 * V_occ

max_vlos = 0.001*122**3 / V_occ
print ("Number of VLOS in one sector",0.001*122**3 / V_occ)



max_vlos / 122**3

