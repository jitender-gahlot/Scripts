import xml.etree.ElementTree as ET
import csv

tree = ET.parse("/tmp/sample.xml")
root = tree.getroot()

data = open('/tmp/XMLData.csv', 'w')


csvwriter = csv.writer(data)
resident_head = []

count = 0
for member in root.findall("./IRECEIPTRECORD/DETAILLIST/DETAILRECORD"):
        resident = []

        if count == 0:
                name = member.find('ITEM').tag
                resident_head.append(name)
                altsku = member.find('./ITEMDETAIL/ITEM/ALTSKU').tag
                resident_head.append(altsku)
                csvwriter.writerow(resident_head)
                count = count + 1

        name = member.find('ITEM').text
        resident.append(name)
        altsku = member.find('./ITEMDETAIL/ITEM/ALTSKU').tag
        resident.append(altsku)
        csvwriter.writerow(resident)

data.close()