#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from app01 import models


class HostModelForm(forms.ModelForm):
    class Meta:
        model = models.Host
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(HostModelForm, self).__init__(*args, **kwargs)
        # 统一给ModelForm生成字段添加样式
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
