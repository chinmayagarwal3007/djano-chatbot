from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

gemini_api_key = "AIzaSyD96dIsNYmvuH3N0Hy9eIUyzU96ui4vHDs"

genai.configure(api_key=gemini_api_key)

def ask_openai(message):
    model=genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(message)
    return response.text

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        print(response)
        return JsonResponse({'message':message, 'response':response}) 
    return render(request, 'chatbot.html')