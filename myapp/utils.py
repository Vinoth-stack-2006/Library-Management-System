from django.contrib.auth.tokens import PasswordResetTokenGenerator

class SimpleTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        """
        Only depend on user primary key and timestamp.
        Ignore email or last_login.
        """
        return f"{user.pk}{timestamp}"

# Instantiate
student_token_generator = SimpleTokenGenerator()
