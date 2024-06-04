#!/bin/bash
export host="localhost"
export port="5432"
export database="giavang"
export user="postgres"
export password="123"
file="D:/INTERN/data_insert.txt"
while IFS= read date
do
	read value1
	read value2
	read value3
	read value4
	read value5
	echo $date
	echo $value1
	echo $value2
	echo $value3
	echo $value4
	echo $value5
	D:/pg/bin/psql.exe -h"$host" -p"$port" -U"$user" -d"$database" -c"INSERT INTO dulieu.thegioi (\"Date\",\"price\",\"Open\",\"high\",\"low\",\"ChangePercent\") VALUES('$date','$value1','$value2','$value3','$value4','$value5');"
done < "$file"
