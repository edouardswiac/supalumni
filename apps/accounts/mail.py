from django.core.mail import send_mail as django_send_mail
from threading import Thread

def async_send_mail(subject, message, from_email, recipient_list, **kwargs):
    
    class Sender(Thread):
        def __init__(self):
            super(Sender, self).__init__()
        
        def run(self):
            django_send_mail(subject, message, from_email, recipient_list, **kwargs)
 
    s = Sender()
    s.start()
    return True