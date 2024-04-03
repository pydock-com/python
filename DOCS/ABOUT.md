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


### Conclusion


dsl python connection between url by rest



