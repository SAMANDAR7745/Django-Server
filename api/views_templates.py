from django.shortcuts import render
from main.serializers import *
from main.models import *
from rest_framework.request import Request
from rest_framework.views import APIView
import django_filters
from django.http.request import HttpRequest


# < ------ HOME LIST ----- >
class HomeCreateListView(APIView):
    def get(self, request: Request):
        # ---------------- > Food < --------------------------------
        food = Food.objects.all().order_by('-id')
        serializer_food = FoodSerializer(food, many=True)
        # ----------------- > Category < ---------------------------
        category = Category.objects.all().order_by('-id')
        serializer = CategorySerializer(category, many=True)
        # ------------------- > CLIENT < ---------------------------
        client = Client.objects.all()
        serializer_client = ClientSerializer(client, many=True)
        # ------------------- > Members < --------------------------
        members = Members.objects.all().order_by('-id')
        serializer_members = MembersSerializer(members, many=True)
        # ------------------- > Coment < --------------------------
        comment = Comment.objects.all().order_by('-id')
        serializer_comment = CommentSerializer(comment, many=True)
        
        # ------------------- > context < --------------------------
        return render(request, "main/index.html", context={"categorylist": serializer.data, "food": serializer_food.data, "members": serializer_members.data, "client": serializer_client.data, "comment": serializer_comment.data})


# < ------ About LIST ----- >
class AboutCreateListView(APIView):
    def get(self, request: Request):
        # ------------------- > Members < --------------------------
        members = Members.objects.all().order_by('-id')
        serializer_members = MembersSerializer(members, many=True)
        return render(request, 'main/about.html', context={"members": serializer_members.data})




def service(request: HttpRequest):
    return render(request, 'main/service.html')


# < ------ Menu LIST ----- >
class MenuCreateListView(APIView):
    def get(self, request: Request):
        # ---------------- > Food < --------------------------------
        food = Food.objects.all().order_by('-id')
        serializer_food = FoodSerializer(food, many=True)
        return render(request, 'main/menu.html', context={"food": serializer_food.data})







def booking(request: HttpRequest):
    return render(request, 'blog/booking.html')


def tur_team(request: HttpRequest):
    return render(request, 'blog/team.html')


def testimonial(request: HttpRequest):
    return render(request, 'blog/testimonial.html')


def contact(request: HttpRequest):
    return render(request, 'forms/contact.html')
