##Prerequisites
Docker should be installed on your machine. You can download and install Docker Desktop from the official website (https://www.docker.com/products/docker-desktop).

##Updating the Solution
To update the solution, follow these steps:
1. Clone the repository and navigate to the root directory of the project.
`git clone https://github.com/your-username/your-repo.git` 
`cd your-repo`
2. Make the necessary changes to the source code and/or the requirements.txt file.
3. Update the Dockerfile with the appropriate base image, dependencies, and commands as described in the previous section.
4. Save the Dockerfile and commit your changes.
`git add .`
`git commit -m "Updated the solution"`

##Building the Solution
To build the Docker image, follow these steps:
1. Open a terminal and navigate to the root directory of the project.
2. Run the following command to build the Docker image:
`docker build -t my-api .`
This command will build the Docker image from the Dockerfile in the current directory and tag it with the name my-api. Note that the . at the end of the command specifies the build context (i.e., the directory where the Dockerfile and other necessary files are located).
3. After the build process is complete, you can verify that the image was created by running the following command:
`docker images`
This command will list all the Docker images on your machine, including the one you just built.

##Running the Solution
To run the Docker container, follow these steps:
1. Run the following command to start the Docker container:
`docker run -p 8000:8000 my-api`
This command will start the Docker container and map port 8000 from the container to port 8000 on the host machine. You should be able to access the API server by going to http://localhost:8000 in your web browser.
2. If you want to stop the container, you can run the following command:
`docker stop $(docker ps -a -q --filter ancestor=my-api --format="{{.ID}}")`
