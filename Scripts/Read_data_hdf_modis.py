from pyhdf.SD import SD, SDC
import numpy as np
import datetime
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
#<---------------Carpeta de la infomacion-------------->
dir_list=["Aqua/","Terra/"]
#<---------------Carpeta de archivos-------------->
dir_data="../Data/"
#<--------------------Localizacion--------------------->
lat_loc,lon_loc=-32.946155,-60.681494
year_i=2019
#<------------------Day , sum and count , year------------->
aod_data=np.zeros([365,2,2])
for dir in dir_list:
    print("Analizando datos "+dir)
    #<-------------Localizacion de archivos y nombres------>
    dir_files=dir_data+dir;files=os.listdir(dir_files)
    for file_name in files:
        #<----------------Lectura de datos----------------->
        file=SD(dir_files+file_name,SDC.READ)
        lon=file.select("Longitude").get()
        lat=file.select("Latitude").get()
        #<------------------Seleccion de zonas deseadas-------------->
        locs=lon[np.abs(lon-lon_loc)<0.1]
        for loc in locs:
            exists=False
            #<---------------Localizacion de los datos--------------->
            locs_x,locs_y=np.where(lon==loc)
            for x,y in zip(locs_x,locs_y):
                #<-----------------Seleccion de zona deseada------------------->
                if np.abs(lat[x,y]-lat_loc)<0.1:
                    exists=True
                if exists:
                    #<---------------obtencion de año y dia consecutivo------------->
                    year,day=int(file_name[10:14]),int(file_name[14:17])
                    if day>=365:
                        day=day-365
                    #<-------------------Obtencion de los datos---------------->
                    aod=(file.select("Optical_Depth_Land_And_Ocean").get())[x][y]
                    if aod>0:
                        #<------------------Suma de los datos----------------->
                        aod_data[day-1,0,year-year_i]+=aod
                        aod_data[day-1,1,year-year_i]+=1
        #<--------------Cierre archivo de medicion--------------->
        file.end()
#<--------------Apertura de archivo final-------------------------->
file_data=open(dir_data+"AOD_MODIS.csv","w")
for year in range(2):
    for day in range(365):
        if aod_data[day,1,year]!=0:
            #<----------------------Valor medio del AOD------------------>
            aod_mean=aod_data[day,0,year]/aod_data[day,1,year]
            date_name=date(day,year+year_i)
            #<-----------------Escritura de archivo------------------->
            file_data.write(date_name+","+str(round(aod_mean))+"\n")
#<----------------------Cierre de archivo final----------------->
file_data.close()