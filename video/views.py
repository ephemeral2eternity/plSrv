import urllib.parse
import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from video.models import Cache
from video.content_caching import *

# Create your views here.
def index(request):
	return render_to_response("video/form.html")

def init_content_caching(request):
	url = request.get_full_path()
	params = url.split('?')[1]
	request_dict = urllib.parse.parse_qs(params)
	print(request_dict)
	if 'videoNum' in request_dict.keys():
		videoNum = int(request_dict['videoNum'][0])
	else:
		videoNum = 10
	if 'minCopy' in request_dict.keys():
		minCopy = int(request_dict['minCopy'][0])
	else:
		minCopy = 3

	if 'zipfParam' in request_dict.keys():
		zipfParam = float(request_dict['zipfParam'][0])
	else:
		zipfParam = 0.1
	existing_caches = Cache.objects.all()
	if existing_caches.count() > 0:
		existing_caches.delete()
	content_caching = initialize_content_caching(videoNum, zipfParam, minCopy)
	for srv in content_caching.keys():
		cached_videos = content_caching[srv]
		cached_videos_str = ', '.join(str(video_id) for video_id in cached_videos)
		newCache = Cache(server=srv, videos=cached_videos_str)
		newCache.save()
	return query(request)

def query(request):
	caches = Cache.objects.all()
	content_caching = {}
	for cache in caches:
		content_caching[cache.server] = cache.videos
	templates = loader.get_template('video/caches.html')
	response =  HttpResponse(templates.render({'caches':caches}, request))
	response['Params'] = json.dumps(content_caching)
	return response
