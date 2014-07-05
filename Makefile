
env: 
	virtualenv env

run:
	. env/bin/activate; pip install --requirement requirements.txt
	. env/bin/activate; python app.py
