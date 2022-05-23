# project1


# Objective
The objective of the project was: " to create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together." 

The main focus of this project is the deployment of the application.

For this project I should have: 
- Kanban Board: Asana or an equivalent Kanban Board
- Version Control: Git
- CI Server: Jenkins
- Configuration Management: Ansible
- Cloud server: GCP virtual machines
- Containerisation: Docker
- Orchestration Tool: Docker Swarm
- Reverse Proxy: NGINX

# Initial Ideas
I have decided to make a random Star Wars databank entry application. The app should:

-Use service1 as a front end
-Use service2 and service3 to generate a random name and planet, with service2 being the name part and service3 being the planet part.
-Use service4 to generate a databank entry 

# Summary
Once the app was made , I added a Dockerfile into each of the service folders to containerize them and made a docker-compose.yaml, I then made ansible related files (Inventory, playbook.yaml and roles/tasks) these help install docker on the (soon-to-be) swarm nodes and then sets up a swarm. I made a Jenkinsfile with scripts so that jenkins can use that to make a pipeline.


I made 3 new Virtual Machines to work with forr the project: 
- Jenkins
- Manager
- Worker
- NGINX

On the Jenkins machine, I used a script to install Jenkins. Next, I used sudo visudo to give Jenkins sudo permissions. As the jenkins user, I installed docker and docker-compose, then generated keys using ssh-keygen -t rsa. I copied and pasted the public key from the jenkins user on the jenkins machine into the Manager and Worker VMs. Once the other two (Manager, Worker) machines where created I used the jenkins machine to ssh into them. Then through the jenkins app on port 8080 I set up a webhook for my git repository and enabled it on git, this allows for a rolling update. 

# GCP
I first spun up a virtual machine on GCP with the purpose of creating the app, placing my local machines public key in, I then SSH through VSC to my VM and clone this GIT repository and create services. Once all the services are complete and the app is working successfully push to Github. I then create a new VM to be my jenkins machine.
