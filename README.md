# RedisPython

Async: This term you will have to use in some cases where you have to decouple the request between code query some data and responder serve the needed data.
At the common web server the customer click PLACE ORDER, and he waits for sometime to get the order number and if the order success or failed, at the backend side you have written professional method to handle the order, but its quite long function going through processes, payments, check the stock, deduct the stock ...etc.
What if you are getting 100K order per hour, do you think it is efficient to make the customer waiting for your function to respond?!
Here is the decoupling concept started to shine since few years since the online users increasing extensively.
So, old way of handling the traffic is called synchronous and the new way is asynchronous.
In the Async world there are a lot of methods , PubSub, Streams, Messaging these are the most well known.
Redis is GREAT you can use it for cashing, PubSub, Streams, No-Sql and few other usages.


Database
redis-19338.c52.us-east-1-4.ec2.cloud.redislabs.com:19338
Username: "default"
DB_PASSWORD
r = redis.Redis(password='DB_PASSWORD', host='redis-19338.c52.us-east-1-4.ec2.cloud.redislabs.com', port=19338)

local mac-os
brew install redis
redis-server
redis-cli
ping

cloud - redis.io
redis-cli -h redis-19338.c52.us-east-1-4.ec2.cloud.redislabs.com -p 19338 -a DB_PASSWORD
ping
info

setup environment variable macos
export REDIS_OM_URL=redis://default:DB_PASSWORD@redis-19338.c52.us-east-1-4.ec2.cloud.redislabs.com:19338
echo $REDIS_OM_URL


python3 -m venv home_env
source home_env/bin/activate
pip install redis
python shell 
import redis 
r = redis.Redis(password='DB_PASSWORD', host='redis-19338.c52.us-east-1-4.ec2.cloud.redislabs.com', port=19338, decode_responses=True)
> set key value pair 
r.set('foo', 'bar')
r.get('foo')


Redis streams 
xrange to select range of data 
listen to new stuff xread like pubsub 
xread block 

>> Practice order data - streaming data instead of kafka 
Streams retain the data unlike pubsub
StreamOrders and SubOrders files 
1- exceute the StreamOrders 
python 1_Streams/StreamOrders.py 
2- excute the sub from another terminal 
