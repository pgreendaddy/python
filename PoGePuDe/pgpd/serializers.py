from rest_framework import serializers
from . models import Devices
from django.contrib.auth.models import User

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id','username', 'email', 'first_name','last_name')
class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Devices
        fields = ('id','devicename','devicemodel','devicedsc','devicestatus')
        
        #feilds='__all__'



