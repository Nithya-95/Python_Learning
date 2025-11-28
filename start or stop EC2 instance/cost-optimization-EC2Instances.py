import boto3
def lambda_handler(event, context):
    action=event['action']
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    instances = []      
    for Reservation in response['Reservations']:
        for instance in Reservation['Instances']:
            instances.append(instance['InstanceId'])
            print(instance['InstanceId'])
            for instanceid in instances:
                if action == 'stop':
                    ec2.stop_instances(InstanceIds=[instanceid])
                    print('stopped your instances: ' + str(instances))
                elif action == 'start':
                    ec2.start_instances(InstanceIds=[instanceid])
                    print('started your instances: ' + str(instances))
                else:
                    print('invalid action')

     
