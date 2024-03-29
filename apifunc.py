# apifunc.py 
def apifunc(dockerfile_path):
    instruction_mapping = {
        "FROM": "Base image",
        "RUN": "Commands",
        "ADD": "File additions",
        "ENV": "Environment variables",
        "ENTRYPOINT": "Entry point",
        "CMD": "Default command",
    }

    with open(dockerfile_path, "r") as f:
        for line in f:
            tokens = line.strip().split(maxsplit=1)
            if tokens:
                instruction = tokens[0]
                if instruction in instruction_mapping:
                    details = tokens[1] if len(tokens) > 1 else ""
                    print(f"{instruction_mapping[instruction]}: {details}")

if __name__ == "__main__":
    dockerfile_path = "Dockerfile"
    parse_dockerfile(dockerfile_path)
