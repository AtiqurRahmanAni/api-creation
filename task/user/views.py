from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . serializers import *

from .models import *


class ParentView(APIView):

    def post(self, request):
        try:
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            street = request.data.get('street')
            city = request.data.get('city')
            zip = request.data.get('zip')

            new_parent = Parent.objects.create(
                first_name=first_name, last_name=last_name, street=street, city=city, zip=zip)

            serializer = ParentSerializer(new_parent)

            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"details": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            parent_id = request.query_params.get('parent_id')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            street = request.data.get('street')
            city = request.data.get('city')
            zip = request.data.get('zip')

            parent = Parent.objects.filter(id=parent_id).first()

            if not parent:
                return Response({"details": "No parent with that parent id"}, status=status.HTTP_404_NOT_FOUND)

            parent.first_name = first_name if first_name else parent.first_name
            parent.last_name = last_name if last_name else parent.last_name
            parent.street = street if street else parent.street
            parent.city = city if city else parent.city
            parent.zip = zip if zip else parent.zip
            parent.save()

            serializer = ParentSerializer(parent)

            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"details": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        parent_id = request.query_params.get('parent_id')

        parent = get_object_or_404(Parent, id=parent_id)
        parent.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ChildView(APIView):

    def post(self, request):
        try:
            parent_id = request.data.get('parent_id')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')

            parent = Parent.objects.filter(id=parent_id).first()

            if not parent:
                return Response({"details": "No parent with that parent id"}, status=status.HTTP_404_NOT_FOUND)

            new_child = Child.objects.create(
                first_name=first_name, last_name=last_name, parent=parent)

            serializer = ChildSerializer(new_child)

            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"details": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            child_id = request.query_params.get('child_id')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')

            child = Child.objects.filter(id=child_id).first()

            if not child:
                return Response({"details": "No child with that child id"}, status=status.HTTP_404_NOT_FOUND)

            child.first_name = first_name if first_name else child.first_name
            child.last_name = last_name if last_name else child.last_name
            child.save()

            serializer = ChildSerializer(child)

            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"details": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        child_id = request.query_params.get('child_id')
        child = get_object_or_404(Child, id=child_id)
        child.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
