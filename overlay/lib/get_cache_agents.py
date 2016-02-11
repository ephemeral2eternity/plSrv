import json
import re
import os
import subprocess

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

if __name__ == "__main__":
	cache_agents = get_cache_agents()
	cache_ips = get_cache_agent_ips(cache_agents)
	print(cache_agents)
	print(cache_ips)
