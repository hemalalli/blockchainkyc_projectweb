from django.shortcuts import render
from django.contrib import messages
from .models import files_upload,User_Profile,status, notifications
from django.conf import settings as confset

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def authenticate(username):
    try:
        if (User_Profile.objects.get(kycid=username)):
            return True
    except:
        return False

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username)
        if user is True:
            # Save session as cookie to login the user
            # Success, now let's login the user.
            user = User_Profile.objects.get(kycid=username)

            try:
                notification = notifications.objects.get(nuid=user)
            except:
                return render(request, 'fileupload.html', {'user': user})
            else:
                return render(request, 'fileupload.html', {'user': user, 'notification': notification})

        else:
            # Incorrect credentials, let's throw an error to the screen.
            messages.error(request,'username or password not correct')
            return render(request, 'login.html')
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')


def upload(request,user):
    username = user
    print(request)

    bank = request.POST['bank']
    passport = request.FILES['passport']
    license = request.FILES['license']
    print(bank ,' ', passport ,' ', license)

    u = User_Profile.objects.get(kycid=user)
    #confset.MEDIA_ROOT

    p = files_upload(fileid=u, filetype="Passport", filename=passport)
    p.save()
    s = files_upload(fileid=u, filetype="License", filename=license)
    s.save()

    messages.success(request, 'User documents are uploaded successfully !')
    return render(request, 'fileupload.html', {"user": u})

def updatenotification(request, action, kid):
    u = User_Profile.objects.get(kycid=kid)
    g = notifications.objects.get(nuid=u.id)

    if action == "accept":
        g.approvestatus = "Accepted"
        g.notify = "Your documents are under processing by YES bank as per your approval"
        g.save()
        messages.success(request, 'Thanks for approving the request , YesBank will process your documents from Blockchain!')
        return render(request, 'fileupload.html', {"user": u, "notification":g, "notificationstatus":1})

    elif action == "reject":
        g.approvestatus = "Reject"
        g.notify = "Your documents are not shared to YES bank as you rejected the request from YES bank"
        g.save()
        messages.error(request,'Thanks for responding the request , YesBank will not process your documents!!!')
        return render(request, 'fileupload.html', {"user": u, "notification": g, "notificationstatus": 0})
    else:
        return render(request, 'fileupload.html')