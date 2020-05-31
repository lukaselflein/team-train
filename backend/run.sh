#export FLASK_ENV=development
export PYTHONDONTWRITEBYTECODE=1 

echo 'Entering in test mode...'
export ENV_FILE_LOCATION=./.testenv
#python3 -m unittest tests/test_signup.py 
#python3 -m unittest tests/test_login.py 
python3 -m unittest tests/test_create_workout.py 

echo 'Entering production mode...'
export ENV_FILE_LOCATION=./.env
python3 app.py
