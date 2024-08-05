from django.core.exceptions import PermissionDenied


def admin_only(function):
    """Limit view to superusers only."""

    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            if hasattr(request.user, "profile"):
                if request.user.profile.role not in ["admin", "vip"]:
                    raise PermissionDenied
            else:
                raise PermissionDenied
        return function(request, *args, **kwargs)

    return _inner
