backupper
=========

Sistema que permite gestionar los backups de multiples bases de datos en varios servidores simultáneamente y de forma centralizada.
Estos backups puede ser programados para ser ejecutados periódicamente, realizando una verificación de calidad de los mismos.

Los backups programados, se puede auto-postergar si la conexión con el servidor que contiene la base de datos falla.

La función de gráficos, permite visualizar la evolución del volumen de información almacenado.

Dependiendo del motor de base de datos utilizado, el sistema ofrece opciones propias de este.

Para poder administrar grandes cantidades de bases de datos, se podran crear grupos de usuarios encargados de las mismas, delegando a estos el trabajo.

Para mantener un control sobre el espacio de almacenamiento, se pueden eliminar backups que se consideren obsoletos, estableciendo una fecha límite para estos, manteniendo siempre al menos un backup.

TODO:
=====

1) Implementar el dump en cada backend


Notas:
------
Usar un archivo ~/.pgpass para conexiones automáticas con psql.

cada linea del archivo tendrá:

server:port:database:username:password

con los siguientes permisos:

0600
