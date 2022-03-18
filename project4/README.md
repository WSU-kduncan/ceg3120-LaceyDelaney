
## Part 2 - Setup Load Balancing TODOs

Setup the following and add documentation or screenshots to your `README.md` file as specified.

1. Create an `/etc/hosts` OR `.ssh/config` file on each system that correlates hostnames to private IPs.
   - Description of how file is configured
   
![image](https://user-images.githubusercontent.com/77417309/158945321-4fdd60fd-6f3f-4dc3-a6c6-4796d67fb8bf.png)
  
Commands used: sudo nano /etc/hosts 
(CTRL,X,Y) save & quit in nano 

2. Document how to SSH in between the systems utilizing their private IPs.
- To SSH in between the systems utilizing their private IPs you need to first copy your key over to the proxy server and change permissions. Then use the following commands below to ssh into the systems. 

commands used: ssh -i ceg3120-aws-vm.pem ubuntu@privateIP 


3. **_HAProxy configuration & documentation requirements_**
   - How to set up a HAProxy load balancer
     - What file(s) where modified & their location
      -/etc/haproxy/haproxy.cfg

     - What configuration(s) were set (if any)
     
        - ![image](https://user-images.githubusercontent.com/77417309/159046435-fb068062-da05-4ee1-8f17-be6366df3a73.png)

     - How to restart the service after a configuration change
     
     - Resources used (websites)
4. **_Webserver 1 & 2 configuration & documentation requirements_**
   - How set up a webserver
     - What file(s) were modified & their location
     - What configuration(s) were set (if any)
     - Where site content files were located (and why)
     - How to restart the service after a configuration change
     - Resources used (websites)
5. From the browser, when connecting to the proxy server, take two screenshots.
   - one screenshot that shows content from "server 1"
   - one screenshot that shows content from "server 2"
6. (Optional) - link to your proxy so I can click it.

## Resources and Warnings

- You **DO NOT** need to mess with UFW rules. You may lock yourself out of SSH access.
- You can have a maximum of **FIVE Elastic IP Addresses and FIVE VPCs**
- To manage resources & keep costs down, you will need to delete your CloudFormation stack in between build & test
- Note: feel free to share additional resources over in Discord. I'll be updating this if I see you guys sharing something useful
- [An Introduction to HAProxy and Load Balancing Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [The Four Essential Sections of an HAProxy Configuration](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- [How to Install the Apache Web Server on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)
- [How to Install Nginx on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)
- [How to edit /etc/hosts](https://linuxize.com/post/how-to-edit-your-hosts-file/)
- [The SSH config file](https://linuxize.com/post/using-the-ssh-config-file/)
- [How to SFTP](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course  
   repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

   - Your repo should contain:
   - `YOURLASTNAME-cf.yml`
   - `README.md`

2. In Pilot, paste the link to your project folder.  
   Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project4

