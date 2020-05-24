#export FLASK_ENV=development
export ENV_FILE_LOCATION=./.env
export PYTHONDONTWRITEBYTECODE=1 

#python3 -m unittest tests/test_signup.py 
#python3 -m unittest tests/test_login.py 
python3 -m unittest tests/test_create_workout.py 

echo 'starting server...'
python3 app.py
