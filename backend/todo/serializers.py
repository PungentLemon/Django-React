from rest_framework import serializers
from .models import Todo

# In the code snippet below, we specified the model to work with and the fields we want to be converted to JSON
# We use "class Meta" to provide more information about specific class. In this case it gives more information about Todo class inside Model
class TodoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Todo
        fields = ('id', 'title', 'description', 'completed')