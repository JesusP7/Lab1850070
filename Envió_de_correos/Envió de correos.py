#Jesús Ponce de León Mota
#Matrícula: 1850070

import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#Creamos el onjeto MIMEMultipart
msg = MIMEMultipart("alternative")
msg["Subject"] = "Prueba de envio (script python) - 1850070"
msg["From"] = "chuyponce721@gmail.com"
msg["To"] = "gerardo.bernal@uanl.edu.mx"
filename = "fcfm_cool.png"
#Mensaje con formato HTML
html = """\
<html>
    <body>
        <p><b>Prueba 12</b><br>
            Ejercicio de la practica 12 para envío de correos
            Alumno: Jesús Ponce de León Mota
            Matrícula: 1850070
        </p>
    </body>
<html>
"""

part = MIMEText(html, "html")
msg.attach(part)
#Agregamos la imagen
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
#Configuramos el encabezado
part.add_header(
    "Content-Disposition",
    "attachment", filename= filename
)
msg.attach(part)
#Creamos la conexión y enviamos el mensaje
conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.ehlo()

conn.starttls()

conn.login("chuyponce721@gmail.com", "erajjaadhzmzom")

conn.sendmail("chuyponce721@gmail.com", "gerardo.bernal@uanl.edu.mx", msg.as_string())

conn.quit()
