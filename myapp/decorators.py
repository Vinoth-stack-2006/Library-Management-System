from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def login_required_custom(view_func):
    """
    Decorator to check if user is logged in based on session 'role'.
    Redirects to 'login' page if not authenticated.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'role' not in request.session:
            messages.error(request, "⚠ Please log in first!")
            return redirect('login')  # Replace 'login' with your login URL name if different
        return view_func(request, *args, **kwargs)
    return wrapper

def role_required(allowed_roles):
    """
    Decorator to restrict view access to users with roles in allowed_roles.
    If role not permitted or missing, redirects to login page.
    Usage: @role_required(['admin', 'staff'])
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user_role = request.session.get('role')
            if not user_role or user_role not in allowed_roles:
                messages.error(request, "⚠ Access denied. Please log in with appropriate credentials.")
                return redirect('login')  # Replace 'login' with your login URL name if different
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator