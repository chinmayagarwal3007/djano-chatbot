from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv('gemini_api_key')
print(gemini_api_key)

genai.configure(api_key=gemini_api_key)

def ask_openai(message):
    model=genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(message)
    return response.text

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message':message, 'response':response}) 
    return render(request, 'chatbot.html')