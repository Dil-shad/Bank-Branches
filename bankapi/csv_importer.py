import pandas as pd
from django.apps import apps
from django.db import models
from rest_framework.views import APIView
from .models import Banks
from django.http import Http404, HttpResponse, JsonResponse


def csv_importer(request):
    try:
        df = pd.read_csv('static/csv/bank_branches.csv')
        banks_data = []
        for index, row in df[:100].iterrows():
            bank = Banks(
                ifsc=row['ifsc'],
                bank_id=row['bank_id'],
                bank_name=row['bank_name'],
                branch=row['branch'],
                address=row['address'],
                city=row['city'],
                district=row['district'],
                state=row['state']
            )
            #bank.save()
            banks_data.append(bank)
            print(len(banks_data))

        Banks.objects.bulk_create(banks_data)

        return HttpResponse("Imported successfully")

    except FileNotFoundError:
        return HttpResponse("CSV file not found", status=404)

    




# def csv_importer(request):
#     try:
#         df = pd.read_csv('static/csv/bank_branches.csv')
#         banks_data = df[:10].to_dict('records')
#         print(banks_data)
#         Banks.objects.bulk_create(banks_data)
#         return JsonResponse(banks_data, safe=False)
#     except FileNotFoundError:
#         raise Http404('File not found')





# class DynamicModelUploadView(APIView):
#     def post(self, request):
#         csv_file = request.FILES.get('file')

#         if not csv_file:
#             return JsonResponse({'error': 'No file uploaded.'}, status=400)

#         try:
#             df = pd.read_csv(csv_file)
#             app_label = 'bankapi'  # Replace with your Django app label
#             model_name = 'DynamicModel'  # Replace with the desired model name

#             model_fields = [
#                 (column, models.CharField(max_length=255))
#                 for column in df.columns
#             ]

#             model_attrs = {
#                 '__module__': f'{app_label}.models',
#                 'id': models.AutoField(primary_key=True),
#                 **dict(model_fields),
#             }

#             dynamic_model = type(model_name, (models.Model,), model_attrs)
#             apps.all_models[app_label][model_name] = dynamic_model

#             return JsonResponse({'message': 'Dynamic model created successfully.'}, status=201)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)


