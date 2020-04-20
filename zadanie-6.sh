#!/bin/bash
grep -v "#" CPCT02220079.annotated.processed.vcf | awk 'BEGIN {OFS = ";"}{print $1, $8}' >> temp.vcf

touch output.csv
echo "Chr,DP" >> output.csv

while read line; do
	over=0
	count=2
	while [ "$over" == "0" ]; do
		check=$(echo $line | awk -v temp=$count -F ";" '{print $temp}')
		check2=$(echo $check | grep -c "DP=")
		if [ "$check2" == "1" ]; then
			DP2=$(echo $line | awk -v temp=$count -F ";" '{print $temp}')
			DP=$(echo $DP2 | tail -c +4)
			Chr=$(echo $line | awk -F ";" '{print $1}')
			echo "$Chr,$DP" >> output.csv
			over=1
		else
			count=`expr $count + 1`
		fi
	done
done < temp.vcf
