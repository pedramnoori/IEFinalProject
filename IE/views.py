from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from IE.models import Game, GameData
from IE.serializers import GameSerializer
from IEProject.settings import onlineUsers, games
from UserManagment.permissions import Authenticate, AuthenticateUser
import json
import random


class Home(APIView):

    def get(self, request):
        return render(request, 'pages/index.html', {'onlineuser': onlineUsers, 'summary': request.user})


class gameDesign(APIView):

    permission_classes = (Authenticate,)
    authentication_classes = (AuthenticateUser,)
    def get(self, request):
        return render(request, 'pages/game.html',)


    def post(self, request):
        serial = GameSerializer(data=request.data)
        serial.is_valid(raise_exception=True)
        g = Game(**serial.validated_data)
        g.user = request.user
        g.save()
        return Response("Done")

class newgame(APIView):

    permission_classes = (Authenticate,)
    authentication_classes = (AuthenticateUser,)

    def get(self, request):
        return render(request, 'pages/newgame.html',{'games': Game.objects.all()})

class GameView(APIView):

    authentication_classes = (AuthenticateUser,)
    # permission_classes = (Authenticate,)

    def get(self, request):
        game_id = request.query_params.get('id')
        if game_id:
            game = Game.objects.get(id=game_id)
            new_game = GameData(game.diceNumber, game.maxScore, [int(x) for x in game.holdDices.split(',')])
            games[new_game.id] = new_game
            return render(request, 'pages/Internet.html', {'games': game, 'id': new_game.id})
        raise NotFound('Game not found!')

    def post(self, request):
        action = request.data.get('action')
        game_id = request.data.get('game_id')
        if not game_id:
            raise ValidationError('game_id not found')
        if not action:
            raise ValidationError('action not found')
        game: GameData = games.get(game_id)
        if not game:
            raise NotFound('game not found')
        if action == 'roll-dice':
            randoms = []
            change_turn = False
            for i in range(game.dice_count):
                rand = random.randrange(1, 7)
                change_turn = change_turn or (rand in game.hold)
                randoms.append(rand)
            if change_turn:
                game.turn = not game.turn
                game.player1_current = 0
                game.player2_current = 0
            game.dices = randoms
            if game.turn:
                game.player1_current += sum(randoms)
            else:
                game.player2_current += sum(randoms)
        elif action == 'hold':
            game.player1_total += game.player1_current
            game.player1_current = 0
            game.player2_total += game.player2_current
            game.player2_current = 0
            game.turn = not game.turn
            if game.player1_total >= game.max_score:
                game.winner = True
            if game.player2_total >= game.max_score:
                game.winner = False
        return Response(json.dumps(game.__dict__))
