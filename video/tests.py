from django.test import TestCase
from video.content_caching import *

# Create your tests here.
video_num = 20
zipf_param = 0.1
min_copy = 2
content_caching = init_content_caching(video_num, zipf_param, min_copy)
print(content_caching)
