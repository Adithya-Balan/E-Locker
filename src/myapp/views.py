from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import userinfo, file_upload
from .forms import file_uploadForm


# Create your views here.
def sign_up(request):
    context = {}
    return render(request, 'registration/sign-up.html', context)

@login_required
def home(request):
    form = file_uploadForm()
    aadhaar = file_upload.objects.filter(user=request.user, type = 'aadhaar').first()
    vaccine = file_upload.objects.filter(user=request.user, type = 'VACER').first()
    Income_Certificate = file_upload.objects.filter(user=request.user, type='INCER').first()
    marksheet = file_upload.objects.filter(user=request.user, type='HSCER').first()
    ration_card = file_upload.objects.filter(user=request.user, type='RATCR').first()
    vechile_card = file_upload.objects.filter(user=request.user, type='RVCER').first()
    driving_lis = file_upload.objects.filter(user=request.user, type='DRVLC').first()
    
    context = {
        'form': form,
        'aadhaar': aadhaar,
        'vaccine': vaccine,
        'Income_Certificate': Income_Certificate,
        'marksheet': marksheet,
        'ration_card': ration_card,
        'vechile_card': vechile_card,
        'driving_lis': driving_lis,
    }
    return render(request, 'myapp/home1.html', context)

@login_required
def profile(request):
    files = file_upload.objects.filter(user=request.user).order_by('-id').first()
    total_files = file_upload.objects.filter(user=request.user).count()
    recent_file_name =  files.file_name
    user_obj = userinfo.objects.get(user= request.user)
    print(user_obj)
    context = {
        'user_obj': user_obj,
        'recent_file_name' : recent_file_name,
        'no_of_files': total_files
    }
    return render(request, 'myapp/profile.html', context)

@login_required
def recent(request):
    files = file_upload.objects.filter(user=request.user).order_by('-id')
    context = {
        'recent_files': files
    }
    return render(request, 'myapp/recent.html', context)

@login_required
def imp_documents(request):
    files = file_upload.objects.filter(user=request.user).exclude(type='custom').order_by('-id')
    custom_doc = file_upload.objects.filter(user = request.user, type = 'custom').order_by('-id')
    context = {
        'files': files ,
        'custom': custom_doc
    }
    return render(request, 'myapp/imp_documents.html', context)

@login_required
def upload_view(request, category):
    category_list = {'aadhaar': 'aadhaar', 
                    'VACER': 'Covid Vaccine Certificate',
                    'INCER': 'Income Certificate', 
                    'HSCER': 'Higher Secondary certficate', 
                    'RATCR': 'Ration Card',
                    'RVCER': 'Registration of vechicles Card',
                    'DRVLC': 'Driving Licesence',
                    'CUSTOM': 'custom',
                    }    
    txt = category
    category_name = category_list.get(txt)
    form = file_uploadForm()
    
    if request.method == "POST":
        form = file_uploadForm(request.POST, request.FILES)
        if form.is_valid():
            form_obj = form.save(commit = False)
            form_obj.type = txt
            form_obj.user = request.user
            form_obj.save()
            return redirect('/document-imp')
            
    context={
        'category_name': category_name,
        'category': category,
        'form': form
    }
    
    return render(request, 'myapp/upload.html', context)

    