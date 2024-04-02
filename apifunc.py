# apifunc.py
import os
import subprocess
import shlex

# Mapping of Docker commands to shell commands
docker_to_shell_mapping = {
    "FROM": "FROM",
    "RUN": "RUN",
    "CMD": "CMD",
    "LABEL": "LABEL",
    "EXPOSE": "EXPOSE",
    "ENV": "ENV",
    "ADD": "ADD",
    "COPY": "COPY",
    "ENTRYPOINT": "ENTRYPOINT",
    "VOLUME": "VOLUME",
    "USER": "USER",
    "WORKDIR": "WORKDIR",
    "ARG": "ARG",
    "ONBUILD": "ONBUILD",
    "STOPSIGNAL": "STOPSIGNAL",
    "HEALTHCHECK": "HEALTHCHECK",
    "SHELL": "SHELL",
}
info_mapping = {
    "FROM": "FROM",  # No change
    "RUN": "RUN",
    "CMD": "CMD",
    "LABEL": "LABEL",
    "EXPOSE": "EXPOSE",
    "ENV": "ENV",
    "ADD": "ADD",
    "COPY": "COPY",
    "ENTRYPOINT": "ENTRYPOINT",
    "VOLUME": "VOLUME",
    "USER": "USER",
    "WORKDIR": "WORKDIR",
    "ARG": "ARG",
    "ONBUILD": "ONBUILD",
    "STOPSIGNAL": "STOPSIGNAL",
    "HEALTHCHECK": "HEALTHCHECK",
    "SHELL": "SHELL",
}

instruction_mapping = {
    "FROM": "echo",
    "RUN": "bash",
    "ADD": "cp",
    "ENV": "echo",
    "ENTRYPOINT": "echo",
    "CMD": "echo",
    "WORKDIR": "mkdir -p",

}

# Example usage: Get the corresponding shell command for a Docker command
#docker_command = "RUN"
#shell_command = docker_to_shell_mapping.get(docker_command, "Unknown")
#print(f"Shell command for '{docker_command}': {shell_command}")


def run_command(config, command, *args):
    """
    Run a Docker command with the specified arguments.

    Args:
        command (str): The Docker command (e.g., "run", "build", "exec").
        args (str): Additional arguments for the command.

    Returns:
        str: Output of the Docker command.
    """
    if len(command) < 2:
        return "No command specified"

    #docker_cmd = f"docker {command} {' '.join(shlex.quote(arg) for arg in args)}"
    shell_cmd = f"{command + ' ' + ' '.join(shlex.quote(arg) for arg in args)}"


    if len(config) and len(config['WORKDIR']):
        shell_cmd = f"cd {config['WORKDIR']} && {shell_cmd}"

    if command.startswith("bash"):
        #shell_cmd = ' '.join(shlex.quote(arg) for arg in args)
        shell_cmd = args[0]



    print("command", command)
    print("shell_cmd", shell_cmd)
    print("args[0]", args[0])
    #return shell_cmd

    try:
        if command.startswith("mkdir"):
            config['WORKDIR'] = str(args[0])[1:]
            print(config['WORKDIR'])
            shell_cmd = f"{command + ' ' + str(args[0])[1:]}"
            print(shell_cmd)


        result = subprocess.run(shell_cmd, shell=True, capture_output=True, text=True, check=True)
        #result = subprocess.run(docker_cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing Docker command: {e}"


# Example usage
def tests():
    # Equivalent to: docker run -d -p 8080:80 my_image
    run_command("run", "-d", "-p", "8080:80", "my_image")

    # Equivalent to: docker build -t my_image /path/to/Dockerfile
    run_command("build", "-t", "my_image", "/path/to/Dockerfile")

    # Equivalent to: docker exec -it my_container ls
    run_command("exec", "-it", "my_container", "ls")




def apifunc(dockerfile_path):
    config = {}

    # if file not exist show error
    if not os.path.isfile(dockerfile_path):
        print(f"File {dockerfile_path} does not exist")
        exit(1)

    # if file has less than 2 lines show error
    with open(dockerfile_path, "r") as f:
        lines = f.readlines()
        if len(lines) < 2:
            print(f"File {dockerfile_path} has less than 2 lines")
            exit(1)


    # open dockerfile
    with open(dockerfile_path, "r") as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line.startswith("#") or stripped_line.startswith("//"):
                continue

            tokens = stripped_line.split(maxsplit=1)
            if tokens:
                instruction = tokens[0]
                if instruction in info_mapping:
                    details = tokens[1] if len(tokens) > 1 else ""
                    #print(f"{info_mapping[instruction]}: {details}")


                if instruction in instruction_mapping:
                    details = tokens[1] if len(tokens) > 1 else ""
                    # run_docker_command( instruction, details)
                    result = run_command(config, instruction_mapping[instruction], details)
                    print(f"{instruction_mapping[instruction]}: {result}")

    print(config)

"""
Create object with mapping for command from docker to shell command run shell script build mapping between docker commands and shell or python comands to build environment baesd on docker configuration in python
{
    "FROM": "FROM", 
    "RUN": "RUN",
    "CMD": "CMD",
    "LABEL": "LABEL",
    "EXPOSE": "EXPOSE",
    "ENV": "ENV",
    "ADD": "ADD",
    "COPY": "COPY",
    "ENTRYPOINT": "ENTRYPOINT",
    "VOLUME": "VOLUME",
    "USER": "USER",
    "WORKDIR": "WORKDIR",
    "ARG": "ARG",
    "ONBUILD": "ONBUILD",
    "STOPSIGNAL": "STOPSIGNAL",
    "HEALTHCHECK": "HEALTHCHECK",
    "SHELL": "SHELL",
}


write example dockerfile with cloning git repository for python scirpt and run him by entrypoint
"""

if __name__ == "__main__":
    dockerfile_path = "Dockerfile"
    apifunc(dockerfile_path)


# python apifunc.py
