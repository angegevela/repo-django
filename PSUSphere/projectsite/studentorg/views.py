from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program, Boat
from studentorg.forms import OrganizationForm,OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy

from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.utils.dateparse import parse_date


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import render, redirect

@method_decorator(login_required, name='dispatch')

# Create your views here.
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'


class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your organization was created successfully!")
        return response


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

    def form_valid(self, form):
        messages.success(self.request, 'Organization details successfully updated.')
        return super().form_valid(form)

# Delete view for Organization
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')
    def get_success_url(self):
        messages.success(self.request, 'Organization details successfully deleted.')
        return reverse_lazy('organization-list')



# Organization Members Views
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'org_members'
    template_name = 'orgmember_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")

        if query:
            # Try to parse the query as a date (supports 'YYYY-MM-DD' or 'MM/DD/YYYY')
            parsed_date = parse_date(query)

            if parsed_date:
                qs = qs.filter(
                    Q(student__lastname__icontains=query) |
                    Q(organization__name__icontains=query) |
                    Q(date_joined=parsed_date)  
                )
            else:
                qs = qs.filter(
                    Q(student__lastname__icontains=query) |
                    Q(organization__name__icontains=query) |
                    Q(date_joined__icontains=query)  
                )
        
        return qs
class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('orgmember-list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your Organization Member Details was created successfully!")
        return response


class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_edit.html'
    success_url = reverse_lazy('orgmember-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Organization Member Details successfully updated.')
        return super().form_valid(form)


class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')
    
    def get_success_url(self):
        messages.success(self.request, 'Organization Member Details successfully deleted.')
        return reverse_lazy('orgmember-list')


# Student Views
class StudentList(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student_list.html'
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(
                Q(firstname__icontains=query) |
                Q(lastname__icontains=query) |
                Q(middlename__icontains=query) |
                Q(student_id__icontains=query) |
                Q(program__prog_name__icontains=query)  # Filtering by Program related field
            )
        return Student.objects.all()



class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your Student Information was created successfully!")
        return response


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        messages.success(self.request, 'Student Details Successfully Updated.')
        return super().form_valid(form)



class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')
    def get_success_url(self):
        messages.success(self.request, 'Student Information successfully deleted.')
        return reverse_lazy('orgmember-list')


# College Views
class CollegeList(ListView):
    model = College
    context_object_name = 'colleges'
    template_name = 'college_list.html'
    paginate_by = 5


class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your College information was created successfully!")
        return response



class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')
    
    def form_valid(self, form):
        college_name = form.instance.college_name
        messages.success(self.request, f'{college_name} has been successfully updated.')
        
        return super().form_valid(form)


class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')
    def get_success_url(self):
        messages.success(self.request, 'College Information successfully deleted.')
        return reverse_lazy('orgmember-list')

class ProgramList(ListView):
    model = Program
    context_object_name = 'programs'
    template_name = 'program_list.html'
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        query = self.request.GET.get('q')
        if query:
            # Filter the Program by program name (prog_name) and by the related college name
            return Program.objects.filter(
                Q(prog_name__icontains=query) |
                Q(college__college_name__icontains=query)  # Filtering on the related college_name field
            )
        return Program.objects.all()



class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your Program was created successfully!")
        return response


class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')
    def form_valid(self, form):
        messages.success(self.request, 'Program Details successfully updated.')
        return super().form_valid(form)



class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')
    
    def get_success_url(self):
        messages.success(self.request, 'Program Information successfully deleted.')
        return reverse_lazy('program-list')


class BoatCreateView(CreateView):
    model = Boat
    fields = '__all__'
    template_name = "boat_form.html"
    success_url = reverse_lazy('boat-list')

    def post(self, request, *args, **kwargs):
        self.object = None
        length = request.POST.get('length')
        width = request.POST.get('width')
        height = request.POST.get('height')

        # Validate dimensions
        errors = []
        for field_name, value in [('length', length), ('width', width), ('height', height)]:
            try:
                if float(value) <= 0:
                    errors.append(f"{field_name.capitalize()} must be greater than 0.")
            except (ValueError, TypeError):
                errors.append(f"{field_name.capitalize()} must be a valid number.")

        # If errors exist, display them and return to the form
        if errors:
            for error in errors:
                messages.error(request, error)
            return self.form_invalid(self.get_form())

        # Call the parent’s post() if validation passes
        return super().post(request, *args, **kwargs)

class BoatListView(ListView):
    model = Boat
    context_object_name = 'boats'
    template_name = 'boat_list.html'
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        query = self.request.GET.get("q")
        if query:
            return Boat.objects.filter(
                Q(name__icontains=query) |
                Q(type__icontains=query)
            )
        return Boat.objects.all()

class BoatUpdateView(UpdateView):
    model = Boat
    fields = '__all__'
    template_name = "boat_form.html"
    success_url = reverse_lazy('boat-list')

    def post(self, request, *args, **kwargs):
        length = request.POST.get('length')
        width = request.POST.get('width')
        height = request.POST.get('height')

        # Validate dimensions
        errors = []
        for field_name, value in [('length', length), ('width', width), ('height', height)]:
            try:
                if float(value) <= 0:
                    errors.append(f"{field_name.capitalize()} must be greater than 0.")
            except (ValueError, TypeError):
                errors.append(f"{field_name.capitalize()} must be a valid number.")

        # If errors exist, display them and return to the form
        if errors:
            for error in errors:
                messages.error(request, error)
            return self.form_invalid(self.get_form())

        # Call the parent’s post() if validation passes
        return super().post(request, *args, **kwargs)

class BoatDeleteView(DeleteView):
    model = Boat
    template_name = 'boat_del.html'
    success_url = reverse_lazy('boat-list')

    def get_success_url(self):
        messages.success(self.request, 'Boat entry successfully deleted.')
        return reverse_lazy('boat-list')
