from django.shortcuts import render
from .forms import FormStepOne, FormStepTwo, SolicitudesStep1_Form, SolicitudesStep1b_Form
from formtools.wizard.views import SessionWizardView
# Create your views here.
class FormWizardView(SessionWizardView):
    template_name = "solicitudes.html"
    form_list = [SolicitudesStep1_Form, SolicitudesStep1b_Form]

    def done(self, form_list, **kwargs):
        return render(self.request, 'solicitud_ok.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })