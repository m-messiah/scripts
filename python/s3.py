#!/usr/bin/python
import boto
import boto.s3.connection
from random import randint
access_key = ''
secret_key = ''

conn = boto.connect_s3(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key,
    host = '',
    calling_format = boto.s3.connection.OrdinaryCallingFormat())

print "Buckets:"
for bucket in conn.get_all_buckets():
    print "{name}\t{created}".format(
            name = bucket.name,
            created = bucket.creation_date,
    )


print "Delete bucket 'test':"
conn.delete_bucket(conn.get_bucket('test'))


print "Create bucket:"
bucket = conn.create_bucket('test2')
print "Created " + bucket.name

print "Bucket content:"
for key in bucket.list():
    print u"{name}\t{size}".format(
        name = key.name,
        size = key.size)


print "Delete content"
bucket.delete_key('test.jpg')


print "New key"
key = bucket.new_key('hello.txt')
key.set_contents_from_filename('hello.txt')

print "Get key"
key = bucket.get_key("hello.txt")
print key
