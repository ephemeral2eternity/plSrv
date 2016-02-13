import json
import re
import os
import subprocess
import urllib.request
import urllib.parse
import socket
import ipgetter

def get_cache_agents():
	# List all instances
	cur_file_folder = os.path.dirname(os.path.realpath(__file__))
	cmd_to_list_files = cur_file_folder + '/list_servers.sh ' + cur_file_folder + '/accounts.csv cache'
	proc = subprocess.Popen(cmd_to_list_files, stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print("All instances:")
	print(out)
	cache_agents = []
	if out:
		lines = out.splitlines()
		for line in lines:
			lineStr = str(line, encoding='utf8')
			items = lineStr.split(",")
			node = {}
			node['name'] = items[0]
			node['zone'] = items[1]
			node['type'] = items[2]
			node['ip'] = items[3]
			cache_agents.append(node)

	return cache_agents

def get_cache_agent_ips(cache_agents):
	# List all instances
	agent_ips = {}
	for node in cache_agents:
		agent_ips[node['name']] = node['ip']

	return agent_ips

def init_manager(cache_ip):
	# List all instances
	myIP = ipgetter.myip()
	url = "http://%s:8615/overlay/initManager?%s" % (cache_ip, myIP)
	print(url)
	try:
		rsp = urllib.request.urlopen(url, timeout=10)
		print(rsp.read())
		return True
	except:
		return False

if __name__ == "__main__":
	cache_agents = get_cache_agents()
	cache_ips = get_cache_agent_ips(cache_agents)
	print(cache_agents)
	print(cache_ips)
	for cache_name in cache_ips.keys():
		cache_ip = cache_ips[cache_name]
		isSuccess = init_manager(cache_ip)
		if isSuccess:
			print("Successfully initialize this server as the manager to cache agent ", cache_ip)
		else:
			print("Failed to this server as the manager to cache agent ", cache_ip)	
