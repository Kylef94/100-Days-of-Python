import smtplib

my_email = 'kftest29@gmail.com'
password = 'Test29'

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs='kftest29@yahoo.com', msg='Hello')
connection.close()