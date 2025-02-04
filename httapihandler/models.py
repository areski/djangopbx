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

from django.db import models
from django.utils.translation import gettext_lazy as _


class HttApiSession(models.Model):
    id      = models.UUIDField(primary_key=True, verbose_name=_('Session_ID'))                           # noqa: E501, E221
    name    = models.CharField(max_length=32, verbose_name=_('Name'))                                    # noqa: E501, E221
    xml     = models.TextField(blank=True, null=True, verbose_name=_('XML'))                             # noqa: E501, E221
    json    = models.JSONField(blank=True, null=True, verbose_name=_('json'))                            # noqa: E501, E221
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=_('Created'))  # noqa: E501, E221

    class Meta:
        db_table = 'pbx_httapi_session'

    def __str__(self):
        return self.id
