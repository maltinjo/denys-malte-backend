from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import  APIView
from rest_framework import generics
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet

from .models import Manufacture
from .serializers import ManufactureSerializer


# Django

def manufacture_list(request):
    manufactures = Manufacture.objects.all()
    print("SQL: ", manufactures.query)

    context = {
        "manufactures": manufactures,
    }
    return render(request, 'manufacture-list.html', context=context)


class ManufactureListView(ListView):
    model = Manufacture
    template_name = "manufacture-list.html"
    context_object_name = "manufactures"


class ManufactureDetailView(DetailView):
    model = Manufacture
    template_name = "manufacture-detail.html"
    context_object_name = "manufacture"


# Django REST
@api_view(["GET"])
def manufacture_list(request):
    manufactures = Manufacture.objects.all()
    serializer = ManufactureSerializer(manufactures, many=True)

    return Response(data=serializer.data, status=200)


class ManufactureListApiView(APIView):
    def get(self, request):
        manufactures = Manufacture.objects.all()
        serializer = ManufactureSerializer(manufactures, many=True)

        return Response(data=serializer.data, status=200)

    def post(self, request):
        serializer = ManufactureSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        Manufacture.objects.create(**serializer.validated_data)

        return Response(serializer.data, status=201)


class ManufactureListApiView(generics.GenericAPIView, ListModelMixin, ):
    queryset = Manufacture.objects.all()
    serializer_class = ManufactureSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ManufactureViewSet(ModelViewSet):
    queryset = Manufacture.objects.all()
    serializer_class = ManufactureSerializer
