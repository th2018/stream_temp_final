import arcpy
arcpy.Intersect_analysis(["bas_ref_all", "mtbs_perims_DD",],"bas_mtbs","ALL")

