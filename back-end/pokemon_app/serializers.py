# pokemon_app/serializers.py
from rest_framework import serializers # import serializers from DRF
from .models import Pokemon # import Pokemon model from models.py
from .models import Move

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon # specify what model this serializer is for
        fields = ['id', 'name', 'level'] # specify the fields you would like this serializer to return
        
        
class MoveSerializer(serializers.ModelSerializer):
    pokemon = serializers.SerializerMethodField()

    class Meta:
        model = Move
        fields = ['id', 'name', 'power', 'accuracy', 'pokemon']

    def get_pokemon(self, obj):
        pokemon = obj.pokemon.all()
        pokemon = [x.name for x in pokemon]
        return pokemon