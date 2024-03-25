from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class ClassList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return get_object_or_404(Class, pk=pk)
        except Class.DoesNotExist:
            raise Http404

    def get(self, request, class_id):
        class_instance = self.get_object(pk = class_id)
        serializer = ClassSerializer(class_instance)
        return Response(serializer.data)

    def patch(self, request, class_id):
        class_instance = self.get_object(pk = class_id)
        serializer = ClassSerializer(class_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, class_id):
        class_instance = self.get_object(pk = class_id)
        class_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AssignmentList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignmentDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return get_object_or_404(Assignment, pk=pk)
        except Assignment.DoesNotExist:
            raise Http404

    def get(self, request, assignment_id):
        assignment_instance = self.get_object(pk = assignment_id)
        serializer = AssignmentSerializer(assignment_instance)
        return Response(serializer.data)

    def patch(self, request, assignment_id):
        assignment_instance = self.get_object(pk = assignment_id)
        serializer = AssignmentSerializer(assignment_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, assignment_id):
        assignment_instance = self.get_object(pk = assignment_id)
        assignment_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class QuestionList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return get_object_or_404(Question, pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, question_id):
        question_instance = self.get_object(pk = question_id)
        serializer = QuestionSerializer(question_instance)
        return Response(serializer.data)

    def patch(self, request, question_id):
        question_instance = self.get_object(pk = question_id)
        serializer = QuestionSerializer(question_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id):
        question_instance = self.get_object(pk = question_id)
        question_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

