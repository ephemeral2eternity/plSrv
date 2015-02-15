from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext, loader
from django.http import HttpResponse
import subprocess
from ping.models import RTTs

# Create your views here.
def index(request):
	nodes = RTTs.objects.all()
	node_num = nodes.count()
	template = loader.get_template('ping/rtts.html')
	context = RequestContext(request, {
		'node_num':node_num,
		'nodes':nodes,
	})
	return HttpResponse(template.render(context))

@csrf_exempt
def addRtts(request):
	if request.method == "POST":
		name = request.POST.get("name", "")
		az01 = float(request.POST.get("az01", ""))
		az02 = float(request.POST.get("az02", ""))
		az03 = float(request.POST.get("az03", ""))
		az04 = float(request.POST.get("az04", ""))
		az05 = float(request.POST.get("az05", ""))
		az06 = float(request.POST.get("az06", ""))
		az07 = float(request.POST.get("az07", ""))
		az08 = float(request.POST.get("az08", ""))
		az09 = float(request.POST.get("az09", ""))
		az10 = float(request.POST.get("az10", ""))
		aws01 = float(request.POST.get("aws01", ""))
		aws02 = float(request.POST.get("aws02", ""))
		aws03 = float(request.POST.get("aws03", ""))
		aws04 = float(request.POST.get("aws04", ""))
		aws05 = float(request.POST.get("aws05", ""))
		aws06 = float(request.POST.get("aws06", ""))
		aws07 = float(request.POST.get("aws07", ""))
		aws08 = float(request.POST.get("aws08", ""))
		gc01 = float(request.POST.get("gc01", ""))
		gc02 = float(request.POST.get("gc02", ""))
		gc03 = float(request.POST.get("gc03", ""))
		gc04 = float(request.POST.get("gc04", ""))
		gc05 = float(request.POST.get("gc05", ""))
		gc06 = float(request.POST.get("gc06", ""))
		gc07 = float(request.POST.get("gc07", ""))
		gc08 = float(request.POST.get("gc08", ""))
		gc09 = float(request.POST.get("gc09", ""))
		gc10 = float(request.POST.get("gc10", ""))
		gc11 = float(request.POST.get("gc11", ""))
		gc12 = float(request.POST.get("gc12", ""))
		gc13 = float(request.POST.get("gc13", ""))
		gc14 = float(request.POST.get("gc14", ""))
		gc15 = float(request.POST.get("gc15", ""))
		gc16 = float(request.POST.get("gc16", ""))
		nodeRTT = RTTs(name=name, gc01=gc01, gc02=gc02, gc03=gc03, gc04=gc04, gc05=gc05, gc06=gc06, gc07=gc07, gc08=gc08,gc09=gc09,gc10=gc10,gc11=gc11, gc12=gc12,gc13=gc13, gc14=gc14, gc15=gc15,gc16=gc16,az01=az01,az02=az02,az03=az03,az04=az04, az05=az05, az06=az06, az07=az07, az08=az08, az09=az09, az10=az10, aws01=aws01, aws02=aws02, aws03=aws03, aws04=aws04, aws05=aws05, aws06=aws06, aws07=aws07, aws08=aws08)
		nodeRTT.save()
	elif request.method == "GET":
		return HttpResponse("Please use POST method!!!")
