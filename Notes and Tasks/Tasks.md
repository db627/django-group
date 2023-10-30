10/18/2023 - Tasks
1. Figure out how to get the Watchtower to work
 - https://containrrr.dev/watchtower/
 - Needed folders 
    - app
    - watchtower (watches our dockerhub repo)
    - github builds image and pushes to dockerhub, watchtower to look
3 folders
1. watchtower
2. myprogram (group dev) does not build just points to image - docker-compose.yml - runs group image that pulls from remote 
    - docker compose needs to point to remote images
// docker push db627/is373-djangoproject:tagname <tagname is just the name of the branch you want to push to>
3. myprogram (local dev) needs to manually build:  folder with dockerfile and docker-compose that builds and pushes- runs local image


1. Take existing dockerfile, create a docker-compose, and push to a dockerhub repo
2. Create a second docker-compose that points to the dockerhum repo image, it needs to use watchtower, that downloads and runs the image
3. SEtup a watchtower and add the label to 2. 

10/20/203
1. Make a github action that builds and push docker image
2. Learn templates and Django ORM
    - setup a master template that has nav, styling, footer on it
    - setup child templates with content
    - Templates: https://docs.djangoproject.com/en/4.2/topics/templates/
    - orm: https://docs.djangoproject.com/en/4.2/topics/db/queries/ 
    - orm: basically writes sql for you 
    - orm: uses sqlalchemy

10/25/2023
1. Generate fake data into the model
2. Make it show up
3. Run testts
1. Generate fake users
    - We need a model scheme for the ORM to make tbales for users
    - Make a thing called a factory
        - A factory basically creates obkects
    - Models vs Database Table
        - For every instance of a model their is a row in a table
    - 3 types of Methods : https://realpython.com/instance-class-and-static-methods-demystified/#:~:text=Instance%20methods%20need%20a%20class,access%20to%20cls%20or%20self%20. 
        - Instance Methods
            - Opposite of Static Methods
            - Operate on the object that has been instantiated
            - Work on models
            - Creates new objects 
            - Know about their data
            - Uses self
        - Class Methods
        - Static Methods
            - Method you call that gets called without needing an object
            - Method that basically just retrieve data
            - Math methods
            - Get data
            - Non object method
        - The difference is what data those methods have access to at any point of time

        - Python: Instance Methods, Class Methods, Static Methods
    - SO Create a User model, another model, and a model factory  "https://refactoring.guru"
    - Create fake data using Faker


    1. A model a factory that generates fake data using Faker when the model is instantiated.
    2. I want a new model with fake data and return back that data with the fake info

    - Create a model
    - Generate the model in a factory
    - Add fake data into it
    - Then use seeds (Database Seeding):
    - A seed is a process that generates fake data
        - Create methods for seeding
        def count(number of records needed)
        def create(0 creaetes the data)
    1. setup ORM and Model
        - Makemigration, Migrate
        - Migrate the model
        - bascially set up schemas but also version control for schema. 
    2. Get your schema with SQL Alchemy
    3. Create a factory using SQL Alchemy
    4. Learn Faker and gernerate Fake Data
    4. Create a seed using SQL Alchemy
    5. Overall: Understand how to make a model, make a model with fake data, and then create x amount of models on demand