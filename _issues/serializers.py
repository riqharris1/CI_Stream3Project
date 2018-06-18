from rest_framework import serializers
from issues.models import issue
 
 
class issueSerializer(serializers.ModelSerializer):
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
        model = Todo
        fields = ('id', 'title', 'description',
                  'status', 'updated')