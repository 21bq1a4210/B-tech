import smtplib
from email.message import EmailMessage
import ssl

class SendMail:
    def __init__(self, data):
        self.data = data
        self.sender = 'greviencevvit@gmail.com'
        self.password = 'otfk agzp pvjr hiec '

    def setMail(self, receiver, subject, body):
        mail = EmailMessage()
        mail['From'] = self.sender
        mail['To'] = receiver
        mail['subject'] = subject
        mail.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender, self.password)
            smtp.sendmail(self.sender, receiver, mail.as_string())

    def ACKToStudent(self):
        receiver = self.data['email']

        subject = f'Acknowledgment of Your Grievance'

        body = f'''
            Dear {self.data['name'].upper()},
    Thank you for registering your grievance. We appreciate your time and trust.
    Rest assured, our team is actively working on your concern. We will keep you updated and aim for a prompt resolution.
    If you have any questions, please feel free to contact us at {self.sender} or 1234567890.
    Best regards,
    
    Minor project
    Project: VVIT expert system
    VVIT '''

        self.setMail(receiver, subject, body)

    def MailToCounseller(self):
        # sender = 'greviencevvit@gmail.com'
        # password = 'otfk agzp pvjr hiec '
        receiver = '21bq1a4210@vvit.net' # counsellor mail

        subject = 'Complaint by {} '.format(self.data['name'])

        body = f'''
            Respected Sir ,
            My name is {self.data['name'].upper()}, and I am writing to bring a matter of concern to your attention. I am a {self.data['year']} year {self.data['who'].upper()} in the {self.data['dept'].upper()} department at VVIT, and I wanted to express my grievances regarding an issue I have encountered.
            My registration number is {self.data['reg_number'].upper()}, and my contact email is {self.data['email'].upper()}. As a {self.data['who'].upper()} of the our institution, I have always held high expectations for the academic and non-academic experiences here.
        Recently, I have come across a {self.data['type_of_grievance'].upper()} matter that has been affecting me. 
        COMPLAINT: 
        {self.data['complant']}
        
            I believe that addressing this issue is crucial to maintaining the quality and integrity of our institution. I kindly request your assistance in resolving this matter promptly.
            Thank you for your attention to this concern, and I look forward to your response.
        
        Sincerely,
        {self.data['name'].upper()}
        '''

        self.setMail(receiver, subject, body)
        self.ACKToStudent()

if __name__ == "__main__":
    # Assuming 'data' contains the required information
    data = {
        'name': 'John Doe',
        'year': '2nd',
        'who': 'student',
        'dept': 'CSE',
        'reg_number': '123456',
        'email': 'john@example.com',
        'type_of_grievance': 'Academic',
        'complant': 'I have a concern about the course material.'
    }

    # Create an instance of the SendMail class with 'data'
    mail = SendMail(data)

    # Send the complaint email to the counselor
    mail.MailToCounseller()
