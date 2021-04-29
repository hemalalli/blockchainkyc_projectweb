from django.shortcuts import render
from django.contrib import messages
from fileupload.models import files_upload, User_Profile, status,notifications
from bank1.models import ipfsmapping
import ipfsapi


def bankauthenticate(username, password):
    if (username == "bankadmin"):
        return True


def bank_user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = bankauthenticate(username=username, password=password)

        if user is True:
            # Save session as cookie to login the user
            # Success, now let's login the user
            user = User_Profile.objects.all()
            fu = files_upload.objects.all()
            statusf = status.objects.all()
            return render(request, 'search.html', {'user': user, 'fu': fu, 'status': statusf})
        else:
            # Incorrect credentials, let's throw an error to the screen.
            messages.error(request, 'username or password not correct')
            return render(request, 'b2login.html')
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'b2login.html')


def usersearch(request):
    if request.method == 'POST':
        uid = request.POST['username']


        api = ipfsapi.Client('127.0.0.1', 5001)
        try:
            u = User_Profile.objects.get(kycid=uid)
        except:
            messages.error(request, 'Userid ' + uid + ' is not valid KYC profile')
        else:
            nn = notifications.objects.get(nuid=u)

            if nn.approvestatus == "Accepted":
                files = {}
                messages.success(request, 'User ' + uid + ' has accepted your request to proceed with document verification and hence loading files from Blockchain')
                for n in ipfsmapping.objects.filter(userid=u.id).iterator():
                    print("Inside IPFS loop")
                    # print(n.ipfsid)
                    # res = api.cat(n.ipfsid)
                    # print(res)
                    # nam = res['name']
                    hashv = n.ipfsid
                    files[hashv] = n.fname
                return render(request, 'search.html', { 'files': files })
            else:

                nn.notify = "We (YesBank) would like to have access to review your documents"
                nn.approvestatus = "Approved"
                nn.save()
                messages.success(request, 'Notification sent to ' + uid + ' user to accept the review request')


        return render(request, 'search.html')



