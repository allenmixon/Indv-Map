import arcpy

feature_layer = 1
text_element = 2
mxd_path = "<mxd file location here>"

mxd = arcpy.mapping.MapDocument(r"" + mxd_path)

title = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[text_element] #Grab Title from layout

lyr = arcpy.mapping.ListLayers(mxd)

lyr[feature_layer].definitionQuery = 'ID = <id number here>'

df = mxd.activeDataFrame

print(lyr[feature_layer].getExtent())

df.panToExtent(lyr[feature_layer].getExtent())

fname = '<file name here>'
title.text = fname
#mxd.save()

arcpy.mapping.ExportToPDF(mxd, r"<output path here>{}.pdf".format(fname))
del mxd