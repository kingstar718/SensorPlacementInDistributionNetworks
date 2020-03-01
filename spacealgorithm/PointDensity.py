# Name: PointDensity_Ex_02.py
# Description: Calculates a magnitude per unit area from point
#    features that fall within a neighborhood around each cell.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inFeatures = "rec_sites.shp"
populationField = "NONE"
cellSize = 60

# Create the Neighborhood Object
radius = 2500
myNbrCirc = NbrCircle(radius, "MAP")

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PointDensity
outPdens = PointDensity(inFeatures, populationField, cellSize,
                        myNbrCirc, "SQUARE_KILOMETERS")

# Save the output
outPdens.save("C:/sapyexamples/output/outpdens")