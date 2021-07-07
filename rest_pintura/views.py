from django.shortcuts             import render
from rest_framework               import status
from rest_framework.decorators    import api_view
from rest_framework.response      import Response
from rest_framework.parsers       import JSONParser
from django.views.decorators.csrf import csrf_exempt

from core.models import Pintura
from .serializers import PinturaSerializer
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_pintura(request):
    '''
    Lista todas los vehiculos
    '''
    if(request.method=='GET'):
        pintura=Pintura.object.all()
        serializers=PinturaSerializer(pintura, many=True)
        return Response(serializers.data)
    elif (request.method=='POST'):
        data = JSONParser().parse(request)    
        serializers=PinturaSerializer(data=data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
