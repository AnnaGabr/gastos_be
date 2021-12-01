from rest_framework import views, status
from rest_framework.response import Response

class DebitMainView(views.APIView):
    
    def get(self, request):

        code = status.HTTP_200_OK
        data = {"message": "probando GET de la vista de Debit"}

        return Response(data, status = code)

    def post(self, request):

        print("Probando POST de la vista de Debit")
        print("Informacion recibida:", request.data)
        code = status.HTTP_201_CREATED

        return Response(status = code)