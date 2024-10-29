import json
from django.core.management.base import BaseCommand
from quiz.models import Question, Answer

class Command(BaseCommand):
    help = 'Import quiz data from a JSON file'

    def handle(self, *args, **kwargs):
        # Load the JSON data with the correct encoding
        with open('quiz/quiz_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Iterate through the quiz results and save to the database
        for item in data['quiz_results']:
            question_text = item['question']
            explanation = item['explanation']
            
            # Create and save the question
            question = Question.objects.create(question_text=question_text, explanation=explanation)

            # Create and save the answers
            for option in item['options']:
                answer_text = option['text']
                is_correct = option['is_correct']
                Answer.objects.create(question=question, answer_text=answer_text, is_correct=is_correct)

        self.stdout.write(self.style.SUCCESS('Successfully imported quiz data'))
