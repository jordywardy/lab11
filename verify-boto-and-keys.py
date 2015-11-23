import boto
import urllib2

response = urllib2.urlopen ("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key")
resp = response.read()
key = resp.split(":")

print (key[0])
print (key[1])
print (boto.Version)
