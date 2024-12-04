import subprocess,json
import time
 
 
def test_Helm_setup():
        list_jobs=subprocess.run(f"curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 
def test_Helm_file():
        list_jobs=subprocess.run(f"chmod 700 get_helm.sh",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 
#./get_helm.sh
 
def test_get_Helm_file():
        list_jobs=subprocess.run(f"#./get_helm.sh",shell=True,capture_output=True)
        time.sleep(5)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
        
 
#helm version
def test_get_Helm_version():
        list_jobs=subprocess.run(f"helm version",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert b'Version:' in list_jobs.stdout
 
# If on Ubuntu:
#sudo apt update -y
def test_ubuntu():
        list_jobs=subprocess.run(f"sudo apt update -y",shell=True,capture_output=True)
        time.sleep(15)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
        
 
# #### Helm Setup
# curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
# chmod 700 get_helm.sh
# ./get_helm.sh
# helm version
 
# ##### If on RHEL, Centos or Amazon Linux:
# sudo yum update -y
# sudo yum install docker -y
# sudo systemctl start docker
# systemctl status docker
# sudo usermod -aG docker $USER && newgrp docker
 
# ##### If on Ubuntu:
# sudo apt update -y
# sudo snap install docker
# sudo snap start docker
 
# sudo su
 
# curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
 
# sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
 
# chmod +x kubectl
 
# mkdir -p ~/.local/bin
 
# mv ./kubectl ~/.local/bin/kubectl
 
# kubectl version
 
# curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
 
# sudo install minikube-linux-amd64 /usr/local/bin/minikube
 
# minikube version
 
# minikube start --force
 
# minikube status
 
def test_instll_docker():
        list_jobs=subprocess.run(f"sudo snap install docker",shell=True,capture_output=True)
        time.sleep(10)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
        
 
def test_start_docker():
        list_jobs=subprocess.run(f"sudo snap start docker",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 
# def test_sudo_su():
#         list_jobs=subprocess.run(f"sudo su",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 
def test_download_binary():
        list_jobs=subprocess.run(f"curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\"",shell=True,capture_output=True)
        time.sleep(10)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
        
 
 
def test_install_kubectl():
        list_jobs=subprocess.run(f"sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 
def test_install_kubectl():
        list_jobs=subprocess.run(f"chmod +x kubectl",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 
def test_create_directory():
        list_jobs=subprocess.run(f"sudo mkdir -p /root/.local/bin",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
def test_move_kubernetes():
        list_jobs=subprocess.run(f"sudo mv ./kubectl /root/.local/bin/kubectl",shell=True,capture_output=True)
        time.sleep(10)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0  
        
 
def test_version_check_kubernetes():
        list_jobs=subprocess.run(f"sudo kubectl version",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert b'Version:' in list_jobs.stdout
 
def test_download_minikube():
        list_jobs=subprocess.run(f"curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 ",shell=True,capture_output=True)
        time.sleep(15)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
        
 
def test_install_kubernetes():
        list_jobs=subprocess.run(f"sudo install minikube-linux-amd64 /usr/local/bin/minikube ",shell=True,capture_output=True)
        time.sleep(3)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0  
          
 
def test_kubernetes_version():
        list_jobs=subprocess.run(f"minikube version",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert list_jobs.returncode==0  
 
def test_kubernetes_start():
        list_jobs=subprocess.run(f"sudo minikube start --force",shell=True,capture_output=True)
        time.sleep(20)
        print( list_jobs.stdout)
        # assert  list_jobs.returncode==0
        
 
def test_kubernetes_status():
        list_jobs=subprocess.run(f"minikube status",shell=True,capture_output=True)
        print( list_jobs.stdout)
        # assert  list_jobs.returncode==0