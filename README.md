# Intro
The tool build an Flask Endpoint server on Azure VM. And use the azs_heartbeat_monitoring.py to monitor the endpoint and push the events into DataDog.
## Instructions
build and run a container. Dockerfile is included.
```
docker run -it -p 5000:5000 -d --name my-endpoint nickkounz/azure-endpoint:latest
```
Create a secrect file with the line break for Datadog api_key and app_key prior to use the mornitoring script.