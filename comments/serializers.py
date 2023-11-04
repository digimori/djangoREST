from rest_framework import serializers
from comments.models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime


class CommentsSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    owner = serializers.ReadOnlyField(source='owner.comments')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 
            'created_at', 'content', 'updated_at', 'post'
        ]


class CommentDetailSerializer(CommentsSerializer):
    post = serializers.ReadOnlyField(source='post.id')