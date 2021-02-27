from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import status as s
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from em_site.apps.store.models import Book
from em_site.apps.store.serializers import BundleOfferSerializer

USER = get_user_model()


class BundleOfferAPIView(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        books = list(Book.objects.filter(user=request.user).values())
        print(books)
        return JsonResponse(books, safe=False)

    @staticmethod
    def post(request):
        data = request.data.copy()
        serializer = BundleOfferSerializer(data=data, context={"request": request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=s.HTTP_201_CREATED)

        return Response(serializer.errors)
