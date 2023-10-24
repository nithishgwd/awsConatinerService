1. docker build -t subscriptionDataVisual:v1 .
2. docker run -d -p 80:80 --name subscriptionDataVisualconatiner subscriptionDataVisual:v1
3. docker login
4. docker tag subscriptionDataVisual:v1 nithishgwd/subscriptionDataVisual:v1
5. docker push nithishgwd/subscriptionDataVisual:v1
6. docker rm -f $(docker ps -aq)
7. docker rmi $(docker images -q)
8. docker ps 
9. docker ps -a
10. docker images



