# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time_now = timezone.now() + datetime.timedelta(days=30)
        # print 'time_now:', time_now
        future_question = Question(pub_date=time_now)
        # print 'future_question:', future_question
        self.assertIs(future_question.was_published_recently(), False)