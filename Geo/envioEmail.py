import smtplib

def enviodeEmail():
    mail_from = 'origin@mail.com'
    mail_to = ['destiny1@mail.com', 'destiny2@mail.com']
    mail_subject = 'Hello'
    mail_message_body = 'Hello World!'

    mail_to_string = ', '.join(mail_to)

    mail_message = f'''
    From: {mail_from}
    To: {mail_to_string}
    Subject: {mail_subject}

    {mail_message_body}


    server = smtplib.SMTP('localhost')
    server.sendmail(mail_from, mail_to, mail_subject, mail_message)
    server.quit()
