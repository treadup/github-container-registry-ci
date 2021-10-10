# GitHub Container Registry CI
This project demonstrates how to create a Docker image using GihHub CI and
uploading it to the GitHub container registry.

## Build strategy
The build strategy will be to create two Docker images. On the base image
os packages and python dependencies will be installed.

The app image will be based on the base image. On the app image we will install
the Django application.

The goal should be to rebuild the base image only when the python dependencies
change.
