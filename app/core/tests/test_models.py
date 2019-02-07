from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest (TestCase):

    def test_create_user_with_email_suscesfull(self):
        """Test ok de creacion de un usuario con email"""
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalizer(self):
        """Testea si el email esta normalizado"""
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(email, 'Testpass123')

        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Testea la creación del usuario sin un email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Testpass123')

    def test_create_new_superuser(self):
        """ Test creando un nuevo super usuario """
# La función create_superuser es parte del PermissionsMixin 2
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'Testpass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
