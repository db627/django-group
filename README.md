# django-group

Names:
1. Dennis B
2. Elizabeth
3. Bovan

Important Commands:
1. pip3 install -r requirements.txt
2. cd <folder name>
3. docker compose up : runs docker-compose.yml
4. docker-compose build : builds the docker-compose image
5. docker tag <image name> db627/is373-djangoproject
6. docker push db627/is373-djangoproject
7. python manage.py runserver
8. to locally build
    - 
    - cd myapp
    - docker build -t <builname> .
    - docker run -p 8000:8000 <buildname>
9. to push local image:
    - start by running step 8
    - then in new terminal run docker ps
    - then run docker tag <imagename> db627/is373-djangoproject
    - then run docker push db627/is373-djangoproject

10. To seed
    - python manage.py seed --users=200 --courses=80 
    or 
    - python manage.py seed
11. To check
    1. python manage.py shell
    2. from myapp.models import User, Course
 	    users = User.objects.all()
 	    for user in users:
            print(user.first_name, user.last_name)
        courses = Course.objects.all()
 	    for course in courses:
 		    print(course.course_name, course.course_section)
Important Notes:
1. # myapp
    - development folder
2. # production
    - folder that points to docker hub
3. # watchtower
    - watchtower that monitors docker hub image for changes
