from rest_framework import permissions, authentication
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404, ListAPIView, UpdateAPIView, \
    DestroyAPIView

from Posts.models import Post, Like, Favorite, Comment, Rating
from Posts.serializers import PostSerializer, LikeSerializer, FavoriteSerializer, CommentSerializer, RatingSerializer


class GetPostView(RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self):
        print(f"pk: {self.kwargs['pk']}")
        return get_object_or_404(Post, id=self.kwargs['pk'])


class GetPostsView(ListAPIView, UpdateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class GetUserPostsView(ListAPIView, UpdateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(owner=self.kwargs.get("user", None))


class CreatePostView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer


class DeletePostView(DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class FavoritePostView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer

    def post(self, request, *args, **kwargs):
        data = {"post": kwargs["post"]}
        request.data._mutable = True
        request.data.update(data)
        return super().post(request, *args, **kwargs)


class GetFavoritedPostsView(ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.kwargs.get('user', None))


class UnFavoritePostView(DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_object(self):
        return get_object_or_404(Favorite, post=self.kwargs.get("post", None), user=self.request.data.get('user', None))


class LikePostView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        data = {"post": kwargs["post"]}
        request.data._mutable = True
        request.data.update(data)
        return super().post(request, *args, **kwargs)


class GetPostLikesView(ListAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(post=self.kwargs.get("post", None))


class GetLikedPostsView(ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(user=self.kwargs.get("user", None))


class UnLikePostView(DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def get_object(self):
        return get_object_or_404(Like, post=self.kwargs.get("post", None), user=self.request.data.get("user", None))


class CommentPostView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        data = {"post": kwargs["post"]}
        request.data._mutable = True
        request.data.update(data)
        return super().post(request, *args, **kwargs)


class GetCommentPostView(RetrieveAPIView):
    serializer_class = CommentSerializer

    def get_object(self):
        return get_object_or_404(Comment, id=self.kwargs.get("pk", None))


class EditCommentPostView(UpdateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


class GetCommentsPostView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs.get("post", None))


class GetCommentedPostsView(ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(user=self.kwargs.get("user", None))


class UnCommentPostView(DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_object(self):
        return get_object_or_404(Comment, id=self.kwargs.get("pk", None), post=self.kwargs.get("post", None),
                                 user=self.request.data.get("user", None))


class RatePostView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RatingSerializer

    def post(self, request, *args, **kwargs):
        data = {"post": kwargs["post"]}
        request.data._mutable = True
        request.data.update(data)
        return super().post(request, *args, **kwargs)


class GetRatePostView(RetrieveAPIView):
    serializer_class = RatingSerializer

    def get_object(self):
        return get_object_or_404(Rating, post=self.kwargs.get("post", None), user=self.request.data.get("user", None))


class GetRatingsPostView(ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(post=self.kwargs.get("post", None))


class EditRatingPostView(UpdateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.all()


class UnRatePostView(DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RatingSerializer

    def get_object(self):
        return get_object_or_404(Rating, post=self.request.data.get("post", None),
                                 user=self.request.data.get("user", None))
