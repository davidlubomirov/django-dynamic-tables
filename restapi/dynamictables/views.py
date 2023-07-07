from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action


class DynamicTablesViewSet(GenericViewSet):
    def create(self, request):
        """create new dynamic table"""
        return Response(
            status=HTTPStatus.NOT_IMPLEMENTED,
            data={
                "message": "not implemented"
            }
        )

    def list(self, request):
        """list of tables"""
        return Response(
            status=HTTPStatus.NOT_IMPLEMENTED,
            data={
                "message": "not implemented"
            }
        )

    def update(self, request, pk: int = None):
        """update table using the index of the table"""
        return Response(
            status=HTTPStatus.NOT_IMPLEMENTED,
            data={
                "message": "not implemented"
            }
        )

    @action(methods=["post"], detail=True)
    def row(self, request, pk: int = None):
        """add new row of data to specific table using index of the selected table"""
        return Response(
            status=HTTPStatus.NOT_IMPLEMENTED,
            data={
                "message": "not implemented"
            }
        )

    @action(methods=["get"], detail=True)
    def rows(self, request, pk: int = None):
        """get all rows for specific table using index of the selected table"""
        return Response(
            status=HTTPStatus.NOT_IMPLEMENTED,
            data={
                "message": "not implemented"
            }
        )
