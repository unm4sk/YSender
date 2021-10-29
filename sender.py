from getpass import getpass
import smtplib

# smptObj = smtplib.SMTP("smtp.yandex.ru", 465)
# smptObj.starttls()


send_mail = []
mail = input('Your mail:\n>>> ')
password = getpass('Password:\n>>> ')
subject = input('Subject:\n>>> ')
main_text = input('Message:\n>>> ')
f_choose = input('Enter the name of file with emails:\n>>> ')


f = open(f_choose, 'r')
for line in f:
    send_mail.append(line.strip())


# smptObj.login(mail, password)

server = smtplib.SMTP_SSL('smtp.yandex.com')
server.set_debuglevel(1)
server.ehlo(mail)
server.login(mail, password)
server.auth_plain()

for i in range(len(send_mail)): 
    message = f"From: {mail}\nTo: {send_mail[i]}\nSubject: {subject}\n\n{main_text}"
    server.sendmail(mail, send_mail[i], message)

print("\n\nProgram succesfully completed!")

server.quit()
