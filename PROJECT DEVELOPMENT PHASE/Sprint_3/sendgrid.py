import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='v.shaju03@gmail.com',
    to_emails='shajuhacker03@gmail.com',
    subject='Budget Tracker Application',
    html_content='<strong>Hello Shaju! Here you have chance to track your Expense!</strong>'
)
sg = SendGridAPIClient("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")
response = sg.send(message)
print(response.status_code, response.body, response.headers)
    
