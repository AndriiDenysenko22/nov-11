import random
import factory
from unittest.mock import Mock, patch
from django.test import TestCase
from django.urls import reverse_lazy

from apps.authentication.models import User
from apps.lms.models import Student


def a_plus_b(a=3, b=6):
    return a + b


def a_plus_random(a):
    return a + random.randint(0, 1)


class APlusBTestCase(TestCase):
    def test_a_plus_b__when_a_4_and_b_5_should_return_9(self):
        self.assertEqual(a_plus_b(4, 5), 9)

    def test_a_plus_b__when_not_passed_args__should_return_9(self):
        self.assertEqual(a_plus_b(), 9)


class APlusRandomTestCase(TestCase):
    def setUp(self):
        self.a = 3
        self.random_mock = Mock()
        self.random_mock.return_value = 3

    def test_a_plus_random__should_return(self):
        with patch('random.randint', self.random_mock):
            self.assertEqual(self.a+3, a_plus_random(self.a))


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'lms.Student'

    name = factory.Faker('name')
    birth_date = factory.Faker('date')


class LMSTestCase(TestCase):

    def setUp(self):
        self.s1 = StudentFactory()
        self.s2 = StudentFactory()

    def test_student_list_when_user_is_not_authorized_should_return_302(self):
        response = self.client.get(reverse_lazy('lms:student-list'))
        self.assertEqual(response.status_code, 302)

    def test_students_list__when_user_authorized__should_return_students(self):
        user = User.objects.create_user('test@test.com')
        self.client.force_login(user)
        response = self.client.get(reverse_lazy('lms:student-list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.s1, response.context['object_list'])
        self.assertIn(self.s2, response.context['object_list'])
