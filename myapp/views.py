from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        num1 = data.get('num1')
        num2 = data.get('num2')
        operation = data.get('operation')

        if not num1 or not num2 or not operation:
            return JsonResponse({'error': 'Invalid input'}, status=400)

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            return JsonResponse({'error': 'Invalid numbers'}, status=400)

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return JsonResponse({'error': 'Division by zero'}, status=400)
            result = num1 / num2
        else:
            return JsonResponse({'error': 'Invalid operation'}, status=400)

        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        subject = data.get('subject')
        message = data.get('message')
        recipient = data.get('recipient')

        if not subject or not message or not recipient:
            return JsonResponse({'error': 'Invalid input'}, status=400)

        send_mail(
            subject,
            message,
            'caudillojose5@gmail.com',  # Replace with your email
            [recipient],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Email sent successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Create your views here.
