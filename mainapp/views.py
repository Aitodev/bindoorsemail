from django.views import View
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
import telebot

from .models import Project, Partner, Review
from .forms import RecallForm, SendCatalogForm, SendCatandpriceForm, QuizForm, SubscribeForm

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

bot = telebot.TeleBot('1168539036:AAFt31_hCwD7Vds8m-2Aivzhxq3U6hDRTCc')

def index(request):
    projects = Project.objects.all()
    partners = Partner.objects.all()
    reviews = Review.objects.all()
    context = {
        'projects': projects,
        'partners': partners,
        'reviews': reviews,
    }
    return render(request, 'mainapp/index.html', context)


class RecallView(View):

    def post(self, request):
        if request.method == 'POST':
            form = RecallForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/thank-you')
        return redirect('/privacy')


class SendCatalogView(View):

    def post(self, request):
        if request.method == 'POST':
            form = SendCatalogForm(request.POST)
            if form.is_valid():
                form.save()
                send_mail(
                    'Заявка на каталог BINDOORS',# Заголовок
                    'Email' ,#Само сообщение,добавь просто перуменнную
                    settings.EMAIL_HOST_USER, #Мой аккаунт,поменяй там
                    ['aitolivelive@gmail.com'], #Кому отправлять 
                    fail_silently=False,
                )
                bot.send_message(104566710, "Заявка!")
                return redirect('/thank-you')
        return redirect('/privacy')


class SendCatandpriceView(View):
    def post(self, request):
        if request.method == 'POST':
            form = SendCatandpriceForm(request.POST)
            if form.is_valid():
                form.save()
                send_mail(
                    'Заявка на каталог и прайс BINDOORS',# Заголовок
                    'Email' ,#Само сообщение,добавь просто перуменнную
                    settings.EMAIL_HOST_USER, #Мой аккаунт,поменяй там
                    ['aitolivelive@gmail.com'],#Кому отправлять 
                    fail_silently=False,
                )
                return redirect('/thank-you')
        return redirect('/privacy')



class QuizView(View):
    def post(self, request):
        if request.method == 'POST':
            form = QuizForm(request.POST)
            if form.is_valid():
                form.save()
                send_mail(
                    'Квиз BINDOORS',# Заголовок
                    'Email',#Само сообщение,добавь просто перуменнную
                    settings.EMAIL_HOST_USER, #Мой аккаунт,поменяй там
                    ['aitolivelive@gmail.com'], #Кому отправлять
                    fail_silently=False,
                )
                return redirect('/thank-you')
        return redirect('/privacy')


class SubscribeView(View):
    def post(self, request):
        if request.method == 'POST':
            form = SubscribeForm(request.POST)
            if form.is_valid():
                form.save()
                send_mail(
                    'Заявка с сайта bindoors',
                    'Мы вам будем присылать новости' ,
                    settings.EMAIL_HOST_USER, 
                    ['aitolivelive@gmail.com'], 
                    fail_silently=False,
                )
                return redirect('/thank-you')
            return redirect('/agreement')
        return redirect('/privacy')


def agreement(request):
    return render(request, 'mainapp/agreement.html')


def privacy(request):
    return render(request, 'mainapp/privacy.html')


def thank_you(request):
    return render(request, 'mainapp/thank-you.html')
