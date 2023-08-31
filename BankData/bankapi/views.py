from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Banks
from .serializers import BanksSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (
    IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser,)
from django.http import Http404
from accounts.authentication import JWTAuthentication
from django.db.models import Q


# GET API to fetch a bank details, given branch IFSC code


class BankDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            ifsc_code = request.query_params.get('ifsc')
            if not ifsc_code:
                raise Http404('IFSC code not provided')

            bank = Banks.objects.get(ifsc=ifsc_code)
            serializer = BanksSerializer(bank)
            return Response(serializer.data)
        except Banks.DoesNotExist:
            return Response({'error': 'Bank details not found.'}, status=404)


# GET API to fetch all details of branches, given bank name and a city. This API should also
# support limit and offset parameters


class GetBranchDetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bank_name = request.query_params.get('bank_name')
        city = request.query_params.get('city')
        limit = int(request.query_params.get('limit', 0))
        offset = int(request.query_params.get('offset', 0))

        branches = Banks.objects.all()

        if bank_name:
            branches = branches.filter(bank_name__icontains=bank_name)
        if city:
            branches = branches.filter(city__icontains=city)

        total_count = branches.count()
        branches = branches[offset:offset+limit]

        serializer = BanksSerializer(branches, many=True)

        return Response({
            'total_count': total_count,
            'branches': serializer.data
        })


"""simple pagination"""


class AllBanksPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    limit = 5
    offset = 5


class AllBanksView(APIView):

    pagination_class = AllBanksPagination

    def get(self, request):
        paginator = self.pagination_class()
        banks = Banks.objects.all()
        paginated_banks = paginator.paginate_queryset(banks, request)
        serializer = BanksSerializer(paginated_banks, many=True)
        return paginator.get_paginated_response(serializer.data)
