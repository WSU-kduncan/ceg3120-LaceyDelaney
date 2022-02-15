Lacey Delaney 
Project 2
Feb 15 2022

Part 1 - Build a VPC

1. Create a VPC 
- Virual Private Cloud: virtual network dedicated to your AWS account. 
![vpc](https://user-images.githubusercontent.com/77417309/154163095-d4bd24cb-2284-407a-8c54-dfbd1d22c103.png)

2. Create a subnet
- Subnet: a range of IP addresses in your VPC. Can use a public subnet for resources that must be connected to the internet. 
, and a private subnet for resources that won't be connected to the internet. 
![subnet](https://user-images.githubusercontent.com/77417309/154163113-9e4d6a90-dfeb-43c2-b731-3dc900cb3ba9.png)


3. Create an internet gateway
- An Internet gateway can transfer communications between an enterprise network and the Internet.
![internetgateway](https://user-images.githubusercontent.com/77417309/154163143-2908f108-49ac-41ba-a973-3c17872b80c4.png)


4. Create a route table. 
- Route Table: used to determine where network traffic is directed using rules. 
![routetable](https://user-images.githubusercontent.com/77417309/154163174-f8ac1874-0ffb-44a0-a0f1-b2b1faad0bfd.png)
![route](https://user-images.githubusercontent.com/77417309/154163194-efc826b1-5d40-45bc-b990-20789aab2805.png)


5. Create a security group
- Security Groupz: enables you to filter traffic based on protocols and port numbers. 
![securitygroup](https://user-images.githubusercontent.com/77417309/154163226-ef4bf500-9f82-435d-a9f0-8518d5de6cad.png)


6. Did not need a new key pair. 

Part 2 - EC2 Instances


