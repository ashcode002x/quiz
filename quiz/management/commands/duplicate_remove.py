from django.core.management.base import BaseCommand
from django.db import transaction
from quiz.models import Question, Answer  # Adjust the import according to your models

class Command(BaseCommand):
    help = 'Remove duplicate questions and their associated answers.'

    def handle(self, *args, **kwargs):
        self.delete_duplicate_questions()

    def delete_duplicate_questions(self):
        # Start a database transaction
        with transaction.atomic():
            # Create a dictionary to track unique questions
            unique_questions = {}
            
            # Fetch all questions
            questions = Question.objects.all()

            for question in questions:
                # If question text is already seen, mark it for deletion
                if question.question_text in unique_questions:
                    # Add the question to a list of duplicates
                    unique_questions[question.question_text].append(question)
                else:
                    # Initialize the list for the first occurrence
                    unique_questions[question.question_text] = [question]

            # Iterate through the dictionary and delete duplicates
            for duplicates in unique_questions.values():
                if len(duplicates) > 1:
                    # Keep the first occurrence, delete the rest
                    for question in duplicates[1:]:
                        # Delete associated answers first
                        Answer.objects.filter(question=question).delete()
                        # Now delete the question
                        question.delete()

            self.stdout.write(self.style.SUCCESS('Duplicate questions and their answers have been removed.'))
