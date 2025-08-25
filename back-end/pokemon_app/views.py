#pokemon_app/views.py
from .models import Pokemon #imports the Pokemon model
from .serializers import PokemonSerializer #imports the PokemonSerializer
from django.http import JsonResponse # Our responses will now be returned in JSON so we should utilize a JsonResponse
# Import both APIView and Response from DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MoveSerializer

# Create your views here.

# def all_pokemon(request):
#     pokemon = PokemonSerializer(Pokemon.objects.order_by('name'), many=True) # Utilize the serializer to serialize all of our Pokemon pulled from the Database
#     return JsonResponse({"pokemon": pokemon.data}) # JSON could only be interpreted in dictionary format so we need to ensure our response is a dictionary itself.



class All_moves(APIView):
    def get(self, request):
        moves = MoveSerializer(Move.objects.order_by('name'), many=True)
        return Response(moves.data)

    
class A_pokemon(APIView):
    
    #  Specify the method to trigger this behavior
    def get(self, request, id): # <-- Notice id is now a parameter and its value is being pulled straight from our URL
        # Lets initialize pokemon as None and give it a
        # corresponding query set depending on the ids type
        pokemon = None
        if type(id) == int: # the to_python method from the converter will return the correct type here
            pokemon = Pokemon.objects.get(id = id)
        else:
            pokemon = Pokemon.objects.get(name = id.title()) # <== We only accept names in Title format so lets use the `title` method to ensure we have the user input in the correct format
        return Response(PokemonSerializer(pokemon).data) #<=== Finally lets use the PokemonSerializer to return our Pokemon in the correct Format for Front End frameworks
    