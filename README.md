# prism installer
This release is an internal release for testing. It has been streamlined to facilitate the validation of each component of the installer by the original dev team. Once each component has been validated, a more complete release will be made available. This release does not use the full installer script as that is not the scope of this testing, this release is explicitly designed for validating each component. 


## What you’ll need:

+ A clean computer that has not been used for any development of any PRISM components
+ 10GB of free memory
+ 20GB of free disk space
+ At least 4 CPUs available for minikube to use
+ Internet connection
+ [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) (if running Windows)
+ [Docker](https://minikube.sigs.k8s.io/docs/drivers/docker/)
+ If using WSL then follow [these instructions](https://docs.docker.com/desktop/windows/wsl/#download) to configure Docker with WSL
+ [minikube](https://minikube.sigs.k8s.io/docs/start/)
+ **Incognito Browser Window**



## How to test the components
+ If you don't already have Docker installed on your machine then download Docker (if using on Windows then follow the steps to get WSL and Docker working together which was posted above) and make sure that you change the max resource settings (located under options) to at least 4 CPUs and 10GB of RAM
+ Download minikube using the correct release for your OS
+ Download a copy of this repo
+ Start a minikube cluster using one of the following command: `minikube start --driver=docker --memory=max --cpus=max` or `minikube start --driver=docker --memory=10gb --cpus=4`
+ Change directories to the parent repo directory and run `make apply`
+ Once **ALL** the containers are running and ready (you can check them using `while :; do kubectl get all; sleep 30; done`), run `kubectl rollout restart -n default deployment web`
+ If you need to load in data to test the complete functionality of your tool, please see the instructions in the readme located in the **sample_data** directory of this repo
+ Then run `make serve` 
+ Open an **incognito** browser window and navigate to http://127.0.0.1.nip.io:8080/
+ Using the landing page navigate to your component and test the functionality


## Supported OS and Architecture
+ Windows 10 (using Windows Subsystem for Linux)
+ MacOS x86-64 (Intel based Macs)
+ Linux x86-64
