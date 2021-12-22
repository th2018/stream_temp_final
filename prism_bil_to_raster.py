import arcpy
from arcpy import env
from arcpy.sa import *

for yr in xrange(2011,2021):
     input07=r"C:\Users\taohuang\Downloads\stream_temp_final-main\PRISM_tmean_stable_4kmM3_"+str(yr)+"07_bil\PRISM_tmean_stable_4kmM3_"+str(yr)+"07_bil.bil"
     arcpy.RasterToOtherFormat_conversion(input07,r"C:\Users\taohuang\Downloads\stream_temp_final-main\PRISM_tmean_stable_4kmM3_"+str(yr)+"07_bil","TIFF")
     input08=r"C:\Users\taohuang\Downloads\stream_temp_final-main\PRISM_tmean_stable_4kmM3_"+str(yr)+"08_bil\PRISM_tmean_stable_4kmM3_"+str(yr)+"08_bil.bil"
     arcpy.RasterToOtherFormat_conversion(input08,r"C:\Users\taohuang\Downloads\stream_temp_final-main\PRISM_tmean_stable_4kmM3_"+str(yr)+"08_bil","TIFF")
     



