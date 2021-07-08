from django.shortcuts             import render
from rest_framework               import status
from rest_framework.decorators    import api_view
from rest_framework.response      import Response
from rest_framework.parsers       import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models                  import Pintura
from .serializers                 import PinturaSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_pintura(request):
    '''
    Lista todas los Pintura
    '''
    if request.method=='GET':
        pintura = Pintura.objects.all()
        serializers = PinturaSerializer(pintura, many=True)
        return Response(serializers.data)
    elif request.method=='POST':
        data = JSONParser().parse(request)    
        serializers=PinturaSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    
@api_view(['GET','PUT','DELETE'])
def detalle_pintura(request,id):
    '''
    Get, update o delete de un vehiculo en particular
    '''
    try: #vericar que id pintura ingresado existe
        pintura = Pintura.objects.get(id_pintura=id)
    except Pintura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=='GET'): #recuperar 1 Pintura x id_pintura
        serializer=PinturaSerializer(pintura)
        return Response(serializer.data)
    if(request.method=='PUT'): #actualizar 1 Pintura x id_pintura
        data=JSONParser().parse(request)   
        serializer=PinturaSerializer(pintura,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='DELETE'):#elimir 1 Pintura x id_pintura
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

