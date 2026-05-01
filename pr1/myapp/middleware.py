from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):  # ✅ double underscores
        self.get_response = get_response

    def __call__(self, request):  # ✅ double underscores
        # Allow public URLs to be accessed without login
        public_paths = [reverse('login'), reverse('admin_login'), '/public-url/']

        if not request.session.get('role') and request.path not in public_paths:
            return redirect('login')

        response = self.get_response(request)
        return response
