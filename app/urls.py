from django.urls import path
from .import views

urlpatterns = [

    path('',views.index,name='index'),

   
    

    path('signup',views.signup,name='signup'),

    path('signin',views.signin,name='signin'),

    path('logout',views.logout,name='logout'),
    
    path('user_home',views.user_home,name='user_home'),

    path('admin_home',views.admin_home,name='admin_home'),

    path('department',views.department,name='department'),

    path('add_departments', views.add_departments, name="add_departments"),

    path('edit_department/<int:id>', views.edit_department, name="edit_department"),

    path('delete_department/<int:id>', views.delete_department, name="delete_department"),

    path('manage_task', views.manage_task, name="manage_task"),


    path('admin_task', views.admin_task, name="admin_task"),

    path('add_task', views.add_task, name="add_task"),

    path('edit_task/<int:id>', views.edit_task, name="edit_task"),

    path('delete_task/<int:id>', views.delete_task, name="delete_task"),

    path('admin_completed_task/<int:id>', views.admin_completed_task, name="admin_completed_task"),

    path('status/<int:id>', views.status, name="status"),

    path('manage_topic', views.manage_topic, name="manage_topic"),

    path('admin_topic', views.admin_topic, name="admin_topic"),

    path('add_topic', views.add_topic, name="add_topic"),

    path('previous_topic', views.previous_topic, name="previous_topic"),

    path('admin_attendance', views.admin_attendance, name="admin_attendance"),
    
    path('attendance_user/<int:id>', views.attendance_user, name="attendance_user"),

    path('add_attendance', views.add_attendance, name="add_attendance"),

    path('view_report', views.view_report, name="view_report"),


    path('report_status/<int:id>', views.report_status, name="report_status"),

    path('admin_payment', views.admin_payment, name="admin_payment"),

    path('view_leave', views.view_leave, name="view_leave"),

    path('leave_status<int:id>', views.leave_status, name="leave_status"),


    path('employee', views.employee, name="employee"),

    path('show_employee/<int:id>', views.show_employee, name="show_employee"),

    path('employee_status/<int:id>', views.employee_status, name="employee_status"),

    path('employee_delete/<int:id>', views.employee_delete, name="employee_delete"),



    

    


    




    


    # user

    path('user_task', views.user_task, name="user_task"),

    path('attendance', views.attendance, name="attendance"),


    path('apply_leave', views.apply_leave, name="apply_leave"),


    path('topic', views.topic, name="topic"),
    

    path('report', views.report, name="report"),
    

    path('payment', views.payment, name="payment"),

    path('emp_detailes', views.emp_detailes, name="emp_detailes"),


    path('task_to_do', views.task_to_do, name="task_to_do"),

   



    path('assigned_task/<int:id>', views.assigned_task, name="assigned_task"),

    path('completed_task', views.completed_task, name="completed_task"),



    path('current_topic', views.current_topic, name="current_topic"),

    path('user_previous_topic', views.user_previous_topic, name="user_previous_topic"),

    path('view_attendance', views.view_attendance, name="view_attendance"),

    path('report_issue', views.report_issue, name="report_issue"),

    path('issue', views.issue, name="issue"),

    path('reported_issue', views.reported_issue, name="reported_issue"),

    path('add_payment', views.add_payment, name="add_payment"),

    path('user_payment', views.user_payment, name="user_payment"),

    path('view_payment', views.view_payment, name="view_payment"),

    path('leave_apply', views.leave_apply, name="leave_apply"),

    path('leave', views.leave, name="leave"),

    path('applied_leave', views.applied_leave, name="applied_leave"),

    path('profile', views.profile, name="profile"),

    




    
    

    




    

    

    

  
   
]