
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, QuestionForm, AnswerForm
from .models import Question, Answer


def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'quora_clone/home.html', {'questions': questions})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'quora_clone/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'quora_clone/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'quora_clone/post_question.html', {'form': form})

@login_required
def answer_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
    return redirect('question_detail', pk=pk)



def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    form = AnswerForm()
    return render(request, 'quora_clone/question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required
def like_answer(request, answer_id):
    try:
        answer = get_object_or_404(Answer, id=answer_id)
        user = request.user

        if user in answer.likes.all():
            answer.likes.remove(user)
            print(f"Removed like from user: {user.username}")
        else:
            answer.likes.add(user)
            print(f"Added like from user: {user.username}")

        print(f"After like: {answer.likes.count()}")
        return redirect('question_detail', pk=answer.question.id)

    except Exception as e:
        return redirect('question_detail', pk=answer.question.id)

