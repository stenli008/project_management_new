from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ProjectManagement.accounts.models import WorkerUser
from ProjectManagement.apis.models import WorkerUserSerializer
from ProjectManagement.apis.permissions import IsSuperuser


class ListWorkerUsersView(APIView):
    def get(self, request):
        workers = WorkerUser.objects.all()
        serializer = WorkerUserSerializer(workers, many=True)
        return Response({"books": serializer.data})
    permission_classes = [IsSuperuser]

