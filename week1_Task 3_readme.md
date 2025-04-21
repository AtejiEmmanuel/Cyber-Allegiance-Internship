# My Docker Automation Implementation

## Project Overview

I successfully automated my development pipeline by integrating Visual Studio, GitHub, and Docker to create a seamless CI/CD workflow. This documentation outlines the steps I took and the solutions I implemented to eliminate manual deployment processes.

## What I Accomplished

I created an end-to-end automated workflow that:
1. Automatically pushes my code changes from Visual Studio to GitHub
2. Triggers GitHub Actions to build Docker images whenever code is updated
3. Pushes these images to my Docker Hub repository (cref07/cyberallegiance2025-private)
4. Enables easy deployment across any environment

## My Implementation Process

### Step 1: Docker Setup

I created a Docker Hub account and set up both public and private repositories:

- Created an account on [hub.docker.com](https://hub.docker.com/)
- Logged in via terminal using:
  ```bash
  docker login
  ```
- Created my private repository: `cref07/cyberallegiance2025-private`

![Alt text](https://github.com/AtejiEmmanuel/Cyber-Allegiance-Internship-Private/blob/main/Screenshots/Screenshot%202025-04-21%20235054.png?raw=true)

### Step 2: Project Configuration

I created the following configuration files in my project:

1. **Dockerfile**
   
   ```dockerfile
   # Use a lightweight official Python image
   FROM python:3.11-slim
   
   # Create app directory inside container
   WORKDIR /app
   
   # Create a simple Python script
   RUN echo "print('Hello, Docker!')" > app.py
   
   # Run the Python script when the container starts running
   CMD ["python", "app.py"]
   ```

2. **.dockerignore**
   
   ```
   node_modules
   npm-debug.log
   .git
   .gitignore
   README.md
   ```

### Step 3: Building and Testing

I built and tested my Docker image locally before pushing to the repository:

```bash
# Built my image
sudo docker build -t cref07/cyberallegiance2025-private:v0 .

# Ran my containerized app
sudo docker run -p 3000:3000 cref07/cyberallegiance2025-private:v0

# Pushed my image to Docker Hub
sudo docker push cref07/cyberallegiance2025-private:v0
```
![Alt text](https://github.com/AtejiEmmanuel/Cyber-Allegiance-Internship-Private/blob/main/Screenshots/Screenshot%202025-04-22%20000208.png?raw=true)

### Step 4: GitHub Actions Automation

I set up GitHub Actions to automate the building and pushing of Docker images:

1. Created the workflow directory:
   ```bash
   mkdir -p .github/workflows
   ```

2. Created a workflow file (`docker-build.yml`):
   ```yaml
   name: Docker Build and Push
   
   # Trigger on push to main branch
   on:
     push:
       branches: [ main ]
     # Optional: Trigger manually from GitHub interface
     workflow_dispatch:
   
   jobs:
     build-and-push:
       runs-on: ubuntu-latest
       steps:
         # Step 1: Check out the repository code
         - name: Checkout code
           uses: actions/checkout@v3
           
         # Step 2: Set up Docker Buildx
         - name: Set up Docker Buildx
           uses: docker/setup-buildx-action@v2
           
         # Step 3: Login to Docker Hub
         - name: Login to DockerHub
           uses: docker/login-action@v2
           with:
             username: ${{ secrets.DOCKERHUB_USERNAME }}
             password: ${{ secrets.DOCKERHUB_TOKEN }}
             
         # Step 4: Build and push Docker image
         - name: Build and push
           uses: docker/build-push-action@v4
           with:
             context: .
             push: true
             tags: cref07/cyberallegiance2025-private:latest,cref07/cyberallegiance2025-private:v${{ github.run_number }}
             cache-from: type=registry,ref=cref07/cyberallegiance2025-private:latest
             cache-to: type=inline
             build-args: |
               ENV=production
   ```

3. Added my Docker Hub credentials to GitHub repository secrets:
   - DOCKERHUB_USERNAME
   - DOCKERHUB_TOKEN

### Step 5: Final Implementation

I committed and pushed all my changes:

```bash
git add .
git commit -m "Add Docker configuration and GitHub Actions workflow"
git push
```

This triggered my workflow, which successfully built and pushed my Docker image to my repository.

## My Versioning Strategy

For each security improvement (v2, v3, v4):
1. I make code changes in Visual Studio
2. Commit and push to GitHub
3. My GitHub Actions workflow automatically builds and pushes updated Docker images
4. Each version becomes available in my Docker repository with both a version tag and the "latest" tag

## Challenges I Overcame

- Needed to use `sudo` for Docker commands due to permission issues
- Ensured proper configuration of GitHub secrets for secure authentication
- Optimized my Dockerfile to reduce image size and build time

## Results and Benefits

By implementing this automation:
1. I eliminated manual deployment steps
2. My code is consistently packaged with all dependencies
3. Deployment across environments is now consistent and reliable
4. I can easily roll back to previous versions if needed
5. My development workflow is significantly faster

## Future Improvements

I plan to enhance my implementation by:
1. Adding Docker Compose for multi-container applications
2. Implementing automated testing in the CI/CD pipeline
3. Setting up staging environments for pre-production testing

## Resources I Used

- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Hub Documentation](https://docs.docker.com/docker-hub/)
