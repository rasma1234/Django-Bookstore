from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

    
        cls.book = Book.objects.create(
            title='A Good Title',
            author='An Author',
            description='A sample book description.',
            published_date=2023,  
            price=19.99,
        )

    def test_book_creation(self):
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.title, 'A Good Title')
        self.assertEqual(book.author, 'An Author')
        self.assertEqual(str(book.published_date), '2023') 
        self.assertEqual(float(book.price), 19.99)  

    def test_book_retrieval(self):
        book_from_db = Book.objects.get(id=self.book.id)
        self.assertEqual(book_from_db, self.book)

    def test_book_update(self):
        self.book.title = "An Updated Title"
        self.book.save()
        updated_book = Book.objects.get(id=self.book.id)
        self.assertEqual(updated_book.title, "An Updated Title")

    def test_book_deletion(self):
        book_id = self.book.id
        self.book.delete()
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book_id)

    def test_str_representation(self):
        self.assertEqual(str(self.book), 'A Good Title')

    def test_book_get_absolute_url(self):
        expected_url = f'/{self.book.id}/'
        actual_url = self.book.get_absolute_url()
        self.assertEqual(actual_url, expected_url)

