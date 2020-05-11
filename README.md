# Sports Training in teams

This project is meant to help coordination and motivation in sports teams.
All team members can complete custom-tailored workout plans to claim points, and increase their highscore for bragging rights.


## Want to use this project?

1. Fork/Clone
    ```git clone https://github.com/lukaselflein/team-train```

1. Install basics

    We need a python interpreter for the backend, a mongodb server for data storage and npm for the frontend: 
    ``` sh
    apt-get install python3
    apt-get install mongodb-server    
    apt-get install npm    
    ```

1. Install & run the backend

    Tell the mongodb server which database to use, set a passphrase, and install python packages
    ```sh
    $ cd backend 
    $ echo "JWT_SECRET_KEY='verysecret'" > .env
    $ echo "MONGODB_SETTINGS={'host': 'mongodb://localhost/team_train_db'}" >> .env
    $ export ENV_FILE_LOCATION=.env
    $ python3 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    ```
    Run the backend server
    ```sh
    $ cd backend     
    $ source env/bin/activate    
    (env)$ python app.py
    ```
    Navigate to [http://localhost:5000/api/workouts](http://localhost:5000/api/workouts) on your browser

1. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client
    $ npm install
    $ npm run serve
    ```

    Navigate to [http://localhost:8080](http://localhost:8080)

# How to start
``` bash
mongod --dbpath ./backend/
python ./backend/env/app.py
cd ./frontend
npm run serve
```

# Contributors
* Olga - Frontend
* Lu - Backend
* Linus - Concepts
