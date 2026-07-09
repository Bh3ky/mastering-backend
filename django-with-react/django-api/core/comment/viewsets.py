from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.abstract.viewsets import AbstractViewSet
from core.comment.models import Comment
from core.comment.serializers import CommentSerializer
from core.post.models import Post


# TODO: comment viewset
class CommentViewSet(AbstractViewSet):
    http_method_names = ["post", "get", "put", "delete"]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()
        
        post_pk = self.kwargs['post_pk']
        return Comment.objects.filter(post__public_id=post_pk)
    
    def get_object(self):
        obj = Comment.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def perform_create(self, serializer):
        post = Post.objects.get_object_by_public_id(self.kwargs["post_pk"])
        serializer.save(author=self.request.user, post=post)

