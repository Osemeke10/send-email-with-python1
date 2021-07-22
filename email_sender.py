import smtplib 

from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'Stephen'
email['to'] ='andrei@zerotomastery.io'
email['subjet'] ='you will be good in this coding, dont give up'

email.set_content('i am a python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('richardgaily8@gmail.com','Osemeke10')
    smtp.send_message(email)
    print('all good boss!')
