from django.test import TestCase
from facebook_app.forms import DateForm
from django.utils import timezone
import datetime

class Test(TestCase):
    def test_validation(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = DateForm(data={'data': date})
        self.assertTrue(form.is_valid())