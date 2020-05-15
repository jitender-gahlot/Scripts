#!/bin/bash
echo "Executing Script. Please wait..."
redis_host_file=./redis-host.txt
db_number=1
while IFS= read -r line
do
  #echo "$line"
  host=$(echo $line | cut -d ":" -f 1)
  port=$(echo $line | cut -d ":" -f 2)
  pwd=$(echo $line | cut -d ":" -f 3)
  #echo $host
  #echo $port
  #echo $pwd
  #echo ""

max_memory=$(redis-cli -h $host -p $port -a $pwd --no-auth-warning info memory | grep 'maxmemory' -w)
m=$(echo $max_memory| cut -d ":" -f 2| tr -d '\r')

used_memory=$(redis-cli -h $host -p $port -a $pwd --no-auth-warning info memory | grep 'used_memory' -w)

u=$(echo $used_memory| cut -d ":" -f 2| tr -d '\r')

keyspace=$(redis-cli -h $host -p $port -a $pwd --no-auth-warning info keyspace | grep 'db')
k=$(echo $keyspace| cut -d ":" -f 2| tr -d '\r'| cut -d',' -f 1)
#echo $k
echo "Extracting details for" DB:$db_number "and HOST"":"$host
redis-cli -h $host -p $port -a $pwd --no-auth-warning info commandstats | grep "cmdstat_" | sed -e 's/[:,=]/,/g' | sort -n -k 3rn -t ',' | sed -e 's/cmdstat_//g' | awk -F ',' -v OFS=',' -v m_memory=$m -v u_memory=$u -v key=$k -v h=$host -v date="$(date +"%Y-%m-%d %r")" 'NR==1  {print "command,operations,usec_per_op,max_memory,used_memory,keyspace,host,timestamp"}{print $1,$3,$7,m_memory,u_memory,key,h,date}' >> db$db_number"_"$host.csv

((db_number++))
done < $redis_host_file
echo "Execution completed!"