# Movie Stats

The first part in this series is to familiarize everyone with basic analytics methods in Python, specifically using Jupyter Notebooks for interactive analysis. The sample dataset we are using is the movies dataset available from Kaggle
(https://www.kaggle.com/rounakbanik/the-movies-dataset/data).

## Installation instructions (~15 minutes)
To ensure everyone is starting off in the same place, we will be using a simple docker container to hold everything we need for this workshop. 

Please follow these instructions below to start up the container:

1. If you don't have a Docker ID account yet, go to [Docker Hub](https://hub.docker.com/) and create an account.

2. Install Docker. On Mac OS X, you can download [Docker for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac) for an easy-to-install desktop app. 

3. Open Docker and enter your Docker Hub credentials.

4. Click on the Docker app icon and select "Preferences...". Under "Advanced", increase the memory available to containers to 8.0 GB.

5. Clone this repository using `git clone`:

```
$ git clone https://github.com/GrGambit/movie_stats.git
```

6. Open a terminal, navigate to the `movie_stats` directory, and run: 
```
$ sh run.sh
``` 
from a terminal to extract the movie dataset and start the Docker container. 


7. You should be able to navigate to **`http://localhost:8889`** with your browser using the refenced key in the command line and see a Jupyter notebook instance. **The password is `spark`.**

8. You can exit the Docker session using `Ctrl+C`.

## Troubleshooting
If step 6 fails with error `unauthorized: incorrect username or password.`, run 

```
$ docker login
```

and enter your DockerHub credentials (username and password; username is _not_ your email).
