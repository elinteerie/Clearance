from rest_framework import permissions

class IsAuthenticatedScreenUserInFaculty(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Check if the user is a ScreenUser
        if request.user.user_type != 'SCREEN':
            return False

        # Get the faculty associated with the user
        faculty = request.user.screenuser.faculty

        # Check if the user's faculty matches the requested faculty
        faculty_pk = view.kwargs.get('pk')
        return faculty.pk == faculty_pk