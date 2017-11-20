from django.test import TestCase
import pytest

# Create your tests here.
@pytest.mark.django_db
class TestUsers:
    def test_home(self, client):
            response = client.get('/')
            assert response.status_code == 200
