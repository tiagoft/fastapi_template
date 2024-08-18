# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Running the Project with Docker

```bash
docker build -t {{ cookiecutter.pckg_name }} .
docker run -d -p 9000:8888 {{ cookiecutter.pckg_name }}
```

## Authors

{{ cookiecutter.group_members }}