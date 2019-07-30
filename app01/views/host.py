#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from app01.forms.host import HostModelForm
from rbac.service.urls import memory_reverse


def host_list(request):
    host_queryset = models.Host.objects.all()
    return render(request, 'host_list.html', {"host_queryset": host_queryset})


def host_add(request):
    if request.method == 'GET':
        form = HostModelForm()
        return render(request, 'rbac/change.html', {'form': form})

    form = HostModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'host_list'))

    return render(request, 'rbac/change.html', {'form': form})


def host_edit(request, pk):
    obj = models.Host.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('主机不存在')
    if request.method == 'GET':
        form = HostModelForm(instance=obj)
        return render(request, 'rbac/change.html', {'form': form})

    form = HostModelForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'host_list'))

    return render(request, 'rbac/change.html', {'form': form})


def host_del(request, pk):
    origin_url = memory_reverse(request, 'host_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': origin_url})

    models.Host.objects.filter(id=pk).delete()
    return redirect(origin_url)
