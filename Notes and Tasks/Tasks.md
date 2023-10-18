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