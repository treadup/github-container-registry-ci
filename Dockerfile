# Build argument specifying the version of the dependency
# docker image that should be used to build this image.
ARG DEPS_VERSION=latest

# Base this image on the dependency docker image that was
# built earlier.
FROM github-container-registry-ci-dependencies:${DEPS_VERSION}

# Set working directory
WORKDIR /app

# Copy over the project
COPY . .

# Run the django development server
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
