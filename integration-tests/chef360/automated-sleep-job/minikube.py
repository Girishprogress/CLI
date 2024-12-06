import subprocess,json
import time
import os 
 
# def test_Helm_setup():
#         list_jobs=subprocess.run(f"curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 
# def test_Helm_file():
#         list_jobs=subprocess.run(f"chmod 700 get_helm.sh",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 
# #./get_helm.sh
 
# def test_get_Helm_file():
#         list_jobs=subprocess.run(f"#./get_helm.sh",shell=True,capture_output=True)
#         time.sleep(5)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
        
 
# #helm version
# def test_get_Helm_version():
#         list_jobs=subprocess.run(f"helm version",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert b'Version:' in list_jobs.stdout
 
# # If on Ubuntu:
# #sudo apt update -y
# def test_ubuntu():
#         list_jobs=subprocess.run(f"sudo apt update -y",shell=True,capture_output=True)
#         time.sleep(15)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
        
 
# # #### Helm Setup
# # curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
# # chmod 700 get_helm.sh
# # ./get_helm.sh
# # helm version
 
# # ##### If on RHEL, Centos or Amazon Linux:
# # sudo yum update -y
# # sudo yum install docker -y
# # sudo systemctl start docker
# # systemctl status docker
# # sudo usermod -aG docker $USER && newgrp docker
 
# # ##### If on Ubuntu:
# # sudo apt update -y
# # sudo snap install docker
# # sudo snap start docker
from configparser import ConfigParser
 
# # sudo su
 
# # curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
 
# # sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
 
# # chmod +x kubectl
 
# # mkdir -p ~/.local/bin
 
# # mv ./kubectl ~/.local/bin/kubectl
 
# # kubectl version
 
# # curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
 
# # sudo install minikube-linux-amd64 /usr/local/bin/minikube
 
# # minikube version
 
# # minikube start --force
 
# # minikube status
 
# def test_instll_docker():
#         list_jobs=subprocess.run(f"sudo snap install docker",shell=True,capture_output=True)
#         time.sleep(10)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
        
 
# def test_start_docker():
#         list_jobs=subprocess.run(f"sudo snap start docker",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 
# # def test_sudo_su():
# #         list_jobs=subprocess.run(f"sudo su",shell=True,capture_output=True)
# #         print( list_jobs.stdout)
# #         assert  list_jobs.returncode==0
 
# def test_download_binary():
#         list_jobs=subprocess.run(f"curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\"",shell=True,capture_output=True)
#         time.sleep(10)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
        
 
 
# def test_install_kubectl():
#         list_jobs=subprocess.run(f"sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 
# def test_install_kubectl():
#         list_jobs=subprocess.run(f"chmod +x kubectl",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 
# def test_create_directory():
#         list_jobs=subprocess.run(f"sudo mkdir -p /root/.local/bin",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
# def test_move_kubernetes():
#         list_jobs=subprocess.run(f"sudo mv ./kubectl /root/.local/bin/kubectl",shell=True,capture_output=True)
#         time.sleep(10)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0  
        
 
# def test_version_check_kubernetes():
#         list_jobs=subprocess.run(f"sudo kubectl version",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert b'Version:' in list_jobs.stdout
 
# def test_download_minikube():
#         list_jobs=subprocess.run(f"curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 ",shell=True,capture_output=True)
#         time.sleep(15)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
        
 
# def test_install_kubernetes():
#         list_jobs=subprocess.run(f"sudo install minikube-linux-amd64 /usr/local/bin/minikube ",shell=True,capture_output=True)
#         time.sleep(3)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0  
          
 
# def test_kubernetes_version():
#         list_jobs=subprocess.run(f"minikube version",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert list_jobs.returncode==0  
 
# def test_kubernetes_start():
#         list_jobs=subprocess.run(f"sudo minikube start --force",shell=True,capture_output=True)
#         time.sleep(20)
#         print( list_jobs.stdout)
#         # assert  list_jobs.returncode==0
        
 
# def test_kubernetes_status():
#         list_jobs=subprocess.run(f"minikube status",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         # assert  list_jobs.returncode==0


# # yes \"y\" | sudo apt install awscli
# def test_install_awscli():
#         print(19)
#         list_jobs=subprocess.run(f"yes \"y\" | sudo apt install awscli",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 
 
# def test_awscli():
#         print(19)
#         list_jobs=subprocess.run(f"aws --version",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 
 
 
# def test_get_access_keys(get_env_variables, monkeypatch):
#     print(20)  
#     # Set environment variables using monkeypatch
#     monkeypatch.setenv("AWS_ACCESS_KEY_ID", get_env_variables["AWS_ACCESS_KEY_ID"])
#     monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", get_env_variables["AWS_SECRET_ACCESS_KEY"])
#     monkeypatch.setenv("AWS_SESSION_TOKEN", get_env_variables["AWS_SESSION_TOKEN"])
 
#     # Fetch environment variables
#     AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
#     AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
#     AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
 
#     # Print for debugging
#     print("AWS_ACCESS_KEY_ID:", AWS_ACCESS_KEY_ID)
#     print("AWS_SECRET_ACCESS_KEY:", AWS_SECRET_ACCESS_KEY)
#     print("AWS_SESSION_TOKEN:", AWS_SESSION_TOKEN)
 
 
#     list_jobs=subprocess.run(f"mkdir -p ~/.aws",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
    
#     list_jobs=subprocess.run(f"echo \"[default]\" > ~/.aws/credentials",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
 
#     cmd1="echo \"aws_access_key_id=\" "+AWS_ACCESS_KEY_ID+" >> ~/.aws/credentials"
#     list_jobs=subprocess.run(cmd1,shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
 
#     cmd2="echo \"aws_secret_access_key=\" "+AWS_SECRET_ACCESS_KEY+" >> ~/.aws/credentials"
#     list_jobs=subprocess.run(cmd2,shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
 
#     aws_access_key_id = AWS_ACCESS_KEY_ID
#     aws_secret_access_key = AWS_SECRET_ACCESS_KEY
#     aws_session_token = AWS_SESSION_TOKEN
 
#     # AWS credentials file path
#     credentials_file = os.path.expanduser("~/.aws/credentials")
#     config_file = os.path.expanduser("~/.aws/config")
 
#     #  Create config parser for credentials file
#     credentials = ConfigParser()
#     credentials.read(credentials_file)
 
#     # Set credentials under the default profile
#     if not credentials.has_section('default'):
#         credentials.add_section('default')
#     credentials.set('default', 'aws_access_key_id', aws_access_key_id)
#     credentials.set('default', 'aws_secret_access_key', aws_secret_access_key)
#     credentials.set('default', 'aws_session_token', aws_session_token)
 
#     # Write the updated credentials file
#     with open(credentials_file, 'w') as f:
#         credentials.write(f)
 
#     # Create config file for region
#     config = ConfigParser()
#     config.read(config_file)
 
#     # Set the region under the default profile
#     if not config.has_section('default'):
#         config.add_section('default')
#     config.set('default', 'session_token', aws_session_token)
 
#     # Write the updated config file
#     with open(config_file, 'w') as f:
#         config.write(f)
 
#     print("AWS credentials and config files have been updated.")

#kubectl create secret docker-registry regcred  --docker-server=448877188565.dkr.ecr.us-east-2.amazonaws.com   --docker-username=AWS   --docker-password=$(aws ecr get-login-password --region us-east-2)
# def test_create_image_secret():
#     print(19)
#     list_jobs=subprocess.run(f"sudo kubectl create secret docker-registry regcred  --docker-server=448877188565.dkr.ecr.us-east-2.amazonaws.com   --docker-username=AWS   --docker-password=$(aws ecr get-login-password --region us-east-2)",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0


#sudo apt install git -y
# def test_create_image_secret():
#     print(19)
#     list_jobs=subprocess.run(f"sudo apt install git -y",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0

# #git clone git@github.com:progress-platform-services/helm.git
# def test_clone():
#     print(19)
#     list_jobs=subprocess.run(f"git clone git@github.com:progress-platform-services/helm.git",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0

#cd helm/chef-platform
# def test_helm_setup():
#     print(19)
#     list_jobs=subprocess.run(f"cd helm/chef-platform",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
# #sed -i 's/tenant-1.dev-360.chef.co/ec2-3-94-190-118.compute-1.amazonaws.com/g' values.yaml
# x=input("enter the dns")
# def test_helm_deploy():
#     print(19)
#     list_jobs=subprocess.run(f"sed -i 's/ec2-3-94-190-118.compute-1.amazonaws.com/{x}/g' helm/chef-platform/values.yaml",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
#     #ec2-3-94-190-118.compute-1.amazonaws.com

#sudo helm install chef-platform .
# def test_helm_setup_install():
#     print(19)
#     list_jobs=subprocess.run(f"sudo helm install chef-platform helm/chef-platform",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
#sudo nohup kubectl port-forward --namespace default service/nginx-reverse-proxy --address 0.0.0.0 31000:8080 &
# def test_helm_setup_install():
#     print(19)
#     list_jobs=subprocess.run(f"sudo nohup kubectl port-forward --namespace default service/nginx-reverse-proxy --address 0.0.0.0 31000:8080 &",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0

#sudo nohup kubectl port-forward --namespace default service/chef-platform-rabbitmq --address 0.0.0.0 31050:5672 &
def test_helm_setup_install():
    print(19)
    list_jobs=subprocess.run(f"sudo nohup kubectl port-forward --namespace default service/chef-platform-rabbitmq --address 0.0.0.0 31050:5672 &",shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0
def test_helm_setup_install1():
    print(19)
    list_jobs=subprocess.run(f"sudo nohup kubectl port-forward --namespace default service/mailpit --address 0.0.0.0 31100:8025 &",shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0




