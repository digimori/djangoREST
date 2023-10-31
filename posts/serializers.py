from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is larger than 2MB. Please use a smaller image.'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image is wider than 4096px, please use a smaller image.'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image is taller than 4096px, please use a smaller image.'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'created_at', 'updated_at',
            'content', 'image', 'title', 'image_filter'
        ]