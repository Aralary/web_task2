from django.shortcuts import render

# Create your views here.
QUESTIONS = [
    {
        "title": f"Question {i}",
        "text": f"This is text for question {i}"
    } for i in range(5, 10)
]


def index(request):
    return render(request, "index.html", {"questions": QUESTIONS})


def ask(request):
    return render(request, "ask.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")
