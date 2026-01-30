from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer


@api_view(['GET', 'POST', 'DELETE'])
def home(request, pk=None):

    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE' and pk is not None:
        try:
            item = Item.objects.get(pk=pk)
            item.delete()
            return Response({'message': 'Item deleted successfully'}, status=204)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=404)
