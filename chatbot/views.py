from django.shortcuts import render
from django.http import JsonResponse

def chatbot(request):
    if request.method == 'POST':
        print('I am here')
        message = request.POST.get('message')
        print(message)
        response = 'Hi this is my response'
        return JsonResponse({'message':message, 'response':response}) 
    return render(request, 'chatbot.html')