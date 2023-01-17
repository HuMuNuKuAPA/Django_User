from django.db import models


# Create your models here.

class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='部门名称', max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    accont = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='入职时间')

    # 外键约束
    #   to= 后面跟的是需要外键连接的表
    #   to_field= 后面跟的是外键链接的值
    # 当部门表中的值被删除，员工表会有两种表现
    #   1. on_delete=models.CASCADE 级联删除
    #   2. on_delete=models.SET_NULL 将值置为空

    depart = models.ForeignKey(verbose_name='部门',to='Department', to_field='id', on_delete=models.CASCADE)
    # depart = models.ForeignKey(to='Department', to_field='id',
    #                            null=True,
    #                            blank=True,
    #                            on_delete=models.SET_NULL,
    #                            )

    # django特有的约束，在数据库表的记录中，对这个gender字段可以记录的值为1或者2，而1和2所表示的意思是在gender_choices
    # 中规定的
    gender_choices = (
        (1,'男'),
        (2,'女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)
