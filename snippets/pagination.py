from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'pagination': {
                'links': {
                    'first': "",
                    'last': "",
                    'previous': self.get_previous_link(),
                    'next': self.get_next_link()
                },
                'total': "",
                'page_size': "",
                'page': ""
            }
        })
