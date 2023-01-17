from django.shortcuts import render,redirect,HttpResponse
from app01.models import *

# Create your views here.

def depart_list(request):
    """部门列表"""
    department_list = Department.objects.all()
    return render(request,'depart_list.html',
                  {'dpt_list': department_list}
                  )


def depart_add(request):
    """部门增加"""
    if request.method == 'GET':
        return render(request,'depart_add.html')

    depart = request.POST.get('depart')
    Department.objects.create(title=depart)
    return redirect('/depart_list/')


def depart_delete(request):
    """部门删除"""
    nid = request.GET.get('nid')
    Department.objects.filter(id=nid).delete()
    return redirect('/depart_list/')


def depart_edit(request,nid):
    """部门修改"""
    if request.method == 'GET':
        query_data = Department.objects.filter(id=nid).first()
        row_data = query_data.title
        return render(request,'depart_edit.html',
                      {'title':row_data}
                      )

    new_depart = request.POST.get('depart')
    Department.objects.filter(id=nid).update(title=new_depart)
    return redirect('/depart_list/')


def user_list(request):
    """用户列表"""
    if request.method == 'GET':
        queryset = UserInfo.objects.all()
        # print(queryset)
        # print(dir(queryset))
        """
        for item in  queryset:
            print(item.name,item.password,
                  # 数据库中保存的时间类型为datatime类型，要将datatime类型格式化为字符串就需要.strftime方法
                  item.create_time.strftime("%Y-%m-%d"),
                  # 通过get_gender_display()方法直接可以获取choices数字所对应的值
                  item.get_gender_display(),
                  # 通过.depart（数据库中定义的字段），可以直接获得所关联的外键数据库表的记录
                  item.depart.title)
        """
        return render(request, 'user_list.html',
                      {'queryset':queryset}
                      )


def user_add(request):
    """用户添加 传统方法"""
    if request.method == 'GET':
        to_web_dict = {
            'gender':UserInfo.gender_choices,
            'depart':Department.objects.all()
        }
        print(Department.objects.all().values())
        return render(request,'user_add.html',to_web_dict)

    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    ac = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gender')
    depart = request.POST.get('depart')

    UserInfo.objects.create(name=name,password=pwd,age=age,accont=ac,
                            create_time=ctime,gender=gender,depart_id=depart)
    return redirect('/user_list/')

"""
form的实现方式
from django import forms
class UserForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput)
    pwd = forms.CharField(widget=forms.PasswordInput)
    ctime = forms.CharField(widget=forms.DateInput)


def user_add_form(request):
    form = UserForm
    return render(request,'user_add_form.html',{'form':form})
"""

from django import forms

class UserModelForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput,min_length=3)
    name = forms.CharField(min_length=3,label="姓名")

    class Meta:
        model = UserInfo
        fields = ['name','password','age','accont','create_time','gender','depart']
        widgets = {
            # 'name': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),   # 修改password字段的input标签类型为PasswordInput，并添加CSS样式
            # 'age': forms.TextInput(attrs={'class':'form-control'}),
            # 'create_time': forms.DateInput(attrs={'class':'form-control'}),
            # 'gender': forms.TypedChoiceField(attrs={'class':'form-control'}),
            # 'depart': forms.ModelChoiceField(attrs={'class':'form-control'})
        }

    # 给ModelForm生成的input标签添加CSS样式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name,field in self.fields.items():
            # print(name,field)
            field.widget.attrs = {'class':'form-control','placeholder':field.label}


def user_add_modelform(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request,'user_add_modelform.html',{'form':form})

    # 用户POST提交数据，数据校验
    form = UserModelForm(data=request.POST)

    if form.is_valid():
        print(form.cleaned_data)
        # 将数据保存至数据库
        form.save()
        return redirect('/user_list/')
    else:
        return render(request, 'user_add_modelform.html', {'form': form})

