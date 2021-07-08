from django.shortcuts             import render
from rest_framework               import status
from rest_framework.decorators    import api_view,permission_classes
from rest_framework.response      import Response
from rest_framework.parsers       import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models                  import Pintura
from .serializers                 import PinturaSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_pintura(request):
    '''
    Lista todas los Pintura
    '''
    if request.method=='GET':
        pintura = Pintura.objects.all()
        serializer = PinturaSerializer(pintura, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = JSONParser().parse(request)    
        serializer=PinturaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_pintura(request,id):
    '''
    Get, update o delete de un pintura en particular
    '''
    try: #vericar que id pintura ingresado existe
        pintura = Pintura.objects.get(id_pintura=id)
    except Pintura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET' : #recuperar 1 Pintura x id_pintura
        serializer = PinturaSerializer(pintura)
        return Response(serializer.data)
    if request.method=='PUT': #actualizar 1 Pintura x id_pintura
        data=JSONParser().parse(request)   
        serializer=PinturaSerializer(pintura,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':#elimir 1 Pintura x id_pintura
        pintura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

