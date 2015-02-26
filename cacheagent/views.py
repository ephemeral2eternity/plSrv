import urllib.parse
import json
import os
import time
import ntpath
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from cacheagent.models import CacheAgent
from cacheagent.gcs_upload import *

# Create your views here.
def index(request):
	agents = CacheAgent.objects.all()
	agent_num = agents.count()
	template = loader.get_template('cacheagent/clients.html')
	context = RequestContext(request, {
			'agents' : agents,
			'agentNum' : agent_num,
	})
	return HttpResponse(template.render(context))

@csrf_exempt
def add(request):
	url = request.get_full_path()
	params = url.split('?')[1]
	param_dict = urllib.parse.parse_qs(params)
	if 'client' in param_dict.keys() and 'cache_agent' in param_dict.keys():
		rcv_client = param_dict['client'][0]
		rcv_cache_agent = param_dict['cache_agent'][0]
		new_agent = CacheAgent(client=rcv_client, cache_agent=rcv_cache_agent)
		new_agent.save()
		return HttpResponse('Successfully add cache agent for client ' + rcv_client + '!!!')
	else:
		return HttpResponse('The url to add cache agent should contain both client and cache_agent!!!')

@csrf_exempt
def dump(request):
	all_agents = CacheAgent.objects.all()
	cache_agents = {}

	for agent in all_agents:
		cache_agents[agent.client] = agent.cache_agent

	cur_file_path = os.path.realpath(__file__)
	cur_path, cur_file_name = ntpath.split(cur_file_path)
	ts = time.strftime('%m%d%H%M')

	agents_file = cur_path + '/tmp/cache_agents_' + ts + '.json'
	with open(agents_file, 'w') as outfile:
		json.dump(cache_agents, outfile, sort_keys=True, indent=4, ensure_ascii=False)

	gcs_upload('agens-data', agents_file)

	all_agents.delete()
	return HttpResponse('Successfully dump all cache agent info!')
