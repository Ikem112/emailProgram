import smtplib
from getpass import getpass
import os



def send_user_Gmail(sender_address, sender_password, receiver_address):
    try:
        print('entering upgrade')
        upgrade = smtplib.SMTP('smtp.google.com', 587)
        print('im in smtplib.SMTP')


        # Security
        upgrade.starttls()
        print('im in security')
        upgrade.login(sender_address, sender_password)
        print('im in login port')

        message = 'hello there! hope you are having a lovely day. \nThis is to inform you that our application will have some down time today because of an upgrade. \nThe app will be up and running once it"s done'

        upgrade.sendmail(sender_address, receiver_address, message)

        upgrade.quit()
        print ('Email sent successfully!')
    except Exception as ex:
        print('something went wrong...', ex)
    

def main():
    sender_address = os.getenv('SENDER_ADDRESS')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_address = input('Please enter your email address: ')

    send_user_Gmail(sender_address, sender_password, receiver_address)

main()
        
    



