import boto3

# Get the service resource.
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
# table = dynamodb.create_table(
#     TableName='users',
#     KeySchema=[
#         {
#             'AttributeName': 'username',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'last_name',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'username',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'last_name',
#             'AttributeType': 'S'
#         },
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

table = dynamodb.Table('users')

#response = table.query(KeyConditionExpression=Key('username').eq('Kshitij'))
response = table.scan(
    #FilterExpression = Attr('username').eq('Hanna')
)

items = response['Items']
print(items)
# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)