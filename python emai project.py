
import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg['Subject'] = 'CSR Offer Letter | Thops Tech Career Solutions'
msg['From'] = 'pamappagari@gmail.com'
msg['To'] = '9922005287@klu.ac.in'

msg.set_content("""
Dear Candidate,

Greetings from Thops Tech Career Solutions.

We are pleased to inform you that you have been selected for our free CSR program.

Thank you.

Best regards,
Pamappagari Jyothi
""")

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login("pamappagari@gmail.com", "cevmmzzvgcqsdfcg")

server.send_message(msg)

print("Email sent successfully")

server.quit()

