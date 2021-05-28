from rest_framework import serializers
from webapp.models import Article


class ArticleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'text', 'name', 'email', 'rating', 'status', 'data')
        read_only_fields = ('id', 'data')



class CreateArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('text', 'name', 'email',)
        read_only_fields = ('id', 'data')


class UpdateArticleSerializerPerm(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('text', 'status',)
        read_only_fields = ('id', 'data')