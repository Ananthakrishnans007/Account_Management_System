
from ast import Assign
from asyncio import tasks
from multiprocessing import context
import os
from re import L
from django.shortcuts import render,redirect
from . models import *
from . models import*
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request,'index.html')





def signup(request):  
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        if password==c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!!!!!!')
                return redirect('signup') 

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!!!!!!')
                return redirect('signup') 

            else:
                user=User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password']) 
                user.save() 
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            return redirect('signup') 
    else:
        return render(request,'index.html')
        
        
    return redirect('signin')    



def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        
        request.session["uid"]=user.id
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin_home')
            else:
                login(request,user)
                auth.login(request,user)
                # Name=user.first_name +" "+ user.last_name
                # messages.info(request, f'Welcome {Name}')
                return redirect('user_home')

        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('index')
    else:
        return redirect('index')


      





@login_required(login_url='index')
def admin_home(request):
    if not request.user.is_staff:
        return redirect('signin')

    department = Department.objects.all()
    dep_count = department.count()
    task = Task.objects.all()
    task_count = task.count()
    topic =Topic .objects.all()
    topic_count = topic.count()
    report = Report.objects.all()
    report_count = report.count()
    emp = Employee.objects.all()
    emp_count = emp.count()

    payment = Payment.objects.all()
    payment_count = payment.count()

    leave = Leave.objects.all()
    leave_count = leave.count()


    context = {
        'dep_count' :dep_count,
        'task_count' :task_count,
        'topic_count' :topic_count,
        'report_count' :report_count,
        'emp_count' :emp_count,
        'payment_count' :payment_count,
        'leave_count'  : leave_count,
    }


    
    return render(request,'administrator/home.html',context)


@login_required(login_url='index')
def department(request):

    department=Department.objects.all
    context = {
        'department' :department,
    }
    return render(request,'administrator/departments.html',context)

@login_required(login_url='index')
def add_departments(request):
    if request.method=='POST':
        dep = Department()
        dep.Department_Name=request.POST['department']
        dep.save()
        return redirect('department')
    return redirect('department')    
    
        

@login_required(login_url='index')
def edit_department(request,id):
    if request.method=='POST':
        dep = Department.objects.get(id=id)
        dep.Department_Name=request.POST['department']
        dep.save()
        return redirect('department')
    return redirect('department')    
    
        
  

@login_required(login_url='index')
def delete_department(request,id):
    dep = Department.objects.get(id=id)
    dep.delete()
    return redirect('department')


@login_required(login_url='index')
def manage_task(request):

    department = Department.objects.all()

    context = {
        'department' : department,

    }



    return render(request,'administrator/manage_task.html',context)


@login_required(login_url='index')
def admin_task(request):
    department = Department.objects.all()
    tasks = Task.objects.all()
    context={
        'department':department,
        'tasks' :tasks,

    }
    return render(request,'administrator/task.html',context)

@login_required(login_url='index')
def add_task(request):
    if request.method=='POST':
        tasks=Task()
        dep = Department.objects.get(id=request.POST['depart'])
        tasks.Department=dep
        tasks.Task_name = request.POST['t_name']
        tasks.Start_date = request.POST['s_date']
        tasks.End_date = request.POST['e_date']
        tasks.save()
        return redirect('admin_task')
    else:
        return redirect('admin_task')


@login_required(login_url='index')
def edit_task(request,id):
    if request.method=='POST':
        tasks=Task.objects.get(id=id)
        dep = Department.objects.get(id=request.POST['depart'])
        tasks.Department=dep
        tasks.Task_name = request.POST['t_name']
        temp1=request.POST['s_date']
        if temp1=='':
            tasks.Start_date = tasks.Start_date

        else:
            tasks.Start_date = temp1 

        temp2=request.POST['e_date']
        if temp1=='':
            tasks.End_date = tasks.End_date

        else:
            tasks.End_date = temp2
            
        tasks.save()
        return redirect('admin_task')
    else:
        return redirect('admin_task')

@login_required(login_url='index')
def delete_task(request,id):
     tasks=Task.objects.get(id=id)
     tasks.delete()
     return redirect('admin_task')


@login_required(login_url='index')
def admin_completed_task(request,id):

    department = Department.objects.all()

    dep_task = Department.objects.get(id=id)

    assigned_task = Assigned_Task.objects.filter(Task=dep_task.id)



    context = {
        'department' :department,
        'assigned_task':assigned_task,
        
    }

    return render(request,'administrator/completed_task.html',context)


@login_required(login_url='index')
def status(request,id):
    if request.method=='POST':
        assigned_task = Assigned_Task.objects.get(id=id)
        assigned_task.Progress = request.POST['st']
        assigned_task.save()

        return redirect('manage_task')
    return redirect('manage_task')    

@login_required(login_url='index')
def manage_topic(request):

    return render(request,'administrator/manage_topic.html')


@login_required(login_url='index')
def admin_topic(request):

    department=Department.objects.all()
    topic=Topic.objects.all()

    context = {
        'department' :department,
        'topic':topic,
    }


    return render(request,'administrator/admin_topic.html',context)

@login_required(login_url='index')
def add_topic(request):
    if request.method=='POST':
        department= Department.objects.get(id=request.POST['depart'])
        if Topic.objects.filter(Department=department.id).exists():
            t1=Topic.objects.get(Department=department)

            pre  = Previous_Topic()
            pre.Department = department
            pre.Topic_name = t1.Topic_name
            pre.Start_date = t1.Start_date
            pre.save()
            t1.delete()


            topic = Topic()
            topic.Department = department
            topic.Topic_name = request.POST['topic']
            topic.Start_date = request.POST['s_date']
            topic.End_date = request.POST['e_date']
            topic.save()
            return redirect('admin_topic')
        else:
            topic = Topic()
            topic.Department = department
            topic.Topic_name = request.POST['topic']
            topic.Start_date = request.POST['s_date']
            topic.End_date = request.POST['e_date']
            topic.save()
            return redirect('admin_topic')




    return redirect('admin_topic')


@login_required(login_url='index')
def previous_topic(request):

    department=Department.objects.all()
    pretopic=Previous_Topic.objects.all()

    context = {
        'department' :department,
        'pretopic':pretopic,
    }


    return render(request,'administrator/previous_topic.html',context)

@login_required(login_url='index')
def admin_attendance(request):

    department=Department.objects.all()
    

    context = {
        'department' :department,
        
    }

    return render(request,'administrator/attendance.html',context)


@login_required(login_url='index')
def attendance_user(request,id):

    department=Department.objects.get(id=id)

    employee = Employee.objects.filter(Department=department)
    dep = department.Department_Name

    context = {
        'department' :department,
        'employee' : employee,
        'dep' : dep,
        
    }

    return render(request,'administrator/attendance_user.html',context)

@login_required(login_url='index')
def add_attendance(request):
    if request.method=='POST':
        user = request.POST['emp']
        pk = Employee.objects.get(user=user)
        att=Attendance()
        att.user = pk.user
        att.Date = request.POST['date']
        att.status = request.POST['attendance']
        att.save()
        
        dp = pk.Department
        department=Department.objects.get(id=dp.id )


        return redirect ('attendance_user',department.id)


@login_required(login_url='index')
def view_report(request):

    report=Report.objects.all()
    
    context = {
        'report' :report,  
    }

    return render(request,'administrator/view_report.html',context)


@login_required(login_url='index')
def report_status(request,id):
    if request.method=='POST':
        report=Report.objects.get(id=id)
        report.status= request.POST['status']
        report.save()
        return redirect('view_report')   

    return redirect('view_report')    


@login_required(login_url='index')
def admin_payment(request):

    payment = Payment.objects.all()

    context = {
        'payment' : payment,  
    }

    return render(request,'administrator/view_payment.html',context)
   
    

@login_required(login_url='index')
def view_leave(request):

    leave = Leave.objects.all()


    context = {
        'leave' : leave,  
    }

    return render(request,'administrator/view_leave.html',context)
   

@login_required(login_url='index') 
def leave_status(request,id):
    if request.method=='POST':
        leave=Leave.objects.get(id=id)
        leave.status= request.POST['status']
        leave.save()
        return redirect('view_leave')   

    return redirect('view_leave') 




@login_required(login_url='index')
def employee(request):

    department=Department.objects.all()
    

    context = {
        'department' :department,
        
    }

    return render(request,'administrator/employee.html',context)
   

@login_required(login_url='index')
def show_employee(request,id):

    department=Department.objects.get(id=id)
    
    employee =Employee.objects.filter(Department=department)
    

    context = {
        'employee':employee,
        'department':department,
        
        
    }

    return render(request,'administrator/show_employee.html',context)
   

@login_required(login_url='index')
def employee_status(request,id):
    emp = Employee.objects.get(id=id)
    department = emp.Department 
    if request.method=='POST':
        

        emp.Category_Name = request.POST['status']
        emp.save()
        return redirect('show_employee',department)
    return redirect('show_employee',department)    


@login_required(login_url='index')

def employee_delete(request,id):
    emp = Employee.objects.get(id=id)
    user = emp.user.id
    department = emp.Department.id 
    os.remove(emp.Image.path)
    os.remove(emp.Plus_two.path)
    os.remove(emp.Degree.path)
    os.remove(emp.Pg.path)
    emp.delete()
    user.delete()
    
    return redirect('show_employee',department)






def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('index')   

    

#    user 

@login_required(login_url='index')
def user_home(request):
    department = Department.objects.all()

    if Employee.objects.filter(user=request.user).exists():
        emp = Employee.objects.get(user=request.user)
        context = {
        'department' :department,
        'emp':emp,
        }
        return render(request,'user/home.html',context)

    context = {
        'department' :department,
        
        }
    return render(request,'user/home.html',context)

    
    
    



@login_required(login_url='index')
def user_task(request):
    emp = Employee.objects.get(user=request.user)

    context={
        
        
        'emp' : emp,

    }

    return render(request,'user/task.html',context)

@login_required(login_url='index')
def attendance(request):
    emp = Employee.objects.get(user=request.user)

    context={
        
        
        'emp' : emp,

    }

    return render(request,'user/attendance.html',context)


@login_required(login_url='index')
def topic(request):
    emp = Employee.objects.get(user=request.user)

    context={
        
        
        'emp' : emp,

    }

    return render(request,'user/topic.html',context)


@login_required(login_url='index')
def report(request):
    emp = Employee.objects.get(user=request.user)

    context={
        
        
        'emp' : emp,

    }

    return render(request,'user/report.html',context)

@login_required(login_url='index')
def payment(request):
    emp = Employee.objects.get(user=request.user)

    context={
        
        
        'emp' : emp,

    }

    return render(request,'user/payment.html')



@login_required(login_url='index')
def apply_leave(request):
    emp = Employee.objects.get(user=request.user)

    context={
        
        
        'emp' : emp,

    }


    return render(request,'user/apply_leave.html',context)

    
@login_required(login_url='index')
def emp_detailes(request):
    if request.method=='POST':
        user=request.user
        user.first_name = request.POST['f_name']
        user.last_name = request.POST['l_name']
        emp=Employee()
        emp.user = user
        emp.DOB = request.POST['dob']
        emp.Gender = request.POST['gender']
        emp.Address = request.POST['address']
        emp.Country = request.POST['country']
        emp.City = request.POST['city']
        emp.State = request.POST['state']
        emp.Postcode = request.POST['zip']
        emp.mobile_number = request.POST['phone']
        
        dep = Department.objects.get(id=request.POST['deprt'])
        emp.Department = dep

        if len(request.FILES) != 0:
            emp.Plus_two = request.FILES['file1']
            emp.Degree= request.FILES['file2']
            emp.Pg  = request.FILES['file3']
            emp.Image = request.FILES['file4']
        user.save()
        emp.save()  
        return redirect('user_home')  
        
        
@login_required(login_url='index')        
def task_to_do(request):
    emp = Employee.objects.get(user=request.user)

    department=Department.objects.get(id=emp.Department.id)
    task = Task.objects.filter(Department=department)



    # tasks = Task.objects.filter(Department=department)
    
    # if User_task.objects.filter(user=request.user) is None:
    #     if not Assigned_Task.objects.filter(Task=tasks) is None:
    #         user_task = User_task()
    #         user_task.user = request.user
    #         user_task.Task = tasks
    #         user_task.save()
    # else:
    #     if not Assigned_Task.objects.filter(Task=tasks) is None:
    #         user_task = User_task()
    #         user_task.user = request.user
    #         user_task.Task = tasks
    #         user_task.save()


        
    
    # task = User_task.objects.filter(user=request.user)   

    context={
        
        'task' :task,
        'emp' : emp,

    }
    return render(request,'user/task_to_do.html',context)

@login_required(login_url='index')
def assigned_task(request,id):
    if request.method=='POST':
        
        task = Task.objects.get(id=id)
        assign=Assigned_Task()
        assign.user = request.user
        assign.Task = task
        
        assign.Description = request.POST['desp']
        if len(request.FILES) != 0:
            assign.File = request.FILES['file']

        assign.save()
        ts=User_task.objects.get(user=request.user)
        ts.delete()
        return redirect('user_task')     

    return redirect('user_task') 



@login_required(login_url='index')
def completed_task(request):
    emp = Employee.objects.get(user=request.user)

    task = Assigned_Task.objects.filter(user=request.user)
    context={
        'task':task,
        'emp' : emp,
    }


    return render(request,'user/completed_task.html',context)

@login_required(login_url='index')
def current_topic(request):

    emp = Employee.objects.get(user=request.user)
    department=Department.objects.get(id=emp.Department.id)


    topic = Topic.objects.filter(Department=department)
    context={
        'topic':topic,
        'emp' : emp,
    }


    return render(request,'user/current_topic.html',context)


@login_required(login_url='index')
def user_previous_topic(request):
    emp = Employee.objects.get(user=request.user)
    department=Department.objects.get(id=emp.Department.id)

    previous = Previous_Topic.objects.filter(Department=department)
    context={
        'previous':previous,
        'emp' : emp,
    }


    return render(request,'user/previous_topic.html',context)


@login_required(login_url='index')
def view_attendance(request):
    if request.method=='POST':
        start_date=request.POST['s_date']
        end_date=request.POST['e_date']
        print(start_date)
        print(end_date)

        
        attendance = Attendance.objects.filter(user=request.user.id,Date__gte=start_date,Date__lte=end_date)

        context={
        'attendance':attendance,
            }
    
        return render(request,'user/view_attendance.html',context)



@login_required(login_url='index')
def report_issue(request):
    emp = Employee.objects.get(user=request.user)
    context={
        
        'emp' : emp,
    }
    
    return render(request,'user/report_issue.html',context)



@login_required(login_url='index')
def issue(request):
    if request.method=='POST':
        report = Report()
        user = User.objects.get(id=request.user.id)
        emp = Employee.objects.get(user=request.user)
        department=Department.objects.get(id=emp.Department.id)

        report.user = user
        report.Department = department

        report.To = request.POST['staff']
        report.Report = request.POST['report']
        report.save()
        return redirect('report_issue')
    return redirect('report_issue')   


@login_required(login_url='index')
def reported_issue(request):
    report = Report.objects.filter(user=request.user.id)
    emp = Employee.objects.get(user=request.user)

    context={
        'report':report,
        'emp' : emp,
    }

    return render(request,'user/reported_issue.html',context)


@login_required(login_url='index')
def add_payment(request):
    user = User.objects.get(id=request.user.id)
    emp = Employee.objects.get(user=user)
    
    context={
        'report':report,
        'emp' : emp,
    }

    return render(request,'user/add_payment.html',context)


@login_required(login_url='index')
def user_payment(request):
    if request.method=='POST':
        user = User.objects.get(id=request.user.id)
        emp = Employee.objects.get(user=request.user)
        department=Department.objects.get(id=emp.Department.id)

        payment = Payment()

        payment.user = user 
        payment.Department = department
        payment.Amount = request.POST['amount']
        payment.Payment_Date = request.POST['date']
        if len(request.FILES) != 0:
            payment.File = request.FILES['file']

        payment.save()  
        return redirect('add_payment')  
    return redirect('add_payment')      


@login_required(login_url='index')
def view_payment(request):
    user = User.objects.get(id=request.user.id)

    emp = Employee.objects.get(user=request.user)

    payment = Payment.objects.filter(user=user)
    
    context={
        'payment':payment,
        'emp' : emp,
    }

    return render(request,'user/view_payment.html',context)

        
@login_required(login_url='index')
def leave_apply(request):
    
    emp = Employee.objects.get(user=request.user)
    context ={
        'emp' : emp,

    }



    return render(request,'user/leave_apply.html',context)

        
@login_required(login_url='index')
def leave(request):
    if request.method=='POST':
        user = User.objects.get(id=request.user.id)
        emp = Employee.objects.get(user=request.user)
        department=Department.objects.get(id=emp.Department.id)

        leave = Leave()

        leave.user = user
        leave.Department = department
        leave.From = request.POST['s_date']
        leave.To = request.POST['e_date']
        leave.Leave  = request.POST['leave']
        leave.Reason = request.POST['reason']
        leave.save()
        
        return redirect('leave_apply')
    return redirect('leave_apply')
    


@login_required(login_url='index')
def applied_leave(request):

    emp = Employee.objects.get(user=request.user)
    leave = Leave.objects.filter(user=request.user)
    context ={
        'leave' : leave,
        'emp' : emp,

    }


    return render(request,'user/applied_leave.html',context)


@login_required(login_url='index')
def profile(request):
   
    emp = Employee.objects.get(user=request.user)

    context ={
        'emp' : emp,

    }

    return render(request,'user/profile.html',context)











