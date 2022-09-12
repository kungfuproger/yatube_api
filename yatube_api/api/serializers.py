from rest_framework import serializers, validators

from posts.models import Comment, Group, Post, Follow, User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowingSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

        validators = [
            validators.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Подписка уже оформлена'
            )
        ]

    def validate_following(self, value):
        if self.context.get('request').method == 'POST':
            if self.context.get('request').user == value:
                raise serializers.ValidationError(
                    "Подписка на себя невозможна")
            return value

