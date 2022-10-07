import csv
import redis

r = redis.Redis(password='Oma4Mb6Rztwe91797HSi50eRrOLvvOJ2', host='redis-19338.c52.us-east-1-4.ec2.cloud.redislabs.com', port=19338)

# open the file and assign the content to csvf
# the csv file must exist at the root path
with open("OnlineRetail.csv", encoding='utf-8-sig') as csvf:
	# use csv to make the data dictionary objects
	csvReader = csv.DictReader(csvf)

	# iterate over each row and use xadd to add to stream called orders 
	for row in csvReader:
		r.xadd("orders", row)
