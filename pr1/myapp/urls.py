from django.conf.urls.static import static 
from django.conf import settings
from .import views
from django.urls import path
from .views import report_issue_view



urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard1/', views.dashboard1, name='dashboard1'),
    path("admin-register/", views.admin_register, name="admin_register"),
    path("admin-login/", views.admin_login, name="admin_login"),
    path("super-login/", views.login_vieww, name="super_login"),
    path('book-login/', views.books_login, name='book_login'),
    path('', views.index, name='index'),
    path('add-book/', views.add_book, name='add_book'),
    path('add-gate/', views.add_gate, name='add_gate'),
    path('gate-login/', views.gate_login, name='gate_login'),
    path("staff/create/", views.staff_create, name="staff_create"),
    path("staff/list/", views.staff_list, name="staff_list"),
    path('scan/', views.scan_page, name='scan'),
    path("student/<int:student_id>/", views.student_detail, name="student_detail"),
    path("save_student/", views.save_student, name="save_student"),
    path("student-login/", views.student_login, name="student_login"),
    path("delete-login/", views.delete_login, name="delete_login"),
    path('available/', views.available_books, name='available'),
    path('avabilable-gate/', views.gate_books, name='avabilable_gate'),
    path("deletes-stud/", views.deletes_stud, name="deletes_stud"),
    path("borrow/", views.borrow, name="borrow"),
    path("borrow-gate/", views.borrow_gate, name="borrow_gate"),
    path("borrow-book/", views.borrow_view, name="borrow_book"),
    path("scan-book/", views.scan_book, name="scan_book"),
    path("scan-gate/", views.scan_gate, name="scan_gate"),
    path("borrow-list/", views.borrow_list, name="borrow_list"),
    path("borrow-listt/", views.borrow_listt, name="borrow_listt"),
    path("show/",views.show,name="delete_book" ),
    path("delete/<int:idn>",views.delete,name="delete"),
    path("show1/",views.show1,name="delete_student"),
    path("delete1/<int:idn1>",views.delete1,name="delete1"),
    path("bulk_upload_students/", views.bulk_upload_students, name="bulk_upload_students"),
    path("bulk_upload_books/", views.bulk_upload_books, name="bulk_upload_books"),
    path("books/<int:pk>/abstract/", views.book_abstract, name="book_abstract"),
    path('report-issue/', report_issue_view, name='report_issue'),
    path('search-borrow/', views.search_borrow, name='search_borrow'),
    path('newspaper-upload/',views. newspaper_upload, name="newspaper_upload"),
    path('newspaper-list/', views.newspaper_list, name="newspaper_list"),
    path('delete/<int:pk>/',views.newspaper_delete, name="newspaper_delete"),
    path("student-broad/", views.student_broad, name="student_broad"),
    path("report-issue/", views.report_issue, name="report_issue"),
    path("staff-dashboard/", views.staff_dashboard, name="staff_dashboard"),
    path("request-purchase/", views.request_purchase, name="request_purchase"),
    path("purchase-requests/", views.view_purchase_requests, name="purchase_requests_list"),
    path('purchase-request/approve/<int:pk>/', views.approve_request, name='approve_request'),
    path('purchase-request/reject/<int:pk>/', views.reject_request, name='reject_request'),
    path('exam-dashboard/', views.exam_dashboard, name='exam_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path("subbranches/<int:main_exam_id>/", views.subbranches, name="subbranches"),
    path("subbranch_details/<int:sub_exam_id>/", views.subbranch_details, name="subbranch_details"),
    path("request-purchase/", views.request_purchase, name="request_purchase"),
    path("notifications/mark-read/", views.mark_notifications_read, name="mark_notifications_read"),
    path("notifications/unread/", views.get_unread_notifications, name="get_unread_notifications"),
    path('generate-barcode/', views.generate_barcode_view, name="generate_barcode"),
    path('staff1-dashboard/', views.staff1_dashboard, name='staff1_dashboard'),
        # HOD Management URLs
    path("hod/create/", views.hod_create, name="hod_create"),
    path("hod/list/", views.hod_list, name="hod_list"),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('donate-books/', views.donate_book, name='donate-books'),
    path('donation-details/', views.donation_details, name='donation-details'),
    path('view-donors/', views.view_donors, name='view_donors'),

]


if settings.DEBUG:
# Serve static and media files during development
     urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)