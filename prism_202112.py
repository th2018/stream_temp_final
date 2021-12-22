import arcpy
from arcpy import env
from arcpy.sa import *

for yr in xrange(2011,2021):
     input07=r"C:\Users\taohuang\Downloads\stream_temp_final-main\PRISM_tmean_stable_4kmM3_"+str(yr)+"07_bil\PRISM_tmean_stable_4kmM3_"+str(yr)+"07_bil.tif"
     output07=r"C:\Users\taohuang\Documents\Tao\Data\PRISM\temp"+str(yr)+"07"
     ExtractValuesToPoints("usgs_wt_ID",input07,output07,"NONE","VALUE_ONLY")
     
     input08=r"C:\Users\taohuang\Downloads\stream_temp_final-main\PRISM_tmean_stable_4kmM3_"+str(yr)+"08_bil\PRISM_tmean_stable_4kmM3_"+str(yr)+"08_bil.tif"
     output08=r"C:\Users\taohuang\Documents\Tao\Data\PRISM\temp"+str(yr)+"08"
     ExtractValuesToPoints("usgs_wt_ID",input08,output08,"NONE","VALUE_ONLY")
     
