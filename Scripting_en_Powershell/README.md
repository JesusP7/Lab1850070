## Scripting en Powershell

Esta sección contiene 2 scripts de Powershell:

- **Scan_portv1.ps1**

	El objetivo de este script es el escaneo de equipos activos en la subred, para esto el script determina el "gateway", rango de subred, y con un ciclo validamos hosts activos en la subred.

- **Scan_alivev2.ps1**

	 Utilizando un array de los puertos más comunes el script realiza un escaneo de puertos en una dirección ip particular, este script utiliza partes de "Scan_portv1.ps1" para realizar el escaneo de los puertos.
