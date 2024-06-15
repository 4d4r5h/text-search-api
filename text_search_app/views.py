from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Paragraph, Word
from .serializers import UserSerializer, ParagraphSerializer, WordSerializer

User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ParagraphListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        text = request.data.get('text', '')
        paragraphs = text.split('\n\n')
        paragraph_ids = []

        for paragraph_text in paragraphs:
            paragraph = Paragraph.objects.create(text=paragraph_text)
            paragraph_ids.append(paragraph.id)
            words = paragraph_text.lower().split()
            unique_words = set(words)

            for word in unique_words:
                Word.objects.create(word=word, paragraph=paragraph)

        return Response({'paragraph_ids': paragraph_ids}, status=status.HTTP_201_CREATED)

class SearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, word):
        word = word.lower()
        word_objects = Word.objects.filter(word=word).distinct('paragraph')
        paragraphs = [word_obj.paragraph for word_obj in word_objects[:10]]

        return Response(ParagraphSerializer(paragraphs, many=True).data)
