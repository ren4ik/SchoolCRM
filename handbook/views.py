from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from handbook.models import Branch, Direction


class BranchDetail(DetailView):
    model = Branch
    template_name = 'handbook/detail.html'


class BranchList(ListView):
    model = Branch
    template_name = 'handbook/list.html'


class BranchUpdate(UpdateView):
    model = Branch
    template_name = 'handbook/update.html'


class BranchDelete(DeleteView):
    model = Branch
    template_name = 'handbook/delete.html'


class BranchCreate(CreateView):
    model = Branch
    template_name = 'handbook/create.html'


class DirectionDetail(DetailView):
    model = Direction
    template_name = 'handbook/detail.html'


class DirectionList(ListView):
    model = Direction
    template_name = 'handbook/list.html'


class DirectionUpdate(UpdateView):
    model = Direction
    template_name = 'handbook/update.html'


class DirectionDelete(DeleteView):
    model = Direction
    template_name = 'handbook/delete.html'


class DirectionCreate(CreateView):
    model = Direction
    template_name = 'handbook/create.html'


class GroupInfoDetail(DetailView):
    pass


class GroupInfoList(ListView):
    pass


class GroupInfoUpdate(UpdateView):
    pass


class GroupInfoDelete(DeleteView):
    pass


class GroupInfoCreate(CreateView):
    pass


class GroupDetail(DetailView):
    pass


class GroupList(ListView):
    pass


class GroupUpdate(UpdateView):
    pass


class GroupDelete(DeleteView):
    pass


class GroupCreate(CreateView):
    pass
