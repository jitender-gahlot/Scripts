import xml.etree.ElementTree as ET
import csv

tree = ET.parse("/Users/cloudera/Downloads/XPO_SHIPMENT_RECEIPT_20171031203658634_NEW.xml")
root = tree.getroot()

data = open('/tmp/XMLData.csv', 'w')


csvwriter = csv.writer(data)
ireceiptrecord_head = []
header = ['ADDDATE', 'ADDWHO', 'BILLEDCONTAINERQTY', 'CARRIERKEY' , 'CARRIERNAME', 'ADDDATE_DR', 'ADDWHO_DR', 'EXTERNRECEIPTKEY', 'CLIENT_ID', 'ALTSKU', 'DESCR']
csvwriter.writerow(header)

for member in root.findall("./IRECEIPTRECORD"):
        ireceiptrecord = []
        
        adddate = member.find('ADDDATE').text
        ireceiptrecord_head.append(adddate)
                
        addwho = member.find('ADDWHO').text
        ireceiptrecord_head.append(addwho)
                
        billedcontainerqty = member.find('BILLEDCONTAINERQTY').text
        ireceiptrecord_head.append(billedcontainerqty)
                
        carrierkey = member.find('CARRIERKEY').text
        ireceiptrecord_head.append(carrierkey)
                
        carriername = member.find('CARRIERNAME').text
        ireceiptrecord_head.append(carriername)
        
        
                
        for member1 in root.findall('./IRECEIPTRECORD/DETAILLIST/DETAILRECORD'):
        	detailrecord = []
        	
        	adddate_dr = member1.find('ADDDATE').text
        	detailrecord.append(adddate_dr + '_DR')
        	
        	addwho_dr = member1.find('ADDWHO').text
        	detailrecord.append(addwho_dr + '_DR')
        	
        	lottable01_dr = member1.find('EXTERNRECEIPTKEY').text
        	detailrecord.append(lottable01_dr)
        	
        	
        	
        	
        	for member2 in root.findall('./IRECEIPTRECORD/DETAILLIST/DETAILRECORD/ITEMDETAIL/ITEM'):
        		itemrecord = []
        		client_id = member2.find('CLIENT_ID').text
        		itemrecord.append(client_id)
        		
        		altsuk = member2.find('ALTSKU').text
        		itemrecord.append(altsuk)
        		
        		descr = member2.find('DESCR').text
        		itemrecord.append(descr)
        		
        		break;
        	csvwriter.writerow(ireceiptrecord_head + detailrecord + itemrecord)
        		
        	
data.close()