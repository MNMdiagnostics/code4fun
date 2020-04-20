#!/bin/bash
grep -v "#" CPCT02220079.annotated.processed.vcf | awk 'BEGIN {OFS = ";"}{print $1, $8}' >> temp.vcf

touch output.csv
echo "Chr,DP" >> output.csv

while read line; do
	over=0
	count=2
	while [ "$over" == "0" ]; do
		check=$(echo $line | awk -v temp=$count -F ";" '{print $temp}')
		echo $check
		check2=$(echo $check | grep -c "DP=")
		if [ "$check2" == "1" ]; then
			echo $line | awk -v temp=$count -F ";" 'BEGIN {OFS = ","}{print $1, $temp}' >> temp.csv
			cat output.csv temp.csv >> temp2.csv
			mv temp2.csv output.csv
			rm temp.csv
			over=1
		else
			count=`expr $count + 1`
		fi
	done
done < temp.vcf
