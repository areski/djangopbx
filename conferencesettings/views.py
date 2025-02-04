#
#    DjangoPBX
#
#    MIT License
#
#    Copyright (c) 2016 - 2022 Adrian Fretwell <adrian@djangopbx.com>
#
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.
#
#    Contributor(s):
#    Adrian Fretwell <adrian@djangopbx.com>
#

from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from pbx.restpermissions import (
    AdminApiAccessPermission
)
from .models import (
    ConferenceControls, ConferenceControlDetails, ConferenceProfiles, ConferenceProfileParams,
)
from .serializers import (
    ConferenceControlsSerializer, ConferenceControlDetailsSerializer, ConferenceProfilesSerializer,
    ConferenceProfileParamsSerializer,
)


class ConferenceControlsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ConferenceControls to be viewed or edited.
    """
    queryset = ConferenceControls.objects.all().order_by('name')
    serializer_class = ConferenceControlsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'enabled']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class ConferenceControlDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ConferenceControlDetails to be viewed or edited.
    """
    queryset = ConferenceControlDetails.objects.all().order_by('conf_ctrl_id', 'id')
    serializer_class = ConferenceControlDetailsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['digits', 'action', 'enabled']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class ConferenceProfilesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ConferenceProfiles to be viewed or edited.
    """
    queryset = ConferenceProfiles.objects.all().order_by('name')
    serializer_class = ConferenceProfilesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'enabled']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class ConferenceProfileParamsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ConferenceProfileParams to be viewed or edited.
    """
    queryset = ConferenceProfileParams.objects.all().order_by('conf_profile_id', 'id')
    serializer_class = ConferenceProfileParamsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'value', 'enabled']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]
