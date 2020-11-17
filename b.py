from pyhdf.SD import SD, SDC
file=SD("data.hdf",SDC.READ)
data=file.select("Optical_Depth_047").get()
print(data)