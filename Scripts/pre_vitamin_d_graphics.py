import matplotlib.pyplot as plt
import numpy as np
dir_vitamin_d="../Data/Rosario_period/"
dir_graphics="../Graphics/"
day_i=datetime.date(2019,6,1)
day_f=datetime.date(2020,5,31)
n_days=(day_f-day_i).days+1
date=np.loadtxt(dir_vitamin_d+"sza_vitamin_max.csv",delimiter=",",skiprows=1,usecols=0,dtype=str)
data_vitamin=np.loadtxt(dir_vitamin_d+"sza_vitamin_max.csv",delimiter=",",skiprows=1,usecols=2)
x=np.arange(0,n_days,25);x=np.append(x,n_days)
plt.scatter(np.arange(n_days),data_vitamin,color="#6a040f")
plt.xlim(0,n_days)
plt.ylim(0,1)
plt.xticks(x,date[x-1],rotation=60)
plt.yticks(np.arange(0,1+0.1,0.1))
plt.grid(ls="--",color="grey",alpha=0.3)
plt.subplots_adjust(left=0.114,bottom=0.171,right=0.945,top=0.94)
plt.savefig(dir_graphics+"Previtamin_D.png",dpi=300)