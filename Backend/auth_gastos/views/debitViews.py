from rest_framework import views, status
from rest_framework.response import Response

class DebitMainView(views.APIView):
    
    def get(self, request):

        code = status.HTTP_200_OK
        data = {"message": "probando GET de la vista de Debit"}

        return Response(data, status = code)