# How to Run
To start this web streamlt application, first you will have to git clone this github repository into your local computer.


# Run the streamlit app using docker:
## Install Docker Desktop:
### Windows 10/11 and macOS
If you haven't installed Docker Desktop, you can download it from the [Docker website](https://docs.docker.com/desktop/install/windows-install/).

### run the Docker Container
To run the docker container you will have to enter the following command on the terminal:
```
docker run -p 8501:8501 ml-streamlit-app
```

### Open your app in your browser
To run your app in your browser will have to enter the following URL:
```
127.0.0.1:8501
```
and NOT the Network - External URL that the docker is showing.


## Run the streamlit app using a python virtual environment (instead of docker)

### Verify Python installation
First, you would need to have installed python3+ version into your system and can check your python version with the command below:
```
    python -V
```
After you successfully installed python you would need to create and activate a virtual environment to run the streamlit application.

### Create venv
To create a new virtual environment you will have to run the command below into your command prompt or terminal:
```
    python -m venv virtual_environment_name
```
### Activate venv
The python virtual environment activation command is different for every system: 
#### Ubuntu debian command
For linux / debian terminal:
```
    source ./virtual_environment_name/bin/activate
```
#### Windows 10/11 command
For windows command prompt:
```
    .\virtual_environment_name\Scipts\activate
```
