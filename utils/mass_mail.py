from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from supalumni.settings import common
from django.contrib.sites.models import Site

def send(firstname = ''):
    users = User.objects.filter(first_name = firstname)
    for u in users:
        prepare(u)


def prepare(user, sendmail=False):
                    
    # send mail with the key (unhashed !)
    subject = "Your registration on supalumni.net"    
        
    content = "Dead SUPINFO member,\n"+user.username
    content += "Unfortunatly, errors on our website may have prevented you to complete your registration\n"
    content += "These problems being solved, you can now get back to http://supalumni.net and start a new registration with your Campus ID\n\n" 
    content += "Thanks."
    
    if sendmail:
        send_mail(subject, content, None, [to])
        user.delete()
    
    send_mail(subject, content, None, ["52086@supinfo.com"])
