import numpy as np
import datetime
import h5py
import os
#<--------------Funcion para dar formato a las fechas---------------->
def date(day,year):
    #<-----------------Obtencion del dia---------------------->
    date=datetime.date(year,1,1)+datetime.timedelta(days=day)
    #<--------------------Distribucion dia,mes,año----------------->
    year,month,day=str(date.year)[2:4],date.month,date.day
    #<---------------------Formato--------->
    month=date_format(month);day=date_format(day)
    date=year+month+day
    return date
#<--------------Funcion para dar formato a los dias------------------>
def date_format(number):
    if number<10:
        number="0"+str(number)
    else:
        number=str(number)
    return number
#<---------Funcion para localizar la celda en el archivo HDF---------->
def loc_grid(ini,data,n_grid):
    return int(np.abs(ini-data)/n_grid)
#<-----------Transformacion de fecha yyddmm a dia consecutivo----------->
def conse_day(year,month,day,year_i):
    day_conse=(datetime.date(year,month,day)-datetime.date(year,1,1)).days
    year+=-year_i
    return day_conse,year
#<---------------Carpeta de archivos-------------->
dir_data="../Data/"
#<------------data_type=0 for OMI , data_type=1 for OMI_500----------------->
data_type=0
if data_type==0:
    #<--------------Direccion en el HDF--------------------->
    data_loc="/HDFEOS/GRIDS/ColumnAmountAerosol/Data Fields/AbsorbingAerosolOpticalThicknessMW"
    #<--------------------Carpeta de archivos------------------>
    version="OMI/"
    #<------------------Nombre de archivo final---------->
    file_name="AOD_OMI.csv"
    #<----------Separacon en el archivo----------------->
    n_degree=0.25
    #<--------------Factor de escala------------------->
    scale_factor=0.001
else:
    #<--------------Direccion en el HDF--------------------->
    data_loc="/HDFEOS/GRIDS/Aerosol NearUV Grid/Data Fields/FinalAerosolOpticalDepth500"
    #<--------------------Carpeta de archivos------------------>
    version="OMI_500/"
    #<------------------Nombre de archivo final---------->
    file_name="AOD_OMI_500.csv"
    #<----------Separacon en el archivo----------------->
    n_degree=1
    #<--------------Factor de escala------------------->
    scale_factor=1
#<--------------------Localizacion--------------------->
lat_loc,lon_loc=-32.946155,-60.681494
lat_loc=loc_grid(-90,lat_loc,n_degree)
lon_loc=loc_grid(-180,lon_loc,n_degree)
year_i=2019
#<------------------Day ,year------------->
aod_data=np.zeros([365,2])
files=os.listdir(dir_data+version)
print("Leyendo informacion")
for file in files:
    grid=h5py.File(dir_data+version+file,"r")
    #<--------------Extraccion de los valores--------------------->
    if data_type==0:
        dataset=(grid[data_loc][4])[lat_loc-1:lat_loc+2,lon_loc-1:lon_loc+2]
    else:
        dataset=(grid[data_loc])[lat_loc-1:lat_loc+1,lon_loc-1:lon_loc+1]
    values=dataset[dataset>0]
    if np.size(values)!=0:
        #<---------Obtencion del día,mes y año a partir del nombre del archivo------------->
        year=int(file[20+data_type:24+data_type])
        month=int(file[25+data_type:27+data_type])
        day=int(file[27+data_type:29+data_type])
        #<-----------------Dia consecutivo---------------------->
        day,year=conse_day(year,month,day,year_i)
        aod_data[day,year]=np.mean(values)*scale_factor
print("Escribiendo archivo "+file_name)
file=open(dir_data+file_name,"w")
file.write("day,AOD\n")
for year in range(2):
    for day in range(365):
        if aod_data[day,year]!=0:
            date_name=date(day,year+year_i)
            file.write(date_name+","+str(round(aod_data[day,year],3))+"\n")
file.close()
