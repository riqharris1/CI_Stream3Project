from rest_framework import serializers
from todo.models import Todo
from django.contrib.auth.models import User
 
class TodoSerializer(serializers.ModelSerializer):
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
        fields = ('id', 'type', 'title', 'description',
                  'status', 'updated')