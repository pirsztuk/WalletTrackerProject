from rest_framework.response import Response
from rest_framework import status

class ResponseShortcutsMixin:
    def ok(self, data=None):
        return Response(data, status=status.HTTP_200_OK)
    def created(self, data=None):
        return Response(data, status=status.HTTP_201_CREATED)
    def no_content(self):
        return Response(status=status.HTTP_204_NO_CONTENT)
    def bad_request(self, errors=None):
        return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
    def no_content(self, errors=None):
        return Response({"errors": errors}, status=status.HTTP_204_NO_CONTENT)