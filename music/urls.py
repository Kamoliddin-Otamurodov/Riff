from django.urls import path
from .views import AlbumView , AlbumDetailView , UserDetailView , UserView , ArtistView , ArtistDetailView , MusicView , MusicDetailView  


urlpatterns = [
    path('artists/', ArtistView.as_view()),
    path('artists/<int:artist_id>/', ArtistDetailView.as_view()),
    path('artists/<int:artist_id>/album/', AlbumView.as_view()),
    path('artists/<int:artist_id>/album/<int:album_id>/', AlbumDetailView.as_view()),
    path('album/', AlbumView.as_view()),
    path('album/<int:album_id>/', AlbumDetailView.as_view()),
    path('artists/<int:artist_id>/album/<int:album_id>/music/', MusicView.as_view()),
    path('artists/<int:artist_id>/album/<int:album_id>/music/<int:music_id>/', MusicDetailView.as_view()),
    path('music/', MusicView.as_view()),
    path('music/<int:music_id>/', MusicDetailView.as_view()),
]