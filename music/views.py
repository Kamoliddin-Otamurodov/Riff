from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Artist , Album , Music, User

from .serializers import AlbumSerializer , ArtistSerializer , MusicSerializer , UserSerializer

class UserView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request) -> Response:
        customer = User.objects.all()

        serializer = UserSerializer(customer, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(self, request: Request, user_id: int) -> Response:
        customer = User.objects.get(id=user_id)

        serializer = UserSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, user_id: int) -> Response:
        data = request.data

        task = User.objects.get(id=user_id)

        serializer = UserSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, user_id: int) -> Response:
        task = User.objects.get(id=user_id)
        task.delete()

        return Response({'message': 'deleted.'})
    

class ArtistView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request) -> Response:
        tasks = Artist.objects.all()

        serializer = ArtistSerializer(tasks, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = ArtistSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistDetailView(APIView):
    def get(self, request: Request, artist_id : int) -> Response:
        customer = Artist.objects.get(id = artist_id)

        serializer = ArtistSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, artist_id : int) -> Response:
        data = request.data

        task = Artist.objects.get(id = artist_id)

        serializer = ArtistSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, artist_id : int) -> Response:
        task = Artist.objects.get(id = artist_id)
        task.delete()

        return Response({'message': 'deleted.'})
    

class AlbumView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request , artist_id : int) -> Response:
        customer = Album.objects.filter(artist_id=artist_id)

        serializer = AlbumSerializer(customer, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request , artist_id : int) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = AlbumSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetailView(APIView):
    def get(self, request: Request, artist_id : int , album_id: int) -> Response:
        customer = Album.objects.get(id=album_id  , artist_id=artist_id)

        serializer = AlbumSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, artist_id : int , album_id: int) -> Response:
        data = request.data

        task = Album.objects.get(id=album_id  , artist_id=artist_id)

        serializer = AlbumSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        

    def delete(self, request: Request, artist_id : int , album_id: int) -> Response:
        task = Album.objects.get(id=album_id  , artist_id=artist_id)
        task.delete()

        return Response({'message': 'deleted.'})
    
    from rest_framework.views import APIView
    

class MusicView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request , artist_id : int ,album_id : int) -> Response:
        customer = Music.objects.filter(album_id = album_id)

        serializer = MusicSerializer(customer, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request , artist_id : int,album_id : int) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = MusicSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MusicDetailView(APIView):
    def get(self, request: Request, artist_id : int ,album_id : int, music_id : int) -> Response:
        customer = Music.objects.get(album_id = album_id , id=music_id)

        serializer = MusicSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, artist_id : int ,album_id : int, music_id : int) -> Response:
        data = request.data

        task = Music.objects.get(album_id = album_id , id=music_id)

        serializer = MusicSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        

    def delete(self, request: Request, artist_id : int ,album_id : int, music_id : int) -> Response:
        task = Music.objects.get(album_id = album_id , id=music_id)
        task.delete()

        return Response({'message': 'deleted.'})

