#MenuTitle: Create varLib Designspace 
# -*- coding: utf-8 -*-
__doc__="""
Export a .designspace file for use with varLib
"""


import xml.etree.ElementTree as ET
from xml.dom import minidom

def cleanUp(elem):
    unparsed = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(unparsed)
    return reparsed.toprettyxml(indent="  ")

def minMax(aNo):
	axisVal = [master.axes[aNo] for master in font.masters]
	axisMax = str(max(axisVal))
	axisMin = str(min(axisVal))
	axis.set('maximum', axisMax)
	axis.set('minimum', axisMin)

def getDefault():
	defaultMaster = None
	for i, master in enumerate(font.masters):
		if 'isDefault' in master.customParameters:
			defaultMaster = master
			break
	if defaultMaster == None:
		defaultMaster = font.masters[0];
		print("No default master defined! Using first!")
	return defaultMaster



font = Glyphs.font
familyName = font.familyName
defaultMaster = getDefault()
ver = 4.0 
designSpace = ET.Element('designspace')
designSpace.set('name',str(ver))
axesX = ET.SubElement(designSpace, 'axes')
for i, axes in enumerate(font.axes):
	axis = ET.SubElement(axesX, 'axis')
	name = axes['Name']
	tag = axes['Tag']
	axis.set('name', name)
	axis.set('tag', tag)
	minMax(i)
	axis.set('default', str(defaultMaster.axes[i]))

sourcesX =ET.SubElement(designSpace, 'sources')
for master in font.masters:
	source = ET.SubElement(sourcesX, 'source')
	name = master.name
	fileName = familyName + "-"+name+".ttf"
	source.set('familyname', familyName)
	source.set('filename', fileName)
	source.set('name', 'master.'+familyName+'.'+name)
	source.set('stylename', name)
	location = ET.SubElement(source, 'location')
	for i, axes in enumerate(master.axes):
		dimension = ET.SubElement(location, 'dimension')
		axis = font.axes[i]
		name = axis['Name']
		dimension.set('name', name)
		xVal = str(axes)
		dimension.set('xvalue', xVal)

instancesX = ET.SubElement(designSpace, 'instances')
for instance in font.instances:
	instanceX = ET.SubElement(instancesX, 'instance')
	instanceX.set('familyname', familyName)
	instanceName = instance.name
	instanceX.set('stylename', instanceName)
	location = ET.SubElement(instanceX, 'location')
	for i, axes in enumerate(instance.axes):
		dimension = ET.SubElement(location, 'dimension')
		axis = font.axes[i]
		name = axis['Name']
		dimension.set('name', name)
		xVal = str(axes)
		dimension.set('xvalue', xVal)


filePath = font.filepath
split = filePath.split("/")
leng = len(split[-1])
filePath = filePath[:-leng]
dsFile = open(filePath+familyName+".designspace", "w+")
data = cleanUp(designSpace)

dsFile.write(data)
dsFile.close()
