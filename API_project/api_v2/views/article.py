from rest_framework import viewsets
from webapp.models import Article
from api_v2.serializers import ArticleSerializers, CreateArticleSerializer, UpdateArticleSerializerPerm
from api_v2.permissions import CustomerAccessPermission

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = [CustomerAccessPermission]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ArticleSerializers
        elif self.request.method == 'POST':
            return CreateArticleSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return UpdateArticleSerializerPerm

