from django.db import models
from user_reg.models import UserReg
# from friends.models import Friends
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    # friend_id = models.IntegerField()
    # friend=models.ForeignKey(UserReg,to_field='user_id',on_delete=models.CASCADE,related_name='abcd')
    friend=models.ForeignKey(UserReg,to_field='user_id',on_delete=models.CASCADE,related_name='ff1')
    # user_id = models.IntegerField()
    user=models.ForeignKey(UserReg,to_field='user_id',on_delete=models.CASCADE,related_name='ff2')
    chat = models.CharField(max_length=160)
    photo = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'chat'
