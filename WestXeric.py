import arcpy
arcpy.Intersect_analysis(["bas_nonref_WestXeric","mtbs_perims_DD"],"West_Xeric_mtbs")

arcpy.management.AddField("West_Xeric_mtbs","area_ratio","FLOAT")
arcpy.CalculateField_management("West_Xeric_mtbs","area_ratio",'!Shape_Area! / !AREA!',"PYTHON")

