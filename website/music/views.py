#from django.http import HttpResponse, Http404
#from django.template import loader	
from .models import Album, Song
from django.shortcuts import render, get_object_or_404


def index(request):
	all_albums = Album.objects.all() #extracting the database
	#template = loader.get_template('music/index.html')
	html_pass = {'all_albums' : all_albums}
	return render(request, 'music/index.html', html_pass)


def details(request, album_id):
	#try:
		#album = Album.objects.get(pk=album_id)
	#except Album.DoesNotExist:
		#raise Http404("Fu*k You,, Album doesn't exist") #raising a 404 error if id not found
	#using shortcut
	album = get_object_or_404(Album, pk = album_id)
	return render(request, 'music/details.html', {'album': album})

def favourite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError, song.DoesNotExist):
		return render(request, 'music/details.html',
					  {
						  'album' : album,
						  'error_mesage' : "You didn not select a valid song",
					  })
	else:
		selected_song.is_favourite = True
		selected_song.save()
		return render(request, 'music/details.html', {'album': album})








