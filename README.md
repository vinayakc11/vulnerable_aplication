To host the application, follow the steps below:

1. Install python

2. Open cmd and run "pip install flask"

3. Now go to the project repo and run "python app.py"

4. check the URL : http://localhost:5000/



#######################################
######## DOCKER ######################
#######################################


## Run with Docker

git clone https://github.com/vinayakc11/vulnerable_application.git
cd vulnerable_application

docker build -t vulnerable-app .
docker run -p 5000:5000 vulnerable-app

Open:
http://localhost:5000
