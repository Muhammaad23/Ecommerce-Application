from rest_framework.response import Response
from .serializers import ProductSerializers
from .models import Product
from rest_framework.views import APIView

class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()  # Use 'objects' instead of 'object'
        serializers = ProductSerializers(queryset, many=True)
        return Response(serializers.data)
