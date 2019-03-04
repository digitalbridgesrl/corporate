# for python 2.7
# -*- coding: utf-8 -*-
import csv
import xml.etree.cElementTree as ET

root = ET.Element("passwordsafe")
root.set("delimiter",";")
root.set("FromDatabaseFormat", "3.14")
root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
root.set("xsi:noNamespaceSchemaLocation","pwsafe.xsd")

preferences = ET.SubElement(root, "Preferences")

with open('Chrome Passwords.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	i=0
	for row in reader:
		if (i > 0):
			entry=ET.SubElement(root, "entry")
			ET.SubElement(entry, "group").text = "Chrome"
			ET.SubElement(entry, "title").text = row[0]
			ET.SubElement(entry, "url").text = row[1]
			ET.SubElement(entry, "username").text = row[2]
			ET.SubElement(entry, "password").text = row[3]
		i=i+1	
		
tree = ET.ElementTree(root)
tree.write("PwSafeImport.xml")
		
csvFile.close()
