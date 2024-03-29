# [python.apifunc.com](http://python.apifunc.com)


## Menu

+ [Project](#Project)
+ [References](#References)
+ [Sources](#Sources)
+ [People](#People)
+ [Contribution](#Contribution)
+ [About](#About)
+ [Usage](#Usage)
  + [Start](#Start)
  + [Development](#Development) 


## Project

+ [docs](http://docs.apifunc.com)
+ [www](http://www.apifunc.com)
+ [logo](http://logo.apifunc.com)


## References

+ [apifunc projects](https://github.com/apifunc)
+ [apitee/python: python.apitee.com](https://github.com/apitee/python)


## Sources

+ [How to Run a Python Script using Docker?](https://www.geeksforgeeks.org/how-to-run-a-python-script-using-docker)
+ [dockerfile - How to run Python command in Docker and capture output and](https://stackoverflow.com/questions/62563856/how-to-run-python-command-in-docker-and-capture-output-and-set-it-to-environment)
+ [Build variables | Docker Docs](https://docs.docker.com/build/building/variables)
+ [Docker file for running a Python program with parameters](https://stackoverflow.com/questions/57528713/docker-file-for-running-a-python-program-with-parameters)
+ [How to write a great Dockerfile for Python apps - PyBootcamp](https://www.pybootcamp.com/blog/how-to-write-dockerfile-python-apps)
+ [python - How do I map ports inside the Dockerfile? - Stack Overflow](https://stackoverflow.com/questions/76595802/how-do-i-map-ports-inside-the-dockerfile)
+ [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)


## People

+ [Tom Sapletta - DevOps](http://tom.sapletta.com)


## Contribution

+ [Edit Docs](https://github.com/apifunc/python/edit/main/README.md)
+ [New Issue](https://github.com/apifunc/python/issues/new)



## About

The python script **apifunc** maps Dockerfile variables, instructions, and functions, a Python script that analyzes a Dockerfile and extracts relevant information.

### Parsing Dockerfile Instructions

- The Dockerfile is looking for docker instructions such `FROM`, `RUN`, `ADD`, `ENV`, `ENTRYPOINT`, and `CMD`  line by line
- For each instruction, is extracting the relevant details (e.g., base image, commands, environment variables)

### Mapping Variables and Functions

- That mapping associates each instruction with its corresponding variables and functions.
- For example:
 - `FROM` instruction maps to the base image.
 - `RUN` instruction maps to the commands executed during image build.
 - `ENV` instruction maps to environment variables.
 - `ENTRYPOINT` and `CMD` instructions map to the entry points for running the container.


### Usage

- Replace `"path/to/your/Dockerfile"` with the actual path to your Dockerfile.
- Run the script using `python apifunc.py`.
- It will print out the relevant details for each instruction found in the Dockerfile.

Remember that this script is a starting point, and you can enhance it further based on your specific needs. 
Additionally, consider using existing Dockerfile parsing libraries (e.g., `apifunc`) for more robust solutions.


### Run local as command line

```bash
apifunc build
```

run service local

```bash
apifunc run
```

### Run remote as command line


```bash
apifunc run remote ssh://
```





### Run as a Service

Serve as a service docker swarm, kubernetes, podman, ...
in nginx, caddy, express, 


```bash
apifunc run nginx
```

```bash
apifunc --file Dockerfile run nginx --config nginx.conf
```

run service local

```bash
apifunc serve remote ssh://
```

### Run by Hypervisor

Serve as a virtual service docker swarm, kubernetes, podman, ...

```bash
apifunc run kube
```


```bash
apifunc run docker
```



```bash
apifunc run swarm
```


### Development


```bash
apifunc 
```


```bash
apifunc init
```


```bash
apifunc test
```



```bash
apifunc publish
```


