from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ProjectManagement.accounts.models import WorkerUser
from ProjectManagement.apis.serializers import WorkerUserSerializer, WorkerUserStatusSerializer
from ProjectManagement.apis.permissions import IsSuperuser


class ListWorkerUsersView(APIView):
    # permission_classes = [IsSuperuser]

    def get(self, request):
        workers = WorkerUser.objects.all()
        serializer = WorkerUserSerializer(workers, many=True)
        return Response({"books": serializer.data})


class UpdateWorkerUserStatus(APIView):
    # permission_classes = [IsSuperuser]

    def post(self, request, pk):
        try:
            worker = WorkerUser.objects.get(pk=pk)
        except WorkerUser.DoesNotExist:
            return Response({'error': 'Worker not found'}, status=status.HTTP_404_NOT_FOUND)

        worker.is_active = not worker.is_active
        worker.save()

        serializer = WorkerUserSerializer(worker)
        return Response(serializer.data)
