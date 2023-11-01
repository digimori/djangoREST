from rest_framework import serializers
from comments.models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.comments')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Comments
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 
            'created_at', 'content', 'updated_at', 'post'
        ]


class CommentDetailSerializer(serializers.CommentsSerializer):
    post = serializers.ReadOnlyField(source='post.id')