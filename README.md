# PyHearthBeat

Instalar rabbitmq

	sudo apt-get install rabbitmq-server

Los siguientes comandos deben correrse los 3 al tiempo
en ese orden respectivamente

Correr el servidor de Celery
	
	celery -A tasks worker --loglevel=info

Correr el servidor de Websockets

	python ws_app_persistent.py

Correr el cliente del sensor

	python Rate_Client.py

Para guardar txt

	python ws_app_persistent.py > output.txt
o 
	python ws_app_persistent.py >> output.txt