# CRYPTOKENS

Aplicación web desarrollada en Python con framework Flask y base de datos SQLite

## FUNCIONALIDAD

CRYPTOKENS es una API que tiene como finalidad el registro de movimientos de criptomonedas. La idea es comprar, vender o intercambiar criptomonedas para hacer crecer la inversión y obtener beneficios en euros.

La página 'Inicio' muestra todos los 'criptomovimientos' realizados: Compra, venta o intercambio

La página 'Compraventa' nos permite realizar una 'Cryptotransacción'. Iniciando con Euros, se puede invertir en criptomonedas. Una vez se dispone de criptos en cartera, se podrán utilizar como moneda de cambio. El sistema consultará con coinAPI.io para obtener el valor de cambio.

La página 'myCRYPTO' muestra la situación de la inversión, los euros gastados en comprar Bitcoin y el valor actual del total de criptomonedas que existan en la cartera del usuario según sus movimientos. Si hay ganancia, la cifra en 'Valor Actual' se mostrará en verde; si hay pérdida, se mostrará en rojo.

## INSTRUCCIONES PARA LA UTILIZACION DE CRYPTOKENS

### Instalación

-Crear un entorno en python y ejecutar el comando

```pip install - requirements.txt```

-La librería ultilizada en Flask https://flask-wtf.readthedocs.io/en/1.2.x/

### Ejecución del programa
-Inicializar parametros para servidor de Flask
-en mac:

``export FLASK_APP = main.py``

-en windows

``set FLASK_APP=main.py``

### Otra opción de ejecución
-Crear un archivo .env y dentro agregar los siguientes:

``FLASK_APP=main.py``
``FLASK_DEBUG=True``

-Y luego poder ejecutar en la terminal el comando:

``flask run``

### Comando para ejecutar el servidor

``flask --app main run``

### Comando para ejecutar el servidor en otro puerto diferente (por default siempre es el 5000)

``flask --app main run -p 5002``

### Comando para ejecutar el servidor en modo debug (realizar cambios en tiempo real)

``flask --app main --debug run``

### Agregar en el archivo config.py:

``ORIGIN_DATA='data/movements.sqlite'``

-La SECRET_KEY se obtiene en https://randomkeygen.com/

``SECRET_KEY='AGREGA TU CODIGO ENCRIPTADO'``

-La API KEY se obtiene en www.coinapi.io

``APIKEY='AGREGA TU API KEY UNICA'``




