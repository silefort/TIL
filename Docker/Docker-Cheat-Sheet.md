# Docker Cheat Sheet

## Working with Docker Containers

    $ docker create [IMAGE_NAME] 				# Creating a Container
    $ docker run [IMAGE_NAME]  					# Creating and Running a Container
    $ docker start [CONTAINER_NAME] 		# Starting a Stopped Container
    $ docker stop [CONTAINER_NAME] 			# Stopping a Running Container
    $ docker restart [CONTAINER_NAME] 	# Restarting a Running Container
    $ docker pause [CONTAINER_NAME] 		# Pausing a Running Container
    $ docker unpause [CONTAINER_NAME] 	#Resuming a Paused Container
    $ docker ps or docker container ls 	# List Running Containers
    $ docker rm [CONTAINER_NAME] 				# Removing a Container

## Working with Docker Container Images

    $ docker build -f [DOCKERFILE_PATH] # Building an Image from a Dockerfile
    $ docker commit [CONTAINER_NAME] [IMAGE_NAME] # Building an Image from a Container
    $ docker image pull [IMAGE_NAME] # Pulling an Image from the Docker Hub
    $ docker login && docker image push [IMAGE_NAME] # Pushing an Image to the Docker Hub
    $ docker image ls or docker image  # List Container Images
    $ docker image remove [IMAGE_NAME] #Deleting an Image from your System

## Working with Docker Volumes

    $ docker volume create [VOLUME_NAME]  # Create a Docker Volume
    $ docker volume rm [VOLUME_NAME]      # Remove a Docker Volume
    $ docker volume inspect [VOLUME_NAME] # Inspect a Docker Volume
    $ docker volume ls                    # List all Docker Volumes

## Working with Docker Networks

    $ docker network create [NETWORK_NAME]                      # Creating a Docker Network
    $ docker network connect [NETWORK_NAME] [CONTAINER_NAME]    # Connecting a Container to a Network
    $ docker network disconnect [NETWORK_NAME] [CONTAINER_NAME] # Disconnecting a Container from a Network
    $ docker network inspect [NETWORK_NAME]                     # Inspecting a Network
    $ docker network ls                                         # Listing all Networks
    $ docker network rm [NETWORK_NAME]                          # Removing a Network
