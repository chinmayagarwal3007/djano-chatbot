from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect

load_dotenv()

gemini_api_key = os.getenv('gemini_api_key')

genai.configure(api_key=gemini_api_key)


def ask_openai(message):
    model=genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(message)
    return response.text

@login_required
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message':message, 'response':response}) 
    return render(request, 'chatbot.html')

def register(request):
    form = None
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('chatbot')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html',{'form':form})