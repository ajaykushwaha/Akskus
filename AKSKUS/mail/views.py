from django.core.mail import send_mail,EmailMessage
from django.http import HttpResponse


def simple_mailtest(request):
    #res = send_mail("Try mail only","Lorem ipsum","ajaykushwaha1215@gmail.com",["ak8366395@gmail.com"],False)
    html_content = '<img src="http://www.facweb.iitkgp.ernet.in/~shamik/spring2008/sca/tutorials/download/pami.uwaterloo.ca/tizhoosh/images/test2.jpg" alt="Smiley face" height="100" width="100">'
    email = EmailMessage("Tada tada tada",html_content,"ajaykushwaha1215@gmail.com",["ak8366395@gmail.com"],False)
    email.content_subtype = "html"
    res = email.send(fail_silently=False)
    return HttpResponse('%s'%res)