from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm

# 创建医生
def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list.html')  # 跳转到医生列表页面
    else:
        form = DoctorForm()

    context = {'form': form}
    return render(request, 'doctors/create_doctor.html', context)

# 更新医生信息
def update_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_detail', pk=doctor.pk)  # 跳转到医生详情页面
    else:
        form = DoctorForm(instance=doctor)

    context = {'form': form, 'doctor': doctor}
    return render(request, 'doctors/update_doctor.html', context)

# 删除医生
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')  # 跳转到医生列表页面

    context = {'doctor': doctor}
    return render(request, 'doctors/delete_doctor.html', context)

# 查看医生详情
def view_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    context = {'doctor': doctor}
    return render(request, 'doctors/view_doctor.html', context)

# 医生列表
def list_doctors(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctors/doctor_list.html', context)