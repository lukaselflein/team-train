#export FLASK_ENV=development
export ENV_FILE_LOCATION=./.env

python3 -m unittest tests/test_signup.py 
python3 -m unittest tests/test_login.py 
python3 -m unittest tests/test_create_workout.py 

