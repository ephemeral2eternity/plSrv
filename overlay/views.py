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
from overlay.models import OverlayNode, Node, Edge
from overlay.lib.get_cache_agents import *

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


def get_edges(request):
	print("Entering edge function in overlay/views.py")
	edges = Edge.objects.all()
	edge_num = edges.count()
	print("There are " + str(edge_num) + " edges in the database to show!")
	template = loader.get_template('overlay/edges.html')
	return HttpResponse(template.render({'edges':edges, 'edge_num':edge_num}, request))

def get_nodes(request):
	nodes = Node.objects.all()
	node_ips = {}
	for node in nodes:
		node_ips[node.name] = node.ip
	response = HttpResponse(str(node_ips))
	response['Params'] = json.dumps(node_ips)
	return response

def get_overlay_nodes(request):
	overlay_nodes = OverlayNode.objects.all()
	node_ips = {}
	for node in overlay_nodes:
		node_ips[node.name] = node.ip
	print("Respond with updated overlay nodes: " + str(node_ips))
	response = HttpResponse(str(node_ips))
	response['Params'] = json.dumps(node_ips)
	return response

def get_zones(request):
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

# Add a node to the overlay network
def add(request):
	print("Entering overlay/add() function!")
	url = request.get_full_path()
	params = url.split('?')[1]
	to_add_dict = urllib.parse.parse_qs(params)
	print("Entering overlay/add() function to add " + params)
	if 'src' in to_add_dict.keys():
		src_name = to_add_dict['src'][0]
		if Node.objects.filter(name=src_name).exists() and (not OverlayNode.objects.filter(name=src_name).exists()):
			node_to_add = Node.objects.get(name=src_name)
			new_overlay_node = OverlayNode(name=node_to_add.name, ip=node_to_add.ip)
			new_overlay_node.save()
		if 'dst' in to_add_dict.keys():
			dst_name = to_add_dict['dst'][0]
			if Node.objects.filter(name=dst_name).exists():
				src_id = int(src_name.split('-')[1])
				dst_id = int(dst_name.split('-')[1])
				if src_id < dst_id:
					print("(", src_id, ", ", dst_id, ")")
					edge_id = src_id * 1000 + dst_id
					print(edge_id)
					print("Saving overlay egde from node:" + src_name + " to node:" + dst_name)
					edge = Edge(id=edge_id, src=node_name, dst=peer)
				else:
					print("(", dst_id, ", ", src_id, ")")
					edge_id = dst_id * 1000 + src_id
					print(edge_id)
					print("Saving overlay egde from node:" + dst_name + " to peer:" + src_name)
					edge = Edge(id=edge_id, src=dst_name, dst=src_name)
				edge.save()
	return get_edges(request)	


# Create your views here.
def initNodes(request):
	## Delete all exisitng nodes and rescan available nodes
	existing_nodes = Node.objects.all()
	existing_nodes.delete()
	gce_nodes = get_cache_agents()
	for n in gce_nodes:
		node_id = int(n['name'].split('-')[1])
		node_name = n['name']
		node_ip = n['ip']
		node_zone = n['zone']
		node_type = n['type']
		node = Node(id=node_id, name=node_name, ip=node_ip, zone=node_zone, type=node_type)
		node.save()
	return get_nodes(request)

def queryOverlay(request):
	prev_edges = Edge.objects.all()
	prev_edges.delete()
	gce_nodes = Node.objects.all()
	for node in gce_nodes:
		node_id = node.id
		node_ip = node.ip
		node_name = node.name
		print("Obtaining peers for cache agent:" + node_name)
		try:
			r = requests.get("http://" + node_ip + ":8615/overlay/query/")
			peer_str = r.headers['agens-peers']
			if peer_str:
				peers = peer_str.split(',')
				print(peers)
				for peer in peers:
					print(peer)
					peer_id = int(peer.split('-')[1])
					if node_id < peer_id:
						print("(", node_id, ", ", peer_id, ")")
						edge_id = node_id * 1000 + peer_id
						print(edge_id)
						print("Saving overlay egde from node:" + node_name + " to peer:" + peer)
						edge = Edge(id=edge_id, src=node_name, dst=peer)
					else:
						print("(", peer_id, ", ", node_id, ")")
						edge_id = peer_id * 1000 + node_id
						print(edge_id)
						print("Saving overlay egde from node:" + node_name + " to peer:" + peer)
						edge = Edge(id=edge_id, src=peer, dst=node_name)
					print("Saving edge to database")
					edge.save()
		except:
			pass
	return get_edges(request)


def initOverlay(request):
	print("Deleting the previous overlay nodes and edges!")
	prev_edges = Edge.objects.all()
	prev_edges.delete()
	prev_overlay_nodes = OverlayNode.objects.all()
	prev_overlay_nodes.delete()
	all_nodes = Node.objects.all()
	for node in all_nodes:
		node_name = node.name 
		node_ip = node.ip
		init_url = "http://%s:8615/overlay/init/"%node_ip
		connect_url = "http://%s:8615/overlay/connect/"%node_ip
		try:
			print("sending initialization request to " + node_name)
			r = requests.get(init_url)
			print(r)
		except:
			pass
		try:
			print("sending connect request to " + node_name)
			r = requests.get(connect_url)
			print(r)
		except:
			pass
	return get_edges(request)


def deleteOverlay(request):
	print("Deleting the previous overlay nodes and edges!")
	prev_edges = Edge.objects.all()
	prev_edges.delete()
	prev_overlay_nodes = OverlayNode.objects.all()
	prev_overlay_nodes.delete()
	return HttpResponse("Successfully delete the previous overlay network!")
	

def initManager(request):
	init_rsts = {}
	nodes = Node.objects.all()
	for n in nodes:
		node_name = n.name
		node_ip = n.ip
		isSuccess = init_manager(node_ip)
		init_rsts[node_name] = isSuccess
	return JsonResponse(init_rsts, safe=False)
