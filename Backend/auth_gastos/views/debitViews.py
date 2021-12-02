from rest_framework import views, status
from rest_framework.response import Response
from rest_framework import generics
from auth_gastos.models.debit import Debit
from auth_gastos.serializers.debitSerializer import DebitSerializer

class DebitTestView(views.APIView):
    
    def get(self, request):
        code = status.HTTP_200_OK
        data = {"message": "probando GET de la vista de Debit"}
        return Response(data, status = code)

    def post(self, request):
        print("Probando POST de la vista de Debit")
        print("Informacion recibida:", request.data)
        code = status.HTTP_201_CREATED
        return Response(status = code)

class DebitMainView(views.APIView):

    def get(self, request):
        serialized = DebitSerializer(Debit.objects.all(), many = True)
        return Response(serialized.data, status = status.HTTP_200_OK)

class DebitListCreateView(generics.ListCreateAPIView):
    queryset = Debit.objects.all()
    serializer_class = DebitSerializer

class DebitRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debit.objects.all()
    serializer_class = DebitSerializer