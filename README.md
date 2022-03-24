# Flask Application Using Docker


##### Prerequisites

1. Python3
2. Docker
3. paramiko
4. dotenv
5. awscli

##### To run on local machine

1. Clone the GitHub repo and install the prerequisites on local machine.

2. Update the environment variables in .env file.

3. Navigate to root of the project and run the python script
```sh
python3 script.py
```

4. Check the docker image pushed in ecr.

5. Login to the server and check if the docker container is running or not.
```sh
docker ps
```

6. Now open 80 port in security group of that instance.

7. Open the ip of ec2 instance at 80 port in the browser.

