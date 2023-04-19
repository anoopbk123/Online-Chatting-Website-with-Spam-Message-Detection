from django.db import models
from user_reg.models import UserReg
from reported_comments.models import ReportedComments
# Create your models here.
class Friends(models.Model):
    friend_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user = models.ForeignKey(UserReg,to_field='user_id',on_delete=models.CASCADE,related_name='f1')
    # report= models.ForeignKey(ReportedComments, to_field='user_id', on_delete=models.CASCADE, related_name='f1')
    # f_user_id = models.IntegerField()
    f_user=models.ForeignKey(UserReg,to_field='user_id',on_delete=models.CASCADE,related_name='f2')
    request_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'friends'

