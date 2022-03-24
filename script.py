import os
import paramiko

from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST")
user = os.getenv("USERNAME")  
repo = os.getenv("REPO_NAME")  
ecr = os.getenv("ECR_URL")  
region = os.getenv("AWS_DEFAULT_REGION")  
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
access_key = os.getenv("AWS_ACCESS_KEY_ID")

commands = f'''
export AWS_ACCESS_KEY_ID={access_key}
export AWS_SECRET_ACCESS_KEY={secret_key}
export AWS_DEFAULT_REGION={region}
aws ecr get-login-password --region {region} | sudo docker login --username AWS --password-stdin {ecr}
sudo yum -y install docker
sudo service docker start
sudo docker run -p 80:80 -d {ecr}/{repo}:v1
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_DEFAULT_REGION
'''

os.system(f"docker build . -t {ecr}/{repo}:v1")
os.system(f"aws ecr get-login-password --region {region} | docker login --username AWS --password-stdin {ecr}")
os.system(f"docker push {ecr}/{repo}:v1")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname=host, username=user)
    
    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(commands,get_pty=True)
    print(ssh_stdout.read().decode())
    err = ssh_stderr.read().decode()
    if err:
        print(err)
    client.close()

except Exception as e:
    print(f"Cannot connect to the SSH Server\n Exception: {str(e)}")

