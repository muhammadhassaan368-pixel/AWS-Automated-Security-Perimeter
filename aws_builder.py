import boto3

print("Target locked. Initializing AWS Boto3...")
ec2 = boto3.resource('ec2', region_name='us-east-1')

# 1. Create the Perimeter (VPC)
print("1. Constructing Virtual Private Cloud (VPC)...")
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc.create_tags(Tags=[{"Key": "Name", "Value": "SOC-Lab-VPC"}])
vpc.wait_until_available()
print(f"   [+] VPC created with ID: {vpc.id}")

# 2. Carve out the Zone (Public Subnet)
print("2. Carving out Public Subnet...")
subnet = ec2.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc.id)
subnet.create_tags(Tags=[{"Key": "Name", "Value": "SOC-Public-Subnet"}])
print(f"   [+] Subnet created with ID: {subnet.id}")

# 3. Build the Door to the Internet (Internet Gateway)
print("3. Attaching Internet Gateway...")
igw = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=igw.id)
igw.create_tags(Tags=[{"Key": "Name", "Value": "SOC-Lab-IGW"}])
print(f"   [+] Gateway attached with ID: {igw.id}")

# 4. Map the Network (Route Table)
print("4. Configuring Route Table...")
route_table = vpc.create_route_table()
route_table.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=igw.id)
route_table.associate_with_subnet(SubnetId=subnet.id)
route_table.create_tags(Tags=[{"Key": "Name", "Value": "SOC-Lab-RouteTable"}])
print(f"   [+] Route Table created & linked: {route_table.id}")

# 5. Stand up the Firewall (Security Group)
print("5. Erecting Security Group (Firewall)...")
sec_group = ec2.create_security_group(
    GroupName='soc_lab_firewall',
    Description='SOC Lab Security Group for Nmap and SSH',
    VpcId=vpc.id
)

sec_group.authorize_ingress(
    IpPermissions=[
        {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        {'IpProtocol': 'icmp', 'FromPort': -1, 'ToPort': -1, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ]
)
sec_group.create_tags(Tags=[{"Key": "Name", "Value": "SOC-Lab-Firewall"}])
print(f"   [+] Firewall active: {sec_group.id}")

print("\nMISSION ACCOMPLISHED: Cloud perimeter established successfully.")
