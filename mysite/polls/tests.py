# Create your tests here.
import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Question

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionindexViewTests(TestCase):
    def test_no_questions(self):
        response = self.cliet.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuertsetEqual(response.context['latest_question_list'], ['<Question: Past question>'])


    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse(polls:index))
        self.assertContains(reponse, "No polls are available")
self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        create_question(question_text = "Past Question.", days=-30)
        create_question(question_text = "Future Question.", days=-30)
        respone = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(reponse.context['latest_question_list'], ['<Question: Past Question 2. >', '<Question: Past Question 1.>'])
