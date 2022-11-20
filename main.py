import smtplib
import pandas as pd

my_csv = pd.read_csv("Recipients.csv", index_col = "Email")

email = (list((my_csv.index)))
firstName = (my_csv.loc[:, "Fname"].values)
location = (my_csv.loc[:, "Area"].values)
industry = (my_csv.loc[:, "Industry"].values)

data = list(zip(email, firstName, location, industry))

def sendmail(email, firstName, location, industry):
    server = smtplib.SMTP('64.233.184.108', 587)
    email_password = "My_Email_Password"

    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("my_email_address@gmail.com", email_password)

    body = f"Hello {firstName}. \n\n" \
           f"We value you as a member of Firefly industries and thank you for supporting {industry} which is one of our subsidiary companies. We will be opening up a new subsidiary company, Procrat, that will deal in organic food production. As our member from {location}, you are invited to join us in our grand opening at Naivasha lounge on 12-12-2022." \
           f"\n\nThank you for your time, {firstName}."

    subject = "INVITATION TO PROCRAT GRAND OPENING."

    message=f'subject: {subject} \n\n{body}'

    server.sendmail(
        "my_email_address@gmail.com",
        email,
        message
    )

    print(f"Message sent successfully to {firstName} at {email}!")


for i in data:
    email= i[0]
    firstName= i[1]
    location= i[2]
    industry = i[3]

    sendmail(email, firstName, location, industry)

