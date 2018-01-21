import xml.etree.ElementTree as ET
import csv

tree = ET.parse("/Users/cloudera/Downloads/XPO_SHIPMENT_RECEIPT_20171031203658634_NEW.xml")
root = tree.getroot()

data = open('/tmp/XMLData.csv', 'w')


csvwriter = csv.writer(data)
ireceiptrecord_head = []
detailrecord_head = []

count = 0
count1 = 0
for member in root.findall("./IRECEIPTRECORD"):
        resident = []
        ireceiptrecord = []
        

        if count == 0:
                adddate = member.find('ADDDATE').tag
                ireceiptrecord_head.append(adddate)
                
                addwho = member.find('ADDWHO').tag
                ireceiptrecord_head.append(addwho)
                
                billedcontainerqty = member.find('BILLEDCONTAINERQTY').tag
                ireceiptrecord_head.append(billedcontainerqty)
                
                carrierkey = member.find('CARRIERKEY').tag
                ireceiptrecord_head.append(carrierkey)
                
                carriername = member.find('CARRIERNAME').tag
                ireceiptrecord_head.append(carriername)
                
                for member1 in root.findall('./IRECEIPTRECORD/DETAILLIST/DETAILRECORD'):
                	detailrecord = []
                	if count1 == 0:
                	
                		adddate_dr = member1.find('ADDDATE').tag
                		ireceiptrecord_head.append(adddate_dr + '_DR')
                		
                		addwho_dr = member1.find('ADDWHO').tag
                		ireceiptrecord_head.append(addwho_dr + '_DR')
                		
                		lottable01_dr = member1.find('EXTERNRECEIPTKEY').tag
                		ireceiptrecord_head.append(lottable01_dr)
                		
                		count1 = count1+1
                		print member1
                
                csvwriter.writerow(ireceiptrecord_head)                
                count = count + 1


        addwho = member.find('ADDDATE').text
        ireceiptrecord.append(addwho)
        
        addwho = member.find('ADDWHO').text
        ireceiptrecord.append(addwho)
        
        billedcontainerqty = member.find('BILLEDCONTAINERQTY').text
        ireceiptrecord.append(billedcontainerqty)
        
        carrierkey = member.find('CARRIERKEY').text
        ireceiptrecord.append(carrierkey)
        
        carriername = member.find('CARRIERNAME').text
        ireceiptrecord.append(carriername)
        
        adddate_dr = member1.find('ADDDATE').text
        ireceiptrecord.append(adddate_dr)
        
        addwho_dr = member1.find('ADDWHO').text
        ireceiptrecord.append(addwho_dr)
        
        lottable01_dr = member1.find('EXTERNRECEIPTKEY').text
        ireceiptrecord.append(lottable01_dr)
        
        csvwriter.writerow(ireceiptrecord)

data.close()