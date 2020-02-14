import boto3

print("Starting boto3 program...")
s3 = boto3.resource("s3")
try:
    for b in s3.buckets.all():
        print(b.name)
    data = open('test.txt', 'rb')
    s3.Bucket('sampleboto3bucket').put_object(Key='test.txt', Body=data)
except Exception:
    print("Some error  {}".format(Exception.__name__))
finally:
    print("Exiting the boto3 program")


