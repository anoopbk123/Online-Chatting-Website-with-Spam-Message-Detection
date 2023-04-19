from django.db import models
# from user_reg.models import UserReg

# Create your models here.
class UserReg(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    phno = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    profile_photo = models.CharField(max_length=100)
    # photo= models.ForeignKey(UserReg, to_field='user_id', on_delete=models.CASCADE, related_name='f1')
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_reg'

