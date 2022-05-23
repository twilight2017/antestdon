from django.contrib.auth.models import AbstractUser
from django.db import models


class AlertUser(AbstractUser):
    """Filed.null:如果是True, Django将在数据库中存储空值为NULL
       如果希望在表单中允许空值，还需要设置blank=True,因为null只影响数据库的存储
       设置blan=True 代表允许该字段为空"""
    revision = models.IntegerField(db_column="REVISION", blank=True, null=True)
    created_by = models.CharField(db_column='CREATED_BY', blank=True, null=True)
    """class DateTimeField 在python中用一个datetime.datetime表示
    auto_now_add:第一次创建对象时，自动将该字段设置为现在，对创建时间戳很有用"""
    created_time = models.DateTimeField(
        db_column='CREATE_TIME', auto_now_add=True, blank=True, null=True
    )
    updated_by = models.CharField(db_column='UPDATED_BY', blank=True, null=True)
    """DateField.auto_now: 每次保存对象时，自动将该字段设置为现在，对于“最后修改”的时间戳很有效"""
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)
    id = models.AutoField(primary_key=True)  # class AutoField 一个IntegerField，根据可用的ID自动递增
    name = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    department = models.CharField(max_length=128, blank=True, null=True)

    # update data
    def update(self, data: dict):
        self.name = data.get('name')
        self.phone = data.get('phone')
        self.email = data.get('email')
        self.department = data.get('department')
        self.save()

    def to_dict(self):
        return {
            "uid": self.id,
            "username": self.username,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "department": self.department
        }