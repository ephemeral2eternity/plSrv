from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
import subprocess
import csv
from hello.models import PLCSite, PLCNode
# from djgeojson.fields import PointField
#from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.core.serializers import serialize
#from hello.models import PLCSite, GeoSite
#from django.contrib.gis.geos import Point

# Create your views here.
def index(request):
#	return HttpResponse("Please come back later!")
	return render_to_response("hello/index.html")

@csrf_exempt
def addnode(request):
	#print("Call addnode function in hello/views.py")
	if request.method == "POST":
		plc_node_id = int(request.POST.get("node_id", ""))
		print(plc_node_id)
		plc_node_name = request.POST.get("hostname", "")
		plc_node_zone = request.POST.get("zone", "")
		plc_node_region = request.POST.get("region", "")
		plc_node_site_id = int(request.POST.get("site_id", ""))
		plc_node_os = request.POST.get("node_os", "")
		plc_node_python = request.POST.get("node_python", "")
		plc_node_ip = request.POST.get("node_ip", "")
		plc_node_site = PLCSite.objects.get(pk=plc_node_site_id)
		p = subprocess.Popen("whois -h whois.cymru.com \" -v " + plc_node_ip + "\"", stdout=subprocess.PIPE, shell=True)
		plc_node_as = p.communicate()[0]
		#print(plc_node_site)
		plc_node_site_name = plc_node_site.site_name
		#print(plc_node_site_name)
		plc_node_type = request.POST.get("node_type", "")
		#print(plc_node_type)
		plc_node = PLCNode(id=plc_node_id, node_ip=plc_node_ip, name=plc_node_name, zone=plc_node_zone, region=plc_node_region, site_id=plc_node_site_id, site=plc_node_site_name, node_type=plc_node_type, node_os=plc_node_os, node_python=plc_node_python, node_as=plc_node_as)
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
def asLookup(request):
	print("Call asLookup function in hello/views.py")
	nodes = PLCNode.objects.all()
	template = loader.get_template('hello/ases.html')
	context = RequestContext(request, {
		'nodes' : nodes,
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
		cur_nodes = PLCNode.objects.filter(site_id=site_id)
	except PLCSite.DoesNotExist:
		raise Http404
	return render(request, 'hello/site_detail.html', {'plc_site' : plc_site,
							  'cur_nodes' : cur_nodes,})

def node_detail(request, node_id):
	try:
		plc_node = PLCNode.objects.get(id=node_id)
	except PLCNode.DoesNotExist:
		raise Http404
	return render(request, 'hello/node_detail.html', {'plc_node' : plc_node})

def get_coordinates(request):
	# Create the HttpResponse object with the appropriate CSV header
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="coordinates.csv"'

	writer = csv.writer(response)
	writer.writerow(['ID', 'Name', 'Latitude', 'Longitude'])

	for site in PLCSite.objects.all():
		writer.writerow([site.id, site.site_name, site.site_latitude, site.site_longitude])
	return response

def get_node_csv(request):
	# Create the HttpResponse object with the appropriate CSV header
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="nodes.csv"'

	writer = csv.writer(response)
	writer.writerow(['ID', 'Name', 'Site_ID', 'Site', 'IP', 'Google Zone', 'Google Region'])

	for node in PLCNode.objects.all():
		writer.writerow([node.id, node.name, node.site_id, node.site, node.node_ip, node.zone, node.region])
	return response

'''
def map(request):
	plc_sites = PLCSite.objects.all()
	for site in plc_sites:
		lng = float(site.site_longitude)
		lat = float(site.site_latitude)
		geom = PointField(lng, lat)
		geo_obj = GeoSite(geom=geom)
		geo_obj.save()
	#	print("Save coordinates for site: %s", site.site_name)
	#gsites = GeoJS`ONSerializer().serialize(GeoSite.objects.all(), use_natural_keys=True)
	gsites = GeoSite.objects.all()
	return render(request, 'hello/map.html', {'geo_sites':gsites})
'''
