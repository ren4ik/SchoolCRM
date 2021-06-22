from django.urls import path, include
from handbook.views import *

branch_url = [
    path('<slug:slug>/', BranchDetail.as_view(), name="branch-detail"),
    path('list/', BranchList.as_view(), name="branch-list"),
    path('update/<slug:slug>/', BranchUpdate.as_view(), name="branch-update"),
    path('delete/<slug:slug>/', BranchDelete.as_view(), name="branch-delete"),
    path('create/', BranchCreate.as_view(), name="branch-create"),
]

direction_url = [
    path('<slug:slug>/', DirectionDetail.as_view(), name="direction-detail"),
    path('list/', DirectionList.as_view(), name="direction-list"),
    path('update/<slug:slug>/', DirectionUpdate.as_view(), name="direction-update"),
    path('delete/<slug:slug>/', DirectionDelete.as_view(), name="direction-delete"),
    path('create/', DirectionCreate.as_view(), name="direction-create"),
]

group_info_url = [
    path('<slug:slug>/', GroupInfoDetail.as_view(), name="group-info-detail"),
    path('list/', GroupInfoList.as_view(), name="group-info-list"),
    path('update/<slug:slug>/', GroupInfoUpdate.as_view(), name="group-info-update"),
    path('delete/<slug:slug>/', GroupInfoDelete.as_view(), name="group-info-delete"),
    path('create/', GroupInfoCreate.as_view(), name="group-info-create"),
]

group_url = [
    path('<slug:slug>/', GroupDetail.as_view(), name="group-detail"),
    path('list/', GroupList.as_view(), name="group-list"),
    path('update/<slug:slug>/', GroupUpdate.as_view(), name="group-update"),
    path('delete/<slug:slug>/', GroupDelete.as_view(), name="group-delete"),
    path('create/', GroupCreate.as_view(), name="group-create"),
]

urlpatterns = [
    path('branch/', include(branch_url)),
    path('direction/', include(direction_url)),
    path('group-info/', include(group_info_url)),
    path('group/', include(group_url)),
]
