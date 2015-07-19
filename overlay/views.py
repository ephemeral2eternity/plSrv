from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import urllib
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
		try:
			r = requests.get("http://" + node_ip + ":8615/overlay/query/")
			peer_str = r.headers['agens-peers']
			print(peer_str)
			if peer_str:
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
		except:
			pass
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

# Show the overlay graph in D3.js
def graph(request):
	return render_to_response("overlay/graph.html")

# Providing the D3.js JSON file from database in /overlay/graph/ request
def overlay_json(request):
	# Nodes should be sorted according to IDs.
	nodes = Node.objects.all().order_by('pk')
	zones = Node.objects.values_list('zone', flat=True).distinct()
	graph = {}
	nodes_json = []
	edges_json = []
	# Changing zone names to categorical numbers
	for node in nodes:
		cur_node_json = {}
		cur_node_json["name"] = node.name
		cur_node_json["group"] = sorted(zones).index(node.zone)
		nodes_json.append(cur_node_json)
	# Update edges according to edges_json
	edges = Edge.objects.all()
	for edge in edges:
		# Update edge's source and dst as node IDs.
		src, dst = divmod(edge.id, 1000)
		cur_edge = {}
		cur_edge["source"] = src - 1
		cur_edge["target"] = dst - 1
		cur_edge["value"] = 5
		edges_json.append(cur_edge)
	# Return nodes and edges as values
	graph["nodes"] = nodes_json
	graph["links"] = edges_json
	return JsonResponse(graph, safe=False)
	# return graph
