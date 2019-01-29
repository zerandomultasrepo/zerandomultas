from rest_framework import serializers
from server.models import Occurrence


class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ('full_name', 'email', 'plan', 'phone', 'description', 'traffic_ticket', 'drivers_licence', 'dut_copy',
                  'value')
