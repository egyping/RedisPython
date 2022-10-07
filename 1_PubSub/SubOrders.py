import redis
import datetime
import time

r = redis.Redis(password='Oma4Mb6Rztwe91797HSi50eRrOLvvOJ2', 
				host='redis-19338.c52.us-east-1-4.ec2.cloud.redislabs.com', 
				port=19338, decode_responses=True)
# decode_responses=True to remvoe the b from b'1665130301815-0' as its orginally recieved as bytes 


while True:
	# get from the stream start from the maximum ID 
	received = r.xread({"orders": '$'}, None, 0)

	print(received)

	for result in received:
		# data represent all the second rows values 
		# will start from the second as it is the unique value "first 0 is header"
		data = result[1]
		#print(type(data)) # <class 'list'>
		#print(data)
		# output
		# [[b'orders', [(b'1665130301815-0', {b'InvoiceNo': b'536464', b'StockCode': b'22952', 
		# b'Description': b'60 CAKE CASES VINTAGE CHRISTMAS', b'Quantity': b'2', b'InvoiceDate': b'12/1/2010 12:23', 
		# b'UnitPrice': b'0.55', b'CustomerID': b'17968', b'Country': b'United Kingdom'})]]]


		# loop in the tuple() and take the second value 1 since first is header "b'orders'," and the actual data is the tuple
		for tuple in data:
			# inside the tuple get the dictionary {} which again start from 1
			orderDict = tuple[1];
			print(orderDict)
			# output 
			# {'InvoiceNo': '536370', 'StockCode': '22900', 'Description': ' SET 2 TEA TOWELS I LOVE LONDON ', 
			# 'Quantity': '24', 'InvoiceDate': '12/1/2010 8:45', 'UnitPrice': '2.95', 'CustomerID': '12583', 
			# 'Country': 'France'}

#	time.sleep(1)

