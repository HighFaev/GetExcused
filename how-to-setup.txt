#Start up (From folder with Dockerfile file)
1. docker build --no-cache -t getexcused .
2. docker run -d -p 8080:8080 --name getexcused-app getexcused
#Now you can find server by http://localhost:8080 adress

#Stop work
1. docker stop getexcused-app

#Delete container
1. docker rm getexcused-app

#Delete image
1. docker rmi getexcused

