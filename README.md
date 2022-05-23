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

On the Jenkins machine, I used a script to install Jenkins. Once that was complete and set up, I gave jenkins sudo permissions by using sudo visudo and as the jenkins user I installed docker and docker-compose, still as the jenkins user I then generated keys using ssh-keygen -t rsa. I then placed the public key from the jenkins user on the jenkins machine into the Manager and Worker VMs. Once the other two (Manager, Worker) machines where created I used the jenkins machine to ssh into them. I also, still as the jenkins user, did docker login to provide my dockerhub username and password. Then through the jenkins app on port 8080 I set up a webhook for my git repository and enabled it on git, this allows for a rolling update. 
