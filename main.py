import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Konfigurasi akun email pengirim
sender_email = 'youremail@gmail.com'
sender_password = 'your password'
recipient_email = 'example@gmail.com'
subject = 'Project Simple'
message = 'Ada project simple nih.'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

try:
    # Membuka koneksi dengan server SMTP Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login ke akun pengirim
    server.login(sender_email, sender_password)

    # Mengirim email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    print('Email berhasil dikirim!')
except Exception as e:
    print(f'Gagal mengirim email. Error: {str(e)}')
finally:
    # Menutup koneksi dengan server
    server.quit()
