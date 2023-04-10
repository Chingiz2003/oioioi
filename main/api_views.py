from rest_framework import generics
from .models import *
from .serializers import *

class ModelApiList(generics.ListAPIView):
    serializer_class = MarkModelSerializer

    def get_queryset(self):
        queryset = MarkModel.objects.all()
        mark = self.request.query_params.get('mark', None)
        print(mark)
        if mark:
            new_mark = Mark.objects.get(id = mark)
            queryset = queryset.filter(mark=new_mark)
        return queryset