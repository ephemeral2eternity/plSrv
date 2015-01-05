from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext, loader
from django.http import HttpResponse
from hello.models import PLCSite, PLCNode, GeoSite
from djgeojson.fields import PointField
#from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.core.serializers import serialize
#from hello.models import PLCSite, GeoSite
#from django.contrib.gis.geos import Point

# Create your views here.
def index(request):
	return HttpResponse("Please come back later!")

@csrf_exempt
def addnode(request):
	#print("Call addnode function in hello/views.py")
	if request.method == "POST":
		plc_node_id = int(request.POST.get("node_id", ""))
		print(plc_node_id)
		plc_node_name = request.POST.get("hostname", "")
		plc_node_site_id = int(request.POST.get("site_id", ""))
		plc_node_site = PLCSite.objects.get(pk=plc_node_site_id)
		#print(plc_node_site)
		plc_node_site_name = plc_node_site.site_name
		#print(plc_node_site_name)
		plc_node_type = request.POST.get("node_type", "")
		#print(plc_node_type)
		plc_node = PLCNode(id=plc_node_id, name=plc_node_name, site_id=plc_node_site_id, site=plc_node_site_name, node_type=plc_node_type)
		plc_node.save()
		#print("Successfully save the node!")
	elif request.method == "GET":
		plc_nodes = PLCNode.objects.all()
		node_num = plc_nodes.count()
		template = loader.get_template('hello/nodes.html')
		context = RequestContext(request, {
			'plc_nodes':plc_nodes,
			'node_num':node_num,
		})
		return HttpResponse(template.render(context))

@csrf_exempt
def addsite(request):
	print("Call add function in hello/views.py")
	if request.method == "POST":
		plc_site_id = int(request.POST.get("site_id", ""))
		plc_site_name = request.POST.get("name", "")
		plc_site_url = request.POST.get("url", "")
		plc_site_login = request.POST.get("login_base", "")
		plc_site_latitude = float(request.POST.get("latitude", ""))
		plc_site_longitude = float(request.POST.get("longitude", ""))
		print(plc_site_name)
		plc_site = PLCSite(id=plc_site_id, site_name=plc_site_name, site_url=plc_site_url, site_login_base=plc_site_login, site_longitude=plc_site_longitude, site_latitude=plc_site_latitude)
		plc_site.save()
	elif request.method == "GET":
		plc_sites = PLCSite.objects.all()
		site_num = plc_sites.count()
		template = loader.get_template('hello/sites.html')
		context = RequestContext(request, {
			'plc_sites':plc_sites,
			'site_num':site_num,
		})
		return HttpResponse(template.render(context))
		
def site_detail(request, site_id):
	try:
		plc_site = PLCSite.objects.get(id=site_id)
	except PLCSite.DoesNotExist:
		raise Http404
	return render(request, 'hello/site_detail.html', {'plc_site' : plc_site})

def node_detail(request, node_id):
	try:
		plc_node = PLCNode.objects.get(id=node_id)
	except PLCNode.DoesNotExist:
		raise Http404
	return render(request, 'hello/node_detail.html', {'plc_node' : plc_node})

def map(request):
	plc_sites = PLCSite.objects.all()
	for site in plc_sites:
		lng = float(site.site_longitude)
		lat = float(site.site_latitude)
		geom = PointField(lng, lat)
		geo_obj = GeoSite(geom=geom)
		geo_obj.save()
	#	print("Save coordinates for site: %s", site.site_name)
	#gsites = GeoJSONSerializer().serialize(GeoSite.objects.all(), use_natural_keys=True)
	gsites = GeoSite.objects.all()
	return render(request, 'hello/map.html', {'geo_sites':gsites})
