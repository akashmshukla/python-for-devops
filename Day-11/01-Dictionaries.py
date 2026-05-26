ec2_instances_info =[
    {
        "id":"instance-1",
        "type":"t2.micro"
    },
    {
        "id":"instance-2",
        "type":"t2.medium"
    },
    {
        "id":"instance-3",
        "type":"t2.xlarge"
    }
]

print(ec2_instances_info[2]["id"])
print(ec2_instances_info[1]["type"])