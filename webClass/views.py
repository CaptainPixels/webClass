from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.middleware import csrf
from django.db import IntegrityError

from .models import Projects
from .forms import *

import os

def list(req):
    return render(req, 'webClass/project-list.html', {'projects':Projects.objects.all()})

def project(req, pk):
    return render(req, 'webClass/project-'+str(pk)+'/index.html', {'project':{'name':Projects.objects.get(pk=pk).name,'id':pk}})

class api():
    def csrf(req):
        csrf.get_token(req)
        return render(req, 'webClass/base.html')
    class project():
        def add(req):
            if req.method == 'POST':
                form = ProjectForm(req.POST)
                if form.is_valid():
                    #get form data
                    projName = form.cleaned_data['name']
                    #test for a duplicate entry
                    try:
                        #add object to database
                        Projects.objects.create(
                            name = projName
                        ).save()
                    except IntegrityError:
                        #return fail for duplicate object
                        return JsonResponse({'success':False,'reason':'name already exists'})
                    #get object that was created
                    proj = Projects.objects.get(name=projName)
                    #return success
                    os.system('cp -r /Users/edit/Documents/web/djangoServer/webClass/static/webClass/project-0 /Users/edit/Documents/web/djangoServer/webClass/static/webClass/project-'+str(proj.id))
                    os.system('cp -r /Users/edit/Documents/web/djangoServer/webClass/templates/webClass/project-0 /Users/edit/Documents/web/djangoServer/webClass/templates/webClass/project-'+str(proj.id))
                    return JsonResponse({'success':True,'name':proj.name,'id':proj.id})
                #return fail for bad form
                return JsonResponse({'success':False,'reason':'invalid form'})
            #return redirect if GET
            return HttpResponseRedirect('/webClass/projects')

        def setid(req):
            if req.method == 'POST':
                form = SetIdForm(req.POST)
                if form.is_valid():
                    projName = form.cleaned_data['name']
                    newId = form.cleaned_data['id']
                    try:
                        oldId = Projects.objects.get(name=projName).pk
                        print(oldId)
                        print(newId)
                    except Projects.DoesNotExist:
                        return JsonResponse({'success':False,'reason':'name does not exist'})
                    Projects.objects.get(name=projName).delete()
                    try:
                        Projects.objects.create(
                        name=projName,
                        pk=newId
                        ).save
                    except ValueError:
                        return JsonResponse({'success':False,'reason':'id must be an int'})
                    oldId = str(oldId)
                    os.system('mv /Users/edit/Documents/web/djangoServer/webClass/templates/webClass/project-'+ oldId + ' /Users/edit/Documents/web/djangoServer/webClass/templates/webClass/project-'+ newId)
                    os.system('mv /Users/edit/Documents/web/djangoServer/webClass/static/webClass/project-'+ oldId + ' /Users/edit/Documents/web/djangoServer/webClass/static/webClass/project-'+ newId)
                    return JsonResponse({'success':True})
                return JsonResponse({'success':False,'reason':'invalid form'})


        def delete(req):
            if req.method == 'POST':
                form = ProjectForm(req.POST)
                if form.is_valid():
                    projName = form.cleaned_data['name']
                    try:
                        projId = str(Projects.objects.get(name=projName).id)
                        Projects.objects.get(name=projName).delete()
                    except Projects.DoesNotExist:
                        return JsonResponse({'success':False,'reason':'project does not exist'})
                    os.system('mkdir /Users/edit/Documents/web/djangoServer/webClass/archived/'+projId)
                    os.system('mv /Users/edit/Documents/web/djangoServer/webClass/templates/webClass/project-'+ projId +' /Users/edit/Documents/web/djangoServer/webClass/archived/'+ projId + '/templates')
                    os.system('mv /Users/edit/Documents/web/djangoServer/webClass/static/webClass/project-'+ projId +' /Users/edit/Documents/web/djangoServer/webClass/archived/'+ projId + '/static')
                    return JsonResponse({'success':True})
                return JsonResponse({'success':False,'reason':'invalid form'})

    class archive():
        def delete(req):
            if req.method == 'POST':
                form = ArchiveForm(req.POST)
                if form.is_valid():
                    projId = form.cleaned_data['id']
                    if projId == 'all':
                        projId = '*'
                    os.system('rm -rf /Users/edit/Documents/web/djangoServer/webClass/archived/'+ projId)
                    return JsonResponse({'success':True})
                return JsonResponse({'success':False,'reason':'invalid form'})
