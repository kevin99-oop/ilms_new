from rest_framework import serializers
from . models import Approvals

class approvalsSerializers(serializers.ModelSerializer):
	class Meta:
		model=Approvals
		fields='__all__'

