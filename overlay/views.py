from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext, loader
from django.http import HttpResponse
import requests
import json
import re
from overlay.models import Node, Edge
from overlay.lib.get_cache_agents import *

# Create your views here.
def index(request):
	## Delete all exisitng nodes and rescan available nodes
	existing_nodes = Node.objects.all()
	existing_nodes.delete()
	gce_nodes = get_cache_agents()
	node_ips = get_cache_agent_ips()
	prev_edges = Edge.objects.all()
	prev_edges.delete()
	for n in gce_nodes:
		node_id = int(n['name'].split('-')[1])
		node_name = n['name']
		node_ip = n['ip']
		r = requests.get("http://" + node_ip + ":8615/overlay/query/")
		peer_str = r.headers['agens-peers']
		print(peer_str)
		peers = peer_str.split(',')
		for peer in peers:
			peer_id = int(peer.split('-')[1])
			print("(", node_id, ", ", peer_id, ")")
			if node_id < peer_id:
				edge_id = node_id * 1000 + peer_id
				print(edge_id)
				edge = Edge(id=edge_id, src=node_name, dst=peer)
			else:
				edge_id = peer_id * 1000 + node_id
				print(edge_id)
				edge = Edge(id=edge_id, src=peer, dst=node_name)
			edge.save()
		node_zone = n['zone']
		node_type = n['type']
		node = Node(id=node_id, name=node_name, ip=node_ip, zone=node_zone, type=node_type)
		node.save()
	return query(request)

@csrf_exempt
def query(request):
	nodes = Node.objects.all()
	node_ips = {}
	for node in nodes:
		node_ips[node.name] = node.ip
	node_num = nodes.count()
	template = loader.get_template('overlay/index.html')
	context = RequestContext(request, {
			'nodes' : nodes,
			'node_num' : node_num,
		})
	response = HttpResponse(template.render(context))
	response['Params'] = json.dumps(node_ips)
	return response

def edge(request):
	print("Entering edge function in overlay/views.py")
	edges = Edge.objects.all()
	edge_num = edges.count()
	template = loader.get_template('overlay/edges.html')
	context = RequestContext(request, {'edges':edges, 'edge_num':edge_num})
	return HttpResponse(template.render(context))

def node(request):
	nodes = Node.objects.all()
	node_ips = {}
	for node in nodes:
		node_ips[node.name] = node.ip
	response = HttpResponse(str(node_ips))
	response['Params'] = json.dumps(node_ips)
	return response

def zone(request):
	nodes = Node.objects.all()
	node_zones = {}
	for node in nodes:
		node_zones[node.name] = node.zone
	response = HttpResponse(str(node_zones))
	response['Params'] = json.dumps(node_zones)
	return response
