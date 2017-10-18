from unittest.mock import MagicMock

from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from app_author.models import validate_image


class AuthorModelTestCase(SimpleTestCase):

    def test_validate_image_author(self):
        obj = MagicMock()
        obj.file.size = 900000
        with self.assertRaisesMessage(ValidationError, 'Max file size is 0.5MB'):
            validate_image(obj)