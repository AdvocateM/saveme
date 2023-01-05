import smtplib
import time
from fpdf import FPDF
import random
import string


pdf = FPDF()
pdf.add_page()


pdf.set_font("Arial", "B", 16)
#  create passwords to cut suspicion
letters = string.ascii_lowercase


for x in range(6):
  result_str = ''.join(random.choice(letters) for i in range(5))
  print(result_str)
  pdf.write(4,result_str, "hyhhh")
else:
  print("Finally finished!")


pdf.output(f"{result_str}.pdf")

# My email and password
from_email = 'mrtamaroga@gmail.com'
from_password = 'your password'
to_email = 'tboymaroga7@gmail.com'

# Connect to the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_email, from_password)
print("Login successful ")

# Send the email
subject = "PDF opened"
body = "This is an automated message to let you know that the PDF file has been opened."
time.sleep(1) # Wait  1seconds before sending the email
server.sendmail(from_email, to_email, f'Subject: {subject}\n\n{body}')

# Disconnect from the server
server.quit()
