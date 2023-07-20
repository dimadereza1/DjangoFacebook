# from django.test import TestCase
# from facebook_app.models import Author

# class ModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         Author.objects.create(first_name='Bob', last_name='Smith')
    
#     def test_first_name_label(self):
#         author = Author.objects.get(id=1)

#         label = author._meta.get_field('first_name').verbose_name
#         self.assertEqual(label, 'first name')

#     def test_date_death_label(self):
#         author = Author.objects.get(id=1)

#         label = author._meta.get_field('data_of_death').verbose_name
#         self.assertEqual('data of death', label)

#     def test_str(self):
#         author = Author.objects.get(id=1)
#         expected = f'{author.first_name}, {author.last_name}'
#         self.assertEqual(str(author), expected)
