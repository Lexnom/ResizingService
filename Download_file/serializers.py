from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
    file = serializers.ImageField()
    oldSize = serializers.CharField(max_length=12)
    width = serializers.IntegerField()
    height = serializers.IntegerField()