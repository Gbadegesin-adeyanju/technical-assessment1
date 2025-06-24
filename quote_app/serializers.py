from rest_framework.serializers import ModelSerializer
from .models import Quote

class QuoteSerializers(ModelSerializer):
    class Meta:
        model = Quote
        fields = ['text']