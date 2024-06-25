


from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import auth,User
from django.http import HttpResponse, JsonResponse
import random
from django.contrib.auth import logout




# Create your views here.
def home(request):
    return render(request,'home.html')

def user_reg(request):
    
    if request.method=="POST":
        user_names=request.POST['user_name']
        child_names=request.POST['child_name']
        parent=request.POST['parent_name']
        addresses=request.POST['user_address']
        date_of_birth=request.POST['dob']
        emaill=request.POST['mail']
        ph_number=request.POST['contact_number']
        img=request.FILES['img']
        password1=request.POST['u_password']
        password2=request.POST['uu_password']
        user_approved=request.POST['user_appointment']

        if password1==password2:
            user=None
            if User.objects.filter(username=user_names).exists():
                user=User.objects.get(username=user_names)
                if users_reg.objects.filter(userr=user).exists():
                    print("already exists")
                    return render(request,'user_registration.html',{'key1':"USERNAME ALREADY EXISTS"})
            else:
                User.objects.create_user(username=user_names,password=password1).save()
                user=User.objects.get(username=user_names)
            if user:
                if users_reg.objects.filter(user_name=user_names).exists():
                    print("uname already exists")
                    return render(request,'user_registration.html',{'key1':"USERNAME ALREADY EXISTS"})
                else:
                    usave=users_reg(userr=user,user_name=user_names,child_name=child_names,parent_name=parent,address=addresses,birth_date=date_of_birth,email=emaill,contact_number=ph_number,image=img,password=password1,users_approve=user_approved)
                    usave.save()
                    print("saved")
                    return redirect(user_login)
                    # return render(request,'user_registration.html',{'key2':"SUCCESSFULLY SAVED"})
        else:
            return render(request,'user_registration.html',{'key':'password does not match'})
    else:
        return render(request,'user_registration.html')
    return render(request,'user_registration.html')
                




            
        
            

        
                
                
                
        

def user_login(request):
    if request.method=='POST':
        username=request.POST['uname']
        passwordd=request.POST['passwordd']
        if users_reg.objects.filter(user_name=username,password=passwordd).exists():
            d=users_reg.objects.get(user_name=username)
            if d.users_approve=="approved":

                user=auth.authenticate(username=username,password=passwordd)
                if user is not None:
                    auth.login(request,user)
                    print("login successfully")
                    return redirect(user_apply)
                else:
                    print("invalid login")
                    return render(request,'user_login.html',{'key':'Invalid Login'})
            else:
                print("username not found")

                return render(request,'user_login.html',{'key':'only approved user can login'})
        else:
                    print("invalid login")
                    return render(request,'user_login.html',{'key':'Invalid Login'})
    return render(request,'user_login.html')



def user_apply(request):
    user=users_reg.objects.get(userr=request.user)
    print("haiiiiiiiiiiiiii")
    print(type(user.age))
    b=user.age() 
    print(b)
    print(type(b))
    if user.age()==0:
        v1=vaccine_notification.objects.filter(v_age="DAY1")
        v2=vaccine_notification.objects.filter(v_age="WEEK 4")
        v3=vaccine_notification.objects.filter(v_age="WEEK 5")
        v4=vaccine_notification.objects.filter(v_age="WEEK 6")
        v5=vaccine_notification.objects.filter(v_age="6 MONTHS")
        v6=vaccine_notification.objects.filter(v_age="WEEK 9")
        v7=vaccine_notification.objects.filter(v_age="9 MONTHS")
        v8=vaccine_notification.objects.filter(v_age="6 MONTHS")
        v9=vaccine_notification.objects.filter(v_age="12 MONTHS")
        
        v11=vaccine_notification.objects.filter(v_age="3 MONTHS")




        
        context={
            'key1':v1,
            'key2':v2,
            'key3':v3,
            'key4':v4,
            'key5':v5,
            'key6':v6,
            'key7':v7,
            'key8':v8,
            'key9':v9,
            'key11':v11,

            # 'key12':user.payment_done    


        }
        return render(request,'users_apply.html',context)
    
    elif user.age()==1:
        va=vaccine_notification.objects.filter(v_age="15 MONTHS")
        v10=vaccine_notification.objects.filter(v_age="1 YEAR")

        context={'key1':va,'key2':v10}
        return render(request,'users_apply.html',context)
    elif user.age()==3:
        v=vaccine_notification.objects.filter(v_age="3 YEAR")
        context={'key1':v}
        return render(request,'users_apply.html',context)
    
    elif user.age()==7:
        v=vaccine_notification.objects.filter(v_age="7 YEAR")
        context={'key1':v}
        return render(request,'users_apply.html',context)
    
    elif user.age()==9:
        v=vaccine_notification.objects.filter(v_age="9 YEAR")
        v1=vaccine_notification.objects.filter(v_age="14 YEAR")

        context={'key1':v,'key2':v1}
        return render(request,'users_apply.html',context)
    
    elif user.age()==10 or user.age()==11 or user.age()==12 or user.age()==13 or user.age()==14:
        v=vaccine_notification.objects.filter(v_age="14 YEAR")
        context={'key1':v}
        return render(request,'users_apply.html',context)
    
    elif user.age()==15:
        v=vaccine_notification.objects.filter(v_age="15 YEAR")
        context={'key1':v}
        return render(request,'users_apply.html',context)
    
    else:
        context={'key22':'NO vaccination for this age'}
        return render(request,'users_apply.html',context)


        # return render(request,'users_apply.html',context)
    return render(request,'users_apply.html',{'key':user.age})

def user_profile_views(request):
    username=request.user
    n=users_reg.objects.filter(userr=username).all()
    di={'view':n}
    return render(request,'user_profile_view.html',di)



def update_user_profile(request,up):
    updates=users_reg.objects.get(id=up)
    user=User.objects.get(username=request.user)
    if request.method=="POST":
        updates.user_name=request.POST['up_username']
        updates.child_name=request.POST['up_child']
        updates.parent_name=request.POST['up_parent']
        updates.address=request.POST['up_address']

        updates.birth_date=request.POST['up_dob']
        # updates.age=request.POST['up_age']
        updates.email=request.POST['up_mail']
        updates.contact_number=request.POST['up_phn']
        user.username=request.POST['up_username']
        user.save()
        updates.save()
        user_app=user_appointment.objects.filter(userr=updates)
        for i in user_app:
            i.name=request.POST['up_username']
            i.mobile_number=request.POST['up_phn']
            i.email_address=request.POST['up_mail']
            i.save()
        return redirect(user_profile_views)
    return render(request,'user_profile_update.html',{'updates':updates})

def dietition(request):
    if request.method=="POST":
        dietition_username=request.POST['d_username']
        dietition_name=request.POST['d_name']
        dietition_dob=request.POST['d_dob']
        dietition_qulification=request.POST['d_qul']
        dietition_experience=request.POST['d_exp']
        dietition_no=request.POST['d_phn']
        diet_email=request.POST['mail']
        password1=request.POST['password']
        password2=request.POST['c_password']
        dietition_img=request.FILES['d_img']
        dietition_approvement=request.POST['dietition_approvement']
        # print(dietition_no)
        if password1==password2:
            user=None
            if User.objects.filter(username=dietition_username).exists():
                user=User.objects.get(username=dietition_username)
                if Dietition.objects.filter(user=user).exists():
                    print("diet already exits")
                    return render(request,'dietition_register.html',{'key':'Password doesnot match'})
            else:
                User.objects.create_user(username=dietition_username,password=password1).save()
                user=User.objects.get(username=dietition_username)
            if user:
                if Dietition.objects.filter(diet_Username=dietition_username).exists():
                    print("diet already exits")
                    return render(request,'dietition_register.html',{'key':'Password doesnot match'})
                else:
                    Dietition(user=user,diet_Username=dietition_username,diet_Name=dietition_name,diet_Date_of_Birth=dietition_dob,diet_Qualifications=dietition_qulification,diet_Experience=dietition_experience,diet_Mobile_no=dietition_no,email=diet_email,diet_password=password1,diet_Image=dietition_img,diet_approvement=dietition_approvement).save()
                    # return render(request,'dietition_register.html',{'key':"SUCCESSFULLY REGISTERD - WAIT FOR ADMIN APPROVAL"})/
                    return redirect(dietitionlog)
        else:
            return render(request,'dietition_register.html',{'key':'Password doesnot match'})
    return render(request,'dietition_register.html')

def dietitionlog(request):
    if request.method=="POST":
        dietition_username=request.POST["username"]
        password1=request.POST["password"]
        print(dietition_username)
        if Dietition.objects.filter(diet_Username=dietition_username,diet_password=password1).exists():
            d=Dietition.objects.get(diet_Username=dietition_username)
            if d.diet_approvement=="approved":
                u=auth.authenticate(username=dietition_username,password=password1)
                if u is not None:
                    auth.login(request,u)
                    return redirect(dietition_apply)
                else:
                    return render(request,'dietition_login.html',{'keys1':"Invalid User"})
            else:

                print("waiting for admin approval")
                return render(request,'dietition_login.html',{'keys1':"waiting for admin approval"})
        else:
            print('invalid')
            return render(request,'dietition_login.html',{'keys1':"Invalid User"})
    return render(request,'dietition_login.html')


def d_profile_view(request):
     
    username=request.user
    u=Dietition.objects.filter(user=username).all()
    di={'view':u}
    return render(request,'dietition_profile.html',di)

    
def dietition_apply(request):
    return render(request,'dietition_apply.html')

def update_dietition_profile(request,upd):
    updates=Dietition.objects.get(id=upd)
    if request.method=="POST":
        updates.diet_Username=request.POST['up_username']
        updates.diet_Name=request.POST['up_name']
        updates.diet_Date_of_Birth=request.POST['up_dob']
        updates.diet_Qualifications=request.POST['up_qualification']
        updates.diet_Experience=request.POST['up_experience']
        updates.diet_Mobile_no=request.POST['up_phn']
        updates.email=request.POST['up_email']
        updates.diet_Image=request.FILES['up_image']

        updates.save()
        return redirect(d_profile_view)
    return render(request,'dietition_profile_update.html',{'updates':updates})
#######
def dietition_list_views(request):
    user=users_reg.objects.get(userr=request.user)
    s=Dietition.objects.filter(diet_approvement="approved")
    # a=user_appointment.objects.filter(userr_appointment=s.)
    d={'view':s}
    return render(request,'dietition_list_views.html',d)

# def dietition_list_views1(request,views):
    
#     store=Dietition.objects.get(id=views)
   
#     return render(request,"dietition_list_views1.html",{'d_view':store})


def add_plan(request):
    print(request.user)
    users=Dietition.objects.get(user=request.user)
    print(users)
    if request.method=="POST":
        std_three_months=request.POST['three_month']
        std_six_months=request.POST['six_month']
        std_one_yrs=request.POST['one_year']
        ex_three_months=request.POST['three_months']
        ex_six_months=request.POST['six_months']
        ex_one_yrs=request.POST['one_years']

        if add_plans.objects.filter(user=users).exists() or plan.objects.filter(user=users).exists():
            print("alredy exist")
            return render(request,'add_payment_plans.html')

        else:
            
            add_plans(user=users,std_three_month=std_three_months,std_six_month=std_six_months,std_one_yr=std_one_yrs).save()

            plan(user=users,ex_three_month=ex_three_months,ex_six_month=ex_six_months,ex_one_yr=ex_one_yrs).save()
            return render(request,'add_payment_plans.html',{'key':"successfully entered"})
    return render(request,'add_payment_plans.html')




def view_plan(request,id):
    
    
    table1_data = add_plans.objects.filter(user=id)
    table2_data = plan.objects.filter(user=id)
    plans = {
        'standard': table1_data,
        'exclusive': table2_data,
    }
    return render(request, 'user_view_plans.html', plans)



def dietition_view_plan(request):
    print(request.user)

    users=Dietition.objects.get(user=request.user)
    print(users.user_id)

    table1_datas = add_plans.objects.filter(user=users)
    table2_datas = plan.objects.filter(user=users)
    planss = {
        'standard': table1_datas,
        'exclusive': table2_datas,
    }
    return render(request, 'dietition_view_plan.html', planss)

def update_standard_plans(request,up_plan):
    updates=add_plans.objects.get(id=up_plan)
    if request.method=="POST":
        updates.std_three_month=request.POST['up_three_month']
        updates.std_six_month=request.POST['up_six_month']
        updates.std_one_yr=request.POST['up_one_year']

        # updates.ex_three_month=request.POST['up_three_months']
        # updates.ex_six_month=request.POST['up_six_months']
        # updates.ex_one_yr=request.POST['up_one_years']
        updates.save()
        return redirect(dietition_view_plan)
    return render(request,'update_standard_plans.html',{'updates':updates})

def update_exclusive_plans(request,p):
    update=plan.objects.get(id=p)
    if request.method=="POST":

        update.ex_three_month=request.POST['up_three_months']
        update.ex_six_month=request.POST['up_six_months']
        update.ex_one_yr=request.POST['up_one_years']
        update.save()
        return redirect(dietition_view_plan)
    return render(request,'update_exclusive_plan.html',{'updates':update})


def dietition_delete_std_plan(request,tk):
    de=add_plans.objects.get(id=tk)
    de.delete()
    return redirect(dietition_view_plan)


def dietition_delete_ex_plan(request,bk):
    d=plan.objects.get(id=bk)
    d.delete()
    return redirect(dietition_view_plan)

def payment(request):
    return render(request,'payments.html')

def booked_success(request):
    return render(request,'booked_success.html')
#
def payment_details(request):
    if request.method=="POST":
        print("loading")
        name_of_card=request.POST['cardname']
        number_of_card=request.POST['cardnum']
        date_expiry=request.POST['ex_date']
        security=request.POST['code']
        post_code=request.POST['zip_code']
        paid_details(card_name=name_of_card,card_number=number_of_card,expiry_date=date_expiry,security_code=security,postal_code=post_code).save()
        print("saved")
        return redirect(booked_success)
    return render(request,'payments.html')




def appointment(request,pk):
    rand=random.randint(0000,9999)
    paids=users_reg.objects.get(userr=request.user)
    diet=Dietition.objects.get(id=pk)
    context={
        'key1':paids,
        'key2':diet
    }


    

    if request.method=="POST":


        u_name=request.POST['user_name']
        phone_number=request.POST['ph_number']
        email=request.POST['mail']
        d_name=request.POST['dietition_name']
        choosed_plan=request.POST['choose_plan']
        duration=request.POST['choose_duration']
        # name1=paids.user_name
        
        # payments(name=u_name,amount=)
        if choosed_plan=="Standard Plan":
            if duration=="3 Month":
                a=add_plans.objects.get(user_id=pk)
                print(a.std_three_month)
                b=a.std_three_month
            elif duration=="6 Month":
                six=add_plans.objects.get(user_id=pk)
                print(six.std_six_month)
                b=six.std_six_month
            elif duration=="1 Year":
                one=add_plans.objects.get(user_id=pk)
                print(one.std_one_yr)
                b=one.std_one_yr
        if choosed_plan=="Exclusive Plan":
            if duration=="3 Month":
                three=plan.objects.get(user_id=pk)
                print(three.ex_three_month)
                b=three.ex_three_month
            elif duration=="6 Month":
                s=plan.objects.get(user_id=pk)
                print(s.ex_six_month)
                b=s.ex_six_month
            elif duration=="1 Year":
                o=plan.objects.get(user_id=pk)
                print(o.ex_one_yr)
                b=o.ex_one_yr
        user_appointment(userr_appointment_id=pk,userr=paids,name=u_name,mobile_number=phone_number,email_address=email,name_of_dietition=d_name,choose_a_plan=choosed_plan,duration_of_plan=duration,payment_amount=b,chat_code=str(rand)).save()
        dic={'key':b}
        

                
            
        
        
            # add_plans.get(user_id=pk)
        
        return render(request,'payments.html',dic)
        # return render(request,'user_appointment.html')
    return render(request,'user_appointment.html',context)





def appointment_view_for_dietition(request):
    print(request.user)
    user=User.objects.get(username=request.user)
    a=Dietition.objects.get(user=user)
    print(a.diet_Name)
    appointment_view=user_appointment.objects.filter(userr_appointment=a)
    dietition_view={'view':appointment_view}
    return render(request,'view_appointments.html',dietition_view)

def user_feedbacks(request):
    print(request.user)
    userrs=users_reg.objects.get(userr=request.user)
    print(userrs.user_name)
    if request.method=="POST":
           full_name=request.POST['name']
           dietition_name=request.POST['diet_name']
           feedbacks=request.POST['feedback']
           rate=request.POST['rate']
           print(rate)
           rateof5=(int(rate)/100)*5
           print(rateof5)
           diet=Dietition.objects.get(diet_Username=dietition_name)
           diet.rating=rateof5
           diet.save()
           user_feedback(userr_feedback=userrs,name_of_user=full_name,Name_of_dietition=dietition_name,feedback=feedbacks,rating=rateof5).save()
           return render(request,'user_feedback.html',{'key':"successfully entered"})
    return render(request,'user_feedback.html',{'key1':userrs})


def user_view_feedbacks(request):

    username=request.user

    feed_back=users_reg.objects.get(userr=request.user)
    # print(feed_back.user_name)

    feedback_view=user_feedback.objects.filter(userr_feedback=feed_back)
    di={'views':feedback_view}
    return render(request,'feedback_view_for_user.html',di)


def user_view_feedbacks_delete(request,fb):
    d=user_feedback.objects.get(id=fb)
    d.delete()
    return redirect(user_view_feedbacks)

def feedback_view_for_dietition(request):
    b=request.user
    diet_view=Dietition.objects.get(user=request.user)
    print(diet_view.diet_Username)

    feed_back_view=user_feedback.objects.filter(Name_of_dietition=diet_view.diet_Username)
    di={'view':feed_back_view}
    return render(request,'feedback_view_for_dietition.html',di)

def vaccination_page(request):
    return render(request,'vaccination_details.html')

def feedback_views_for_all(request):
    feedbacks=user_feedback.objects.all()
    di={'view':feedbacks}
    return render(request,'view_all_feedbacks.html',di)

def admin_apply(request):
    return render(request,'admin_apply.html')


def complaints(request,pk):
    user=users_reg.objects.get(userr=request.user)
    diet=Dietition.objects.get(id=pk)
    comp=user_complaint.objects.filter(user=user)
    context={
        'key1':user,
        'key2':diet,
        'key3':comp
    }
    if request.method=="POST":
        names=request.POST['name']
        diet_names=request.POST['d_name']
        complaints=request.POST['complaint']
        user_complaint(user=user,name=names,diet_name=diet_names,issues=complaints).save()
        comp=user_complaint.objects.filter(user=user)
        context={
            'key1':user,
            'key2':diet,
            'key3':comp
        }
        return render(request,'post_complaints.html',context)
    return render(request,'post_complaints.html',context)



def activities(request):
    return render(request,'activities.html')

def add_videos(request):
    if request.method=="POST":
        print("hello")
        ages=request.POST['ages']
        video_names=request.POST['name_of_video']
        video=request.FILES['uploads_video']
        videos(age=ages,videos=video,video_name=video_names).save()
        return render(request,'activity_add_video.html',{'key':"successfully enetered"})
    return render(request,'activity_add_video.html')

def add_story(request):
    if request.method=="POST":
        print("hello")
#         print('oiiiiiiiiiii')
        ages=request.POST['ages']
        story_name=request.POST['name_of_story']
        storyy=request.FILES['uploads_video']
        stories(age=ages,story=storyy,story_name=story_name).save()
        return render(request,'activity_add_story.html',{'key':"successfully enetered"})
    return render(request,'activity_add_story.html')


    

def add_picture(request):
    if request.method=="POST":
        ages=request.POST['ages']
        pic_name=request.POST['name_of_picture']
        imgs=request.FILES['uploads_image']
        images(age=ages,images=imgs,image_name=pic_name).save()
        return render(request,'activity_add_image.html',{'key':"successfully enetered"})
    return render(request,'activity_add_image.html')

def add_lullaby(request):
    if request.method=="POST":
        ages=request.POST['ages']
        lullaby_name=request.POST['name_of_lullaby']
        lullabies=request.FILES['uploads_lullaby']
        lullaby(age=ages,lullaby=lullabies,lullaby_name=lullaby_name).save()
        return render(request,'activity_add_lullaby.html',{'key':"successfully enetered"})
    return render(request,'activity_add_lullaby.html')


def add_healthy_tip(request):
    
    return render(request,'add_healthytips.html')


def dietchart(request):
    return render(request,'add_diet_chart.html')



def add_diet_chart(request):
    doc=Dietition.objects.get(user=request.user)
    print(request.user)
    print("hii")

    if request.method=="POST":
        dietion_name=request.POST['diet_name']
        chart=request.POST['chart1']
        charts=request.POST['chart2']
        
        diet_chart(diets=doc,diet_name=dietion_name,chart_heading=chart,explanation=charts).save()
        return render(request,'add_chart.html')
    return render(request,'add_chart.html')

def alogin(request):
    if request.method=="POST":
        print("hai")
        uname=request.POST['uname']
        pass1=request.POST['psw'] 
        u=auth.authenticate(username=uname,password=pass1)
        print(u)
        print(u.is_superuser)
        if u is not None and u.is_superuser==True:
            auth.login(request,u)
            return redirect(admin_apply)
        
        else:
            return render(request,'admin_login.html',{'key':'invalid superuser'})
    
    return render(request,'admin_login.html')

def admin_add_tips(request):
    if request.method=="POST":
        healthy_tip=request.POST['day_tip']
        healthy_tips=request.POST['tip']
        add_healthy_tips(tips=healthy_tip,tip=healthy_tips).save()
        return render(request,'admin_add_tip.html',{'key':"successfully enetered"})
    return render(request,'admin_add_tip.html')

def admin_tip_view(request):
    
    s=add_healthy_tips.objects.all()
    d={'view':s}
    return render(request,'admin_view_tip.html',d)


######

def admin_delete_tip(request,dk):
    d=add_healthy_tips.objects.get(id=dk)
    d.delete()
    return redirect(admin_tip_view)


def admin_feedback_view(request):
    feedback=user_feedback.objects.all()
    di={'view':feedback}
    return render(request,'admin_feedback_view.html',di)

def admin_complaints_view(request):
    complaints_view=user_complaint.objects.all()
    di={'view':complaints_view}
    return render(request,'admin_complaint_view&reply.html',di)

def admin_complaint_reply(request,pk):
    # user=users_reg.objects.get(userr=request.user)
    # context={'key1':user}

    comp_reply=user_complaint.objects.get(id=pk)
    print(comp_reply.issues)

    if request.method=="POST":
        # person_name=request.POST['person_name']
        complaint_reply=request.POST['reply']
        #
        comp_reply.admin_reply=complaint_reply
        comp_reply.save()


        # admin_reply(reply=complaint_reply).save()
        return render(request,'admin_complaint_reply.html',{'key':"successfully enetered"})
    return render(request,'admin_complaint_reply.html')

def admin_complaint_reply_view(request):
    return render(request,'admin_complaint_reply.html')

#waiting response


def admin_view_dietitian(request):
    s=Dietition.objects.all()
    d={'view':s}
    return render(request,'admin_view_dietitions.html',d)

def admin_approve(request,tk):
    rej=Dietition.objects.get(id=tk)
    rej.diet_approvement='approved'
    rej.save()
    return redirect(admin_view_dietitian)

def admin_dietition_delete(request,tk):
    d=Dietition.objects.get(id=tk)
    d.delete()
    return redirect(admin_view_dietitian)


    
def admin_update_dietition_profile(request,upd):
    updates=Dietition.objects.get(id=upd)
    if request.method=="POST":
        updates.diet_Username=request.POST['up_username']
        updates.diet_Name=request.POST['up_name']
        updates.diet_Date_of_Birth=request.POST['up_dob']
        updates.diet_Qualifications=request.POST['up_qualification']
        updates.diet_Experience=request.POST['up_experience']
        updates.diet_Mobile_no=request.POST['up_phn']
        updates.email=request.POST['up_mail']
        updates.diet_Image=request.POST['up_image']

        updates.save()
        return redirect(admin_view_dietitian)
    return render(request,'admin_update_dietitions.html',{'updates':updates})


#chat

def chat_homes(request,pk):
    a=request.user
    user=user_appointment.objects.get(id=pk)
    return render(request, 'chat_home.html',{'key':user,'key1':a})

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Messages.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Messages.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


def appointments_view_for_user(request):
    print(request.user)
    
    a=users_reg.objects.get(user_name=request.user)
    print(a.user_name)
    # appointment_view=user_appointment.objects.filter(name=request.user)

    appointment_view=user_appointment.objects.filter(userr=a)
    dietition_view={'view':appointment_view}
    return render(request,'users_view_appointment.html',dietition_view)

def users_view_healthy_tips(request):
    s=add_healthy_tips.objects.all()
    d={'view':s}
    return render(request,'user_view_healthytips.html',d)

def user_view_dietchart_tips(request,pk):
    b=Dietition.objects.get(id=pk)
    print("hai")
    print(b)
    s=diet_chart.objects.filter(diets=b)
    di={'view':s}
    return render(request,'user_views_the_addchart.html',di)

######################################################################################
#checkit
def admin_view_dietchart_tips(request):
    print(request.user)
    user=User.objects.get(username=request.user)
    a=Dietition.objects.get(user=user)
    print("haii")
    # print(a.user)
    print(a.diet_Name)
    chart=diet_chart.objects.filter(diets=a)
    di={'view':chart}
    return render(request,'admin_view_diet_chart.html',di)
#####################################3
# def user_view_dietchart(request,pk):
#     a=users_reg.objects.get(userr=request.user)
#     b=user_appointment.objects.get(id=pk)
#     print("hai")
#     print(a.user_name)

#     c=diet_chart.objects.filter(diet_name=b.name_of_dietition)
#     d={'view':c}
#     return render(request,'user_views_the_addchart.html',d)


def admin_dietchart_delete(request,tk):
    d=diet_chart.objects.get(id=tk)
    d.delete()
    return redirect(admin_view_dietchart_tips)

def activity_view_videos(request):
    a=users_reg.objects.get(userr=request.user)
    print(a.age)

    if a.age()<=5:
        activity=videos.objects.filter(age=5)
        print("yes")
        dict={'key':activity}
        return render(request,'user_view_the_activity.html',dict)
    elif a.age()>5 and a.age()<=10:
        activity=videos.objects.filter(age=10)
        print("invalid")
        dict={'key':activity}
        return render(request,'user_view_the_activity.html',dict)
    elif a.age()>10 and a.age()<=16:
        activity=videos.objects.filter(age=16)
        print("valid")
        dict={'key':activity}
        return render(request,'user_view_the_activity.html',dict)
    else:
        print("hai")
        return render(request,'user_view_the_activity.html',{'key1':"there is no vedio's for you"})
    # dict={'key':activity}
    return render(request,'user_view_the_activity.html')

def activities_view_for_users(request):
    return render(request,'activities_view_for_user.html')


def activity_view_story(request):
    a=users_reg.objects.get(userr=request.user)
    print(a.age)

    if a.age()<=5:
        activity=stories.objects.filter(age=5)
        print("yes")
        dict={'key':activity}
        return render(request,'user_view_the_activity_story.html',dict)
    elif a.age()>5 and a.age()<=10:
        activity=stories.objects.filter(age=10)
        print("invalid")
        dict={'key':activity}
        return render(request,'user_view_the_activity_story.html',dict)
    elif a.age()>10 and a.age()<=16:
        activity=stories.objects.filter(age=16)
        print("valid")
        dict={'key':activity}
        return render(request,'user_view_the_activity_story.html',dict)
    else:
        print("hai")
        return render(request,'user_view_the_activity_story.html',{'key1':"there is no vedio's for you"})

def activity_view_image(request):
    a=users_reg.objects.get(userr=request.user)
    print(a.age)

    if a.age()<=5:
        activity=images.objects.filter(age=5)
        print("yes")
        dict={'key':activity}
        return render(request,'user_view_the_activity_picture.html',dict)
    elif a.age()>5 and a.age()<=10:
        activity=images.objects.filter(age=10)
        print("invalid")
        dict={'key':activity}
        return render(request,'user_view_the_activity_picture.html',dict)
    elif a.age()>10 and a.age()<=16:
        activity=images.objects.filter(age=16)
        print("valid")
        dict={'key':activity}
        return render(request,'user_view_the_activity_picture.html',dict)
    else:
        print("hai")
        return render(request,'user_view_the_activity_picture.html',{'key1':"there is no vedio's for you"})
    

def activity_view_lullaby(request):
    a=users_reg.objects.get(userr=request.user)
    print(a.age)

    if a.age()<=5:
        activity=lullaby.objects.filter(age=5)
        print("yes")
        dict={'key':activity}
        return render(request,'user_view_the_activity_lullaby.html',dict)
    elif a.age()>5 and a.age()<=10:
        activity=lullaby.objects.filter(age=10)
        print("invalid")
        dict={'key':activity}
        return render(request,'user_view_the_activity_lullaby.html',dict)
    elif a.age()>10 and a.age()<=16:
        activity=lullaby.objects.filter(age=16)
        print("valid")
        dict={'key':activity}
        return render(request,'user_view_the_activity_lullaby.html',dict)
    else:
        print("hai")
        return render(request,'user_view_the_activity_lullaby.html',{'key1':"there is no vedio's for you"})
    

def about(request):
    return render(request,'about.html')


def user_logout(request):
    logout(request)
    return redirect(home)

def dietitian_logout(request):
    logout(request)
    return redirect(home)

def admin_logout(request):
    logout(request)
    return redirect(home)


def admin_view_user(request):
    user_view=users_reg.objects.all()
    di={'view':user_view}
    return render(request,'admin_view_users.html',di)

def admin_approve_user(request,tk):
    rej=users_reg.objects.get(id=tk)
    rej.users_approve='approved'
    rej.save()
    return redirect(admin_view_user)

def admin_delete_user(request,pk):
    d=users_reg.objects.get(id=pk)
    d.delete()
    return redirect(admin_view_user)

def admin_view_activities(request):
    return render(request,'admin_view_activities.html')

def admin_view_pictures(request):
    admin_view=images.objects.all()
    dic={'view':admin_view}
    return render(request,'admin_view_picture.html',dic)

def admin_view_videos(request):
    video_view=videos.objects.all()
    d={'view':video_view}
    return render(request,'admin_view_videos.html',d)

def admin_view_story(request):
    story_view=stories.objects.all()
    di={'view':story_view}
    return render(request,'admin_view_story.html',di)

def admin_view_lullaby(request):
    l_view=lullaby.objects.all()
    di={'view':l_view}
    return render(request,'admin_view_lullaby.html',di)

def admin_delete_picture(request,pk):
    d=images.objects.get(id=pk)
    d.delete()
    return redirect(admin_view_pictures)

def admin_delete_video(request,tk):
    d=videos.objects.get(id=tk)
    d.delete()
    return redirect(admin_view_videos)

def admin_delete_story(request,sk):
    d=stories.objects.get(id=sk)
    d.delete()
    return redirect(admin_view_story)

def admin_delete_lullaby(request,lk):
    d=lullaby.objects.get(id=lk)
    d.delete()
    return redirect(admin_view_lullaby)
