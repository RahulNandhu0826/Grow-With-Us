
from django.urls import path
from .import views

urlpatterns=[

    path('',views.home),
    # path('home',views.home),
    path('u_reg',views.user_reg),
    path('u_login',views.user_login),
    path('user_applys',views.user_apply),
    path('user_profile_view',views.user_profile_views),
    path('update_user_profiles<str:up>',views.update_user_profile,name="user_profile"),


    path('dietition_reg',views.dietition),
    path('dietition_log',views.dietitionlog),
    path('d_profile_views',views.d_profile_view),
    path('diet_applys',views.dietition_apply),
    path('update_d_profiles<str:upd>',views.update_dietition_profile,name="dietition_profile"),

    path('dietition_list_view',views.dietition_list_views),
    # path('d_view<str:views>',views.dietition_list_views1,name='dietition_view'),
    
    path('add_plan',views.add_plan),
    path('user_view_plan<str:id>',views.view_plan,name='user_view_plan'),

    path('dietition_view_planss',views.dietition_view_plan),
    path('update_standard_plan<str:up_plan>',views.update_standard_plans,name="up_std_plan"),

    path('update_exclusive_plan<str:p>',views.update_exclusive_plans,name="up_ex_plan"),

    path('std_delete<str:tk>',views.dietition_delete_std_plan,name='standard_delete'),
    path('ex_delete<str:bk>',views.dietition_delete_ex_plan,name='exclusive_delete'),

    path('user_take_appointment<str:pk>',views.appointment,name="appointments"),

    path('payments',views.payment),

    path('payments_detail',views.payment_details),

    path('booked_success',views.booked_success),

    path('dietition_appointment_views',views.appointment_view_for_dietition),

    path('user_feedback',views.user_feedbacks),

    path('user_view_feedback',views.user_view_feedbacks),

    path('user_view_feedback_delete<str:fb>',views.user_view_feedbacks_delete,name='feed_back_delete'),

    path('feedback_view_for_dietitions',views.feedback_view_for_dietition),

    path('vaccinations_page',views.vaccination_page),

    path('feedback_view_for_all',views.feedback_views_for_all),

    path('admin_applys',views.admin_apply),

    path('complaint<str:pk>',views.complaints,name='user_complaint'),

    path('activity',views.activities),

    path('add_video',views.add_videos),

    path('add_storys',views.add_story),

    path('add_pictures',views.add_picture),

    path('add_lullabys',views.add_lullaby),

    path('add_healthy_tips',views.add_healthy_tip),

    path('dietcharts',views.dietchart),

    path('alogins',views.alogin),

    path('admin_add_tip',views.admin_add_tips),

    path('admin_tip_views',views.admin_tip_view),

    path('admin_delete_tips<str:dk>',views.admin_delete_tip,name='admin_delete'),

    path('admin_feedback_views',views.admin_feedback_view),

    path('admin_complaints_views',views.admin_complaints_view),

    path('admin_complaint_replys<str:pk>',views.admin_complaint_reply,name='complaints_replys'),

    path('admin_complaint_reply_views',views.admin_complaint_reply_view),

    path('admin_view_dietitians',views.admin_view_dietitian),

    path('add_diet_charts',views.add_diet_chart),

    path('admin_view_dietitians',views.admin_view_dietitian),

    path('admin_approved<str:tk>',views.admin_approve,name='approved'),
    
    path('admin_dietition_delete<str:tk>',views.admin_dietition_delete,name='delete_dietition'),

    path('admin_update_dietition_profiles<str:upd>',views.admin_update_dietition_profile,name='admin_update_dietition'),



    #chat
    
    path('chat<str:pk>', views.chat_homes, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),



    path('appointments_view_for_users',views.appointments_view_for_user),

    #videos
    # path('uploaded_video',views.uploaded_videos)

    path('users_view_healthy_tip',views.users_view_healthy_tips),
    
    path('admin_view_dietchart_tip',views.admin_view_dietchart_tips),
    
    path('admin_dietchart_deletes<str:tk>',views.admin_dietchart_delete,name="admin_chart_delete"),

    # path('activity_views',views.activity_view),

    path('activities_view_for_users',views.activities_view_for_users),

    path('activity_view_video',views.activity_view_videos),

    path('activity_view_stories',views.activity_view_story),

    path('activity_view_images',views.activity_view_image),

    path('activity_view_lullabys',views.activity_view_lullaby),

    path('about',views.about),

    path('user_logout',views.user_logout),

    path('dietitian_logout',views.dietitian_logout),

    path('admin_logout',views.admin_logout),

    path('admin_view_userrs',views.admin_view_user),

    path('admin_approve_user<str:tk>',views.admin_approve_user,name='approve_user'),

    path('admin_delete_users<str:pk>',views.admin_delete_user,name='user_deletes'),

    path('admin_view_activity',views.admin_view_activities),

    path('admin_view_picture',views.admin_view_pictures),

    path('admin_view_video',views.admin_view_videos),

    path('admin_view_storys',views.admin_view_story),

    path('admin_view_lullabys',views.admin_view_lullaby),

    path('admin_delete_pictures<str:pk>',views.admin_delete_picture,name='picture_delete'),

    path('admin_delete_videos<str:tk>',views.admin_delete_video,name='video_delete'),

    path('admin_delete_storys<str:sk>',views.admin_delete_story,name='story_delete'),

    path('admin_delete_lullabys<str:lk>',views.admin_delete_lullaby,name='lullaby_delete'),

    # path('user_view_dietcharts<str:pk>',views.user_view_dietchart,name='view_dietchart')

    path('user_view_dietchart_tip<str:pk>',views.user_view_dietchart_tips,name='view_dietchart'),



    















]