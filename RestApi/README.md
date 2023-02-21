techstack:
docker
flask
mongodb

steps:

https://ishmeet1995.medium.com/how-to-create-restful-crud-api-with-python-flask-mongodb-and-docker-8f6ccb73c5bc

<!-- check version of docker -->
docker -v
<!-- pull mongo image  -->
sudo docker pull mongo
<!-- we have our image now we need to run it.  we need to create a container.  -->
sudo docker create -it --name MongoTest -p 5000:27017 mongo
<!-- start the container -->
docker start MongoTest
<!-- check your application will be running at  -->
http://localhost:5000/
<!-- install requirements -->
pip install flask 
pip install pymongo

<!-- create app.py  -->


