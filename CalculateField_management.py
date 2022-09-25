import arcpy
arcpy.AddField_management("mtbs_bas_2021","percent_burn","DOUBLE")
arcpy.AddField_management("mtbs_bas_2021","burn_ratio","DOUBLE")
arcpy.CalculateField_management("mtbs_bas_2021","burn_ratio",'!Shape_Area! / !AREA!',"PYTHON_9.3")

