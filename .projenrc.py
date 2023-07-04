from projen.python import PythonProject

project = PythonProject(
    author_email="h1f1x@users.noreply.github.com",
    author_name="Felix Borchers",
    module_name="aws_secrets_manager",
    name="aws-secrets-manager",
    version="0.1.0",
)

project.synth()