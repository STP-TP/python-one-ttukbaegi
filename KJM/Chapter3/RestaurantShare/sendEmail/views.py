from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..shareRes.models import *     # right?
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your views here.
def send_email(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    # print(checked_res_list, "/", inputReceiver, "/", inputTitle, "/", inputContent)

    mail_html = "<html><body>"
    mail_html += "<h1> 맛집 공유 </h1>"
    mail_html += "<p>"+inputContent+"<br>"
    mail_html += "발신자님께서 공유하신 맛집은 다음과 같습니다.</p>"

    # 274쪽

    return HttpResponseRedirect(reverse('index'))
