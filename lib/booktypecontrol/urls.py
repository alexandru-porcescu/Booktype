# This file is part of Booktype.
# Copyright (c) 2012 Aleksandar Erkalovic <aleksandar.erkalovic@sourcefabric.org>
#
# Booktype is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Booktype is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Booktype.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, url

from .views import ControlCenterView, ControlCenterSettings, PersonInfoView
from .views import EditPersonInfo, PasswordChangeView, BookRenameView, DeleteGroupView

urlpatterns = patterns('',
    url(r'^$', ControlCenterView.as_view(), name='frontpage'),
    url(r'^settings/$', ControlCenterSettings.as_view(), name='settings'),

    url(r'^people/(?P<username>[\w\d\@\.\+\-\_\s]+)/info/$', PersonInfoView.as_view(), name='person_info'),
    url(r'^people/(?P<username>[\w\d\@\.\+\-\_\s]+)/edit/$', EditPersonInfo.as_view(), name='person_edit'),
    url(r'^people/(?P<username>[\w\d\@\.\+\-\_\s]+)/password/$', PasswordChangeView.as_view(), name='password_change'),

    url(r'^books/(?P<bookid>[\w\s\_\.\-\d]+)/rename/$', BookRenameView.as_view(), name='rename_book'),
    url(r'^groups/(?P<groupid>[\w\s\_\.\-\d]+)/delete/$', DeleteGroupView.as_view(), name='delete_group'),
)
