from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from client.models import Client, CustomUser
from .models import Customer, File, FileStatus, Status
from datetime import date
from django.http import JsonResponse
import json

@login_required
def dashboard(request):
    user = request.user
    if user.isChamp():
        return render(request, 'champ/dashboard.html')
    elif user.isClient():
        return render(request, 'client/dashboard.html')
    else:
        return redirect('/admin')

@login_required
def status(request):
    user = request.user
    if user.isChamp():
        clients = Client.objects.all()
        retrunObj = {
            'clients': clients,
            'date': date.today().strftime("%Y-%m-%d")
        }
        return render(request, 'champ/status.html', retrunObj)
    elif user.isClient():
        return render(request, 'client/status.html')
    else:
        return redirect('/admin')

@login_required
def get_customers(request):
    user = request.user
    if user.isChamp():
        clientId = request.GET.get('client_id')
        customers = Customer.objects.filter(client=clientId).values('id', 'name', 'customerId')
        customerList = list(customers)
        return JsonResponse(customerList, safe=False)
    elif user.isClient():
        return JsonResponse({}, safe=False)
    else:
        return redirect('/admin')

@login_required
def get_file_status(request):
    user = request.user
    if user.isChamp():
        clientId = request.GET.get('client_id')
        customerId = request.GET.get('customer_id')
        date = request.GET.get('date')
        if not (clientId and customerId and date):
            response = {
                'files': [],
                'status': []
            }
            return JsonResponse(response, safe=False)
        files = File.objects.filter(client=clientId).values('id', 'name')
        status = Status.objects.values()
        fileStatus = FileStatus.objects.filter(customer=customerId, date=date).values('id', 'file', 'status', 'comments')
        temp = [{
            'file_id': file['id'],
            'file_name': file['name'],
            'status': (fileStatus.filter(file=file['id']).first() or {'status': status[0]['id']})['status'],
            'comments': (fileStatus.filter(file=file['id']).first() or {'comments': ''})['comments'],
        } for file in files]
        fileStatusList = list(temp)
        response = {
            'files': fileStatusList,
            'status': list(status)
        }
        return JsonResponse(response, safe=False)
    elif user.isClient():
        return JsonResponse({}, safe=False)
    else:
        return redirect('/admin')


@login_required
def upsert_file_status(request):
    user = request.user
    if user.isChamp():
        if request.method == 'POST':
            data = json.loads(request.body)
            customer_id = data.get('customerId')
            date = data.get('date')
            user_id = request.user.id

            try:
                customer = Customer.objects.get(id=customer_id)
                user = CustomUser.objects.get(id=user_id)
            except (Customer.DoesNotExist, CustomUser.DoesNotExist) as e:
                return JsonResponse({'error': str(e)}, status=404)

            for file_data in data.get('files', []):
                file_id = file_data.get('file_id')
                status_id = file_data.get('status')
                comments = file_data.get('comments')

                try:
                    file = File.objects.get(id=file_id)
                    status = Status.objects.get(id=status_id)
                except (File.DoesNotExist, Status.DoesNotExist) as e:
                    return JsonResponse({'error': str(e)}, status=404)

                file_status, created = FileStatus.objects.update_or_create(
                    customer=customer,
                    file=file,
                    date=date,
                    defaults={
                        'status': status,
                        'comments': comments,
                        'drafterBy': user,
                        'isDraft': True
                    }
                )
            
            return JsonResponse({'message': 'File statuses updated successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
    elif user.isClient():
        logout(request)
        return redirect('/users/login')
    else:
        return redirect('/admin')