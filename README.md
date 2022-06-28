# prism installer
This release is an internal release for **testing**. It has been streamlined to facilitate the validation of each component of the installer by the original dev team. Once each component has been validated, a more complete release will be made available for further testing. This release does not use the full installer script as that is not the scope of this testing. **This release is explicitly designed for validating each component.**


## What you’ll need:

+ A clean computer that has not been used for any development of any PRISM components
+ 10GB of free memory
+ 30GB of free disk space
+ At least 4 CPUs available for minikube to use
+ Internet connection
+ [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) (if running Windows)
+ [Docker](https://minikube.sigs.k8s.io/docs/drivers/docker/)
+ If using WSL then follow [these instructions](https://docs.docker.com/desktop/windows/wsl/#download) to configure Docker with WSL
+ wget
+ python3



## How to install PRISM
+ If you don't already have Docker installed on your test machine then download Docker (if using on Windows then follow the steps to get WSL and Docker working together which was posted above) and make sure that you change the max resource settings (located under preferences > resources) to at least 4 CPUs and 10GB of RAM
+ navigate to the directory you want to use to install PRISM
+ run prism_installer_v1_final.py and answer the questions when prompted
+ After prism_installer_v1_final.py exits, open two new terminal windows and run `python tunnel.py` in one terminal window and run `python portforward.py` in the other terminal window. These terminal windows must remain open for the PRISM instance to function correctly. 
+ Open an **incognito** browser window and navigate to http://127.0.0.1.nip.io:8181/
+ Using the landing page navigate to your component and test the functionality


## Supported OS and Architecture
+ Windows 10 (using Windows Subsystem for Linux)
+ MacOS x86-64 (Intel based Macs)
+ Linux x86-64
