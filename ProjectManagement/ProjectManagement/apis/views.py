from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from ProjectManagement.accounts.models import WorkerUser
from ProjectManagement.apis.serializers import WorkerUserSerializer, WorkerUserStatusSerializer, TaskSerializer, \
    UpdateWorkDoneSerializer
from ProjectManagement.apis.permissions import IsSuperuser
from ProjectManagement.projects.models import Task


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


class DeleteTaskView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({'tasks': serializer.data})

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateWorkDoneView(APIView):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, many=False)
        return Response({'task': serializer.data})

    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateWorkDoneSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            new_work_done = serializer.validated_data['work_done']
            task.work_done = new_work_done

            if new_work_done >= task.requirement:
                task.complete = True

            task.save()

            updated_task_serializer = TaskSerializer(task)
            return Response(updated_task_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
