from .models import Customer, File, FileStatus, Status
from client.models import Client
from django.http import JsonResponse
from datetime import datetime, date, timedelta
from django.shortcuts import get_object_or_404

def get_statuses_count_for_dashboard(fileStatusObject, customers):    
    processedFileStatus = fileStatusObject.filter(status__in=Status.objects.filter(color='success'))
    customersWithAllFielsProcessed = processedFileStatus.values('customer').distinct()
    NotProcessedCustomers = fileStatusObject.exclude(status__in=Status.objects.filter(color='success')).values('customer').distinct().exclude(customer__in=[i['customer'] for i in customersWithAllFielsProcessed])
    
    response = {
        'allfiles': fileStatusObject.count(),
        'processedFiles': processedFileStatus.count(),
        'numberOfCustomers': customers.count(),
        'allProcessedCustomers': customersWithAllFielsProcessed.count() - NotProcessedCustomers.count(),
    }
    return response


def get_structured_file_statuses(clientId, startDate, endDate):
    if not clientId or not startDate or not endDate:
        return JsonResponse({'error': 'Missing required parameters'}, status=400)

    # Convert dates from string to date objects
    startDate = datetime.strptime(startDate, '%Y-%m-%d').date()
    endDate = datetime.strptime(endDate, '%Y-%m-%d').date()

    # client = get_object_or_404(Client, id=clientId)

    # Get all dates in the range
    date_range = [startDate + timedelta(days=x) for x in range((endDate - startDate).days + 1)]

    customers_data = []
    for customer in Customer.objects.filter(client=clientId):
        files_data = []
        for file in File.objects.filter(client=clientId):
            statuses_data = []
            for date in date_range:
                file_status = FileStatus.objects.filter(customer=customer, file=file, date=date).first()
                if file_status:
                    statuses_data.append({
                        'status_title': file_status.status.title,
                        'status_color': file_status.status.color,
                        'date': file_status.date.strftime('%Y-%m-%d'),
                        'comments': file_status.comments,
                    })
                else:
                    statuses_data.append({
                        'status_title': 'Status Not Updated Yet',
                        'status_color': 'secondary',
                        'date': date.strftime('%Y-%m-%d'),
                        'comments': '',
                    })

            files_data.append({
                'file_id': file.id,
                'file_name': file.name,
                'statuses': statuses_data,
            })

        customers_data.append({
            'customer_id': customer.id,
            'customer_name': customer.name,
            'customer_display_id': customer.customerId,
            'files': files_data,
        })

    response_data = {
        'dates': [date.strftime('%Y-%m-%d') for date in date_range],
        'customers': customers_data,
    }

    return JsonResponse(response_data, safe=False)

