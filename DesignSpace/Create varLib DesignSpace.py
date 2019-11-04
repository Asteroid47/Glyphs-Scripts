import xml.etree.ElementTree as ET

from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")



font = Glyphs.font
familyName = font.familyName
ver = 4.0 
designSpace = ET.Element('designspace')
designSpace.set('name',str(ver))
axesX = ET.SubElement(designSpace, 'axes')
for i, axes in enumerate(font.axes):
	print (axes)
	axis = ET.SubElement(axesX, 'axis')
	name = axes['Name']
	tag = axes['Tag']
	axis.set('name', name)
	axis.set('tag', tag)
	minAx = 9999999999999 
	maxAx = 0
	for master in font.masters:
		aX = master.axes[i]
		if (aX < minAx):
			minAx = aX
		if (aX > maxAx):
			maxAx = aX
	defAx = ((maxAx - minAx)/2) + minAx
	axis.set('default', str(defAx))
	axis.set('maximum', str(maxAx))
	axis.set('minimum', str(minAx))

sourcesX =ET.SubElement(designSpace, 'sources')
for master in font.masters:
	print (master)
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
myfile = open(filePath+familyName+".designspace", "w+")
mydata = prettify(designSpace)

myfile.write(mydata)
