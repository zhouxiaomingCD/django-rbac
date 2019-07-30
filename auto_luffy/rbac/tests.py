from django.test import TestCase

# Create your tests here.

# 首先导入ModelForm
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError

# 在视图函数中，定义一个类，比如就叫StudentListModelForm，这个类要继承ModelForm，在这个类中再写一个原类Meta（规定写法，并注意首字母是大写的）
# 在这个原类中，有以下属性（部分）：

class StudentListModelForm(ModelForm):
    confirm_password = forms.CharField(label='确认密码')  # 如果要增加显示字段，在这里增加

    class Meta:
        model = Student  # 对应的Model中的类
        fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段。否则用['title', 'icon']指定字段
        exclude = None  # 排除的字段
        # error_messages用法：
        error_messages = {
            'name': {'required': "用户名不能为空", },
            'age': {'required': "年龄不能为空", },
        }
        # widgets用法,比如把输入用户名的input框改为Textarea
        from django.forms import widgets as wid  # 首先得导入模块因为重名，所以起个别名
        widgets = {"name": wid.Textarea(attrs={"class": "c1"})}  # 还可以自定义属性
        labels = {"name": "用户名"}  # labels，自定义在前端显示的名字
        help_texts = None  # 帮助提示信息

    def __init__(self, *args, **kwargs):  # 给每个标签添加属性
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):  # 钩子函数
        """
        检测密码是否一致
        :return:
        """
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('两次密码输入不一致')
        return confirm_password

# <pre><code>
# </code></pre>