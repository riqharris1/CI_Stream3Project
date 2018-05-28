from rest_framework import serializers
from issueTracker.models import issueTracker
 
class issueTrackerSerializer(serializers.ModelSerializer):
    """
    Todo Serializer.
 
    Used to serialize the Todo model to JSON. The fields to be 
    serialized are:
    - id
    - title
    - description
    - status
    - updated
    """
 
    class Meta:
        model = issueTracker
        fields = ('id', 'title', 'description',
                  'status', 'updated')