from email.message import EmailMessage

from smtplib import SMTP

email = EmailMessage()

email['Subject'] = 'Confirmation message'

email['from'] = 'mmms404'

email['to'] = '9sammmmmmm@gmail.com'

email.set_content('wow, you are the winner!')

with SMTP(host='smtp.gmail.com', port=587) as mail:
 
  mail.ehlo()
 
  mail.starttls()
  
  mail.login('9sammmmmm@gmail.com', '_Mmms404#')

  mail.sendmail()