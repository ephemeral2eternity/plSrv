import random
from overlay.models import Node

def generate_zipf(video_num, zipf_param):
	zipf_prob = {}
	prob_sum = 0.0
	for k in range(1, video_num+1):
		zipf_prob[k] = k ** (-zipf_param)
		prob_sum += zipf_prob[k]
	
	for k in zipf_prob.keys():
		zipf_prob[k] = zipf_prob[k]/prob_sum

	return zipf_prob

def initialize_content_caching(video_num, zipf_param, min_copy):
	zipf_prob = generate_zipf(video_num, zipf_param)
	nodes = Node.objects.all()
	max_copy = nodes.count()
	all_nodes = []
	for node in nodes:
		all_nodes.append(node.name)
	max_zipf_prob = max(zipf_prob.keys())
	min_zipf_prob = min(zipf_prob.keys())
	
	content_caching = {}
	for srv in all_nodes:
		content_caching[srv] = []

	for k in zipf_prob.keys():
		cur_zipf_prob = zipf_prob[k]
		cached_copy_num = round((max_copy - min_copy) * (cur_zipf_prob - min_zipf_prob) / (max_zipf_prob - min_zipf_prob) + min_copy)
		
		# Randomly select cached_copy_num servers to cache k video
		cached_servers = random.sample(all_nodes, cached_copy_num)
		for srv in cached_servers:
			content_caching[srv].append(k)

	return content_caching
