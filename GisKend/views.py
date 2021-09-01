from rest_framework.decorators import api_view
from .models import Evento
from .serializers import EventoSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(('GET', 'PUT','DELETE'))
def get_evento(request, id):
    try:
        evento = Evento.objects.get(id=id)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Api key
    if request.method == "GET":
        serializer = EventoSerializer(evento)
        return Response(serializer.data)

    if request.method == "DELETE":
        operation = evento.delete()
        data = {}
        if operation:
            data["succes"]= "delete succesful"
        else:
            data["failure"]= "delete failed"
        return Response(data=data)

    if request.method == "PUT":
        serializer = EventoSerializer(evento, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["succes"] = "update succesful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('POST',))
def crear_evento(request):
    evento = Evento()
    #Api key
    if request.method == "POST":
        serializer = EventoSerializer(evento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)