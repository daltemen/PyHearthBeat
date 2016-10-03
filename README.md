# PyHearthBeat

Correr el servidor de Celery
	
	celery -A tasks worker --loglevel=info

Correr el servidor de Websockets

	python ws_app_persistent.py

Correr el cliente del sensor

	python Rate_Client.py