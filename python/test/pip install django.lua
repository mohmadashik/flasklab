pip install django 
djangoadmin startproject mysite
manage.py 
-- settings.py --- database changes settings of the project, we will be adding app in the installed apps
-- urls.py -- we will add the respective app paths in the url 
etc 
djangoadmin startapp some_app 

inside the app folder 
we have urls.py 
    inside this we will be adding the app oriented paths
    views.py 
        in this views.py we will add the view functions for the urls given urls.py of the app 
    
    static folder - html,images,javascript

AWS EC2,S3,Lambda,API gateway, IAM cloud9

first we write the code in module
and we zip it 
we create requirements files for the packages we are gonna use in the code we are going to upload to the lambda
after that we update the lambda code 
we update the requirements file 
finally we install the requirements

docker images and build docker container 
it is like a separate os with the perfect requirements 

select name from user;
select u.name,o.date from user u join order o on u.id = o.id where u.id>20;
select avg(marks) as avg_marks,section from class group by section;

section a,b,c 
a- 50,50,60,80
b - 70,80,100,20
c - 77, 67,45,20


ros, AWS IOT,