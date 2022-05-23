docker build -t Service1 Service1/application
docker build -t Service2 Service2/application
docker build -t Service3 Service3/application
docker build -t Service4 Service4/application

docker network create servicenenetwork

docker run -d -p 5000:5000 --network servicenetwork --name Service1 Service1
docker run -d -p 5001:5001 --network servicenetwork --name Service2 Service2
docker run -d -p 5002:5002 --network servicenetwork --name Service3 Service3
docker run -d -p 5003:5003 --network servicenetwork --name Service4 Service4