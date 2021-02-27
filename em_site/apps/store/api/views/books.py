from rest_framework.views import APIView


class BooksAPIView(APIView):
    def get(self, request):
        books = request
