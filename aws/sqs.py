import boto3

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='test')
response = queue.send_message(MessageBody='Hello World!')
queue.send_message(MessageBody='boto3', MessageAttributes={
    'Author': {
        'StringValue': 'Daniel',
        'DataType': 'String'
    }
})
for queue in sqs.queues.all():
    print(queue.url)
    queue.delete_queue

print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))


