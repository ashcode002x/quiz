from django.shortcuts import render, redirect
from .models import Question
import random

def quiz_view(request):
    # Get all questions
    questions = list(Question.objects.all())
    
    # Shuffle the questions to get them in random order
    random.shuffle(questions)

    # Optionally, limit the number of questions displayed
    # For example, display only 10 random questions
    questions = questions[:20]  # Change this number as needed

    return render(request, 'quiz/quiz.html', {'questions': questions})
def submit_quiz(request):
    score = 0
    total_questions = 0
    explanations = {}

    for question in Question.objects.all():
        total_questions += 1
        selected_answer = request.POST.get(str(question.id))
        if selected_answer:
            answer = question.answer_set.get(id=selected_answer)
            if answer.is_correct:
                score += 1
            explanations[question.id] = (answer.is_correct, question.explanation)

    return render(request, 'quiz/result.html', {'score': score, 'total_questions': total_questions, 'explanations': explanations})

from django.http import JsonResponse

def check_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_answer_id = request.POST.get('selected_answer_id')

        question = Question.objects.get(id=question_id)
        selected_answer = question.answer_set.get(id=selected_answer_id)
        correct_answer = question.answer_set.filter(is_correct=True).first()

        is_correct = selected_answer.is_correct
        explanation = question.explanation
        correct_answer_text = correct_answer.answer_text

        return JsonResponse({
            'is_correct': is_correct,
            'explanation': explanation,
            'correct_answer': correct_answer_text,
        })
