from random import random

from django.shortcuts import render

# Create your views here.
QUESTIONS = [
    {
        "title": f"Question {i}",
        "text": f"This is text for question {i}",
        "tag1": f"tag {i + 1}",
        "tag2": f"tag {i - 1}",
        "tag3": f"tag {i * i}"
    } for i in range(5, 10)
]

ANSWERS = [
    {
        "title": f"Answer {i}"
    } for i in range(1, 3)
]

LOOK_QUESTIONS = [
    {
        "title": f"Question A{i}",
        "text": f"Text for question with number {i}",
        "tag1": f"tag {i + 1}",
        "tag2": f"tag {i - 1}",
        "tag3": f"tag {i * i}"
    } for i in range(1, 2)
]


def index(request):
    return render(request, "index.html", {"questions": QUESTIONS})


def ask(request):
    return render(request, "ask.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def question(request):
    return render(request, "question.html", {"answers": ANSWERS, "look_questions": LOOK_QUESTIONS})
