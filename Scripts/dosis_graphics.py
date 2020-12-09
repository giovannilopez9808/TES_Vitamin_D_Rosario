import matplotlib.pyplot as plt
import numpy as np

def plot_grids(ax,lim,div):
    for x in np.linspace(0,366,13):
        ax.plot([x,x],[0,lim],ls="--",color="grey",alpha=0.5)
    for y in np.arange(0,lim+div,div):
        ax.plot([0,366],[y,y],ls="--",color="grey",alpha=0.5)

def plot_data(ax,data,lim,div,meses,days,title,color):
    ax.plot(np.arange(days),data,color=color,lw=3)
    ax.set_title(title)
    plot_grids(ax,lim,div)
    ax.set_yticks(np.arange(0,lim+div,div))
    ax.set_xlim(0,days)
    ax.set_ylim(0,lim)
    if ax==ax2:
        ax.set_xticks(np.linspace(0,days,13))
        ax.set_xticklabels(meses)
    else:
        ax.set_xticks([])

meses=["jun","jul","agt","sept","oct","nov","dic","en","feb","mzo","abr","my","jun"]
dir_data="../Data/Rosario_period/"
dates,time_vitamin,time_med=np.loadtxt(dir_data+"dosis_time.csv",delimiter=",",unpack=True,skiprows=1)
fig,(ax1,ax2)=plt.subplots(2)
days=366
lim,div=40,10;title="Pre Vitamina D";color="#6930c3"
plot_data(ax1,time_vitamin,lim,div,meses,days,title,color)
lim,div=80,20;title="MED";color="#4ea8de"
plot_data(ax2,time_med,lim,div,meses,days,title,color)
fig.text(0.04, 0.5, 'Tiempo (min)', va='center', rotation='vertical',fontsize=13)
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.952,top=0.912,hspace=0.248)
plt.show()
