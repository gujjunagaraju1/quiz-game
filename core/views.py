from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import QuizCategory,QuizQuestions,UserSubmitAnswer,UserTotalScore,CertifiedAlready
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    return render(request,'main.html')

def register(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        phone=request.POST['phone']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 == pass2:
            username=email.split('@')[0]
            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            
            mail_subject="Thank you for register"
            message=render_to_string('mail.html',
                                 {
                                     'myuser':myuser
                                 })
            to_email=email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            #send_email.attach_file('GUJJU_NAGARAJU_2023 (4).pdf')
            send_email.send()
      
        
       
        return redirect('login')
       
    
    
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['pass1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
           
            return redirect('home')
        else:
          return redirect('login')
        
    return render(request,'login.html')
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


def category(request):
    category=QuizCategory.objects.all()
    
   
    
   
    context={
        'category': category,
        
    }
    return render(request,'category.html',context)
@login_required(login_url='login')
def category_question(request,cat):
    user=request.user
    category=QuizCategory.objects.get(id=cat)
    questions=QuizQuestions.objects.filter(category__id=cat).order_by('id').first() 
   

    
    try:
        result=CertifiedAlready.objects.get(user=user,category=category)
    except CertifiedAlready.DoesNotExist:
        result=None
        
    context={
        'category':category,
        'questions':questions,
        'result':result
      }
    return render(request,'category_question.html',context)
        
    
    
   
 
    
  
    
    
    
    

def submit_question(request,cat,prodt):
    if request.method=="POST":
        category=QuizCategory.objects.get(id=cat)
        questions=QuizQuestions.objects.filter(category=category,id__gt=prodt).order_by('id').first()
        if 'skip' in request.POST:
            quest=QuizQuestions.objects.get(id=prodt)
            user=request.user
            answer="Not Submitted"
            saveAnswer=UserSubmitAnswer.objects.create(question=quest,right_answer=answer,user=user,category=category)
            saveAnswer.save()
            if questions: 
                
                context={'questions':questions,'category':category}
                return render(request,'category_question.html',context)
           
    
        else:
            question=QuizQuestions.objects.get(id=prodt)
            answer=request.POST['answer']
            user=request.user
            saveAnswer=UserSubmitAnswer.objects.create(question=question,right_answer=answer,user=user,category=category)
            saveAnswer.save()
            
        if questions:
            context={'questions':questions,'category':category}
            return render(request,'category_question.html',context)
        else:
            
            
            result=UserSubmitAnswer.objects.filter(user=request.user,category=category)
            v=[]
            score=0
            Total=0
            
            for i in result:
                if i.question in v:
                    pass
                else:
                    Total+=1
                    v.append(i.question)
                    if i.question.right_opt == i.right_answer:
                        score=score+1
            percent=((score)/Total)*100 
            
            TotalScore=UserTotalScore.objects.create(user=request.user,Score=score,category=category,Total=Total,percentage=percent) 
            TotalScore.save()
            result.delete()
            
            if percent >= 70:
                certified=CertifiedAlready.objects.create(user=request.user,category=category,certified=True)
                certified.save()
                context={
                    'certified':certified,
                    
                }
                
                return redirect('certified',cat=category.id)
            else:
                return redirect('not_certified')
 
            
             
            
           
    else:
        return HttpResponse('wrong call')

def  result(request):
    result=UserTotalScore.objects.filter(user=request.user).order_by('-id').first()
    total=CertifiedAlready.objects.filter(user=request.user)
    total_count=total.count()

    
   
    context={
        'result':result,
        'total':total,
        'total_count':total_count
      
    }
    return render(request,'dashboard.html',context)
    
def certified(request,cat):
    get=CertifiedAlready.objects.get(user=request.user,category__id=cat)
    #use_id=CertifiedAlready.objects.all()
    context={
        'get':get,
       
    }
    
    return render(request,'certificate_download.html',context)

def not_certified(request):
    return render(request,'not_certified.html')


def view_history(request):
    history=UserTotalScore.objects.filter(user=request.user).order_by('-id')
    context={
        'history':history
    }
    return render(request,'view_history.html',context)

def change_password(request):
    if request.method=="POST":
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']
        user=User.objects.get(username__exact=request.user.username)
        if new_password==confirm_password:
            sucess=user.check_password(current_password)
            if sucess:
                user.set_password(new_password)
                user.save()
                return redirect('home')
            else:
                return redirect('change_password')
        
    return render(request,'change_password.html')



