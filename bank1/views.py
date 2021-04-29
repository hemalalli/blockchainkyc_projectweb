from django.shortcuts import render
from django.contrib import messages
from fileupload.models import files_upload, User_Profile, status, notifications
from .models import ipfsmapping
import ipfsapi
import json
from web3 import Web3, HTTPProvider
#from solc import compile_files


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
            return render(request, 'approvals.html', {'user': user, 'fu': fu, 'status': statusf})
        else:
            # Incorrect credentials, let's throw an error to the screen.
            messages.error(request, 'username or password not correct')
            return render(request, 'blogin.html')
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'blogin.html')


def bank_approval(request):
    return render(request, 'approvals.html')


#def smartcontract(hass):
 #   blockchain_address = 'http://127.0.0.1:9545'
  #  w3 = Web3(HTTPProvider(blockchain_address))
    # Set the default account (so we don't need to set the "from" for every transaction call)
    #w3.eth.defaultAccount = w3.eth.accounts[0]

    #compiled_sol = compile_files({
     #   "language": "Solidity",
      #  "sources": {
      #      "FixedSupplyToken.sol": {
      #          "urls": ["file:///Users/nithe/Documents/blockchain-eth/contracts/IPSFStoring.sol"]
      #      }
      #  }
    #}, allow_paths="file:///Users/nithe/Documents/blockchain-eth/contracts")

    #bytecode = compiled_sol['IPSFStoring.sol']
    #abi = json.loads(compiled_sol['IPSFStoring.sol'])['output']['abi']

    #hashing = w3.eth.contract(abi=abi, bytecode=bytecode)

    #tx_hash = hashing.constructor().transact()

    #tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    #hasher  = w3.eth.contract(
     #   address=tx_receipt.contractAddress,
      #  abi=abi
    #)

    #m = hasher.functions.sendHash(hass).transact()
    #print(m)

    #tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    #n = hasher.functions.getHash().call()

    #print(n)

def send_blockchain(request, kid):
    # This means the documents are APPROVED and sending to BlockChain
    api = ipfsapi.Client('127.0.0.1', 5001)
    u = User_Profile.objects.get(kycid=kid)

    for n in files_upload.objects.filter(fileid=u.id).iterator():
        res = api.add(n.filename)
        print(res)
        #hass = res['Hash']
        #smartcontract(hass)
        #{'Name': 'BeanPassport_SCj0aO4.jpg', 'Hash': 'QmShUEVGiypjngeqLdsmMVz41ScZYd9RJPNH8noK6MeMY2', 'Size': '12402'}
        #{'Name': 'BeanDrivingLicense.jpg', 'Hash': 'QmNqdfkB5f6A3gJJUSnA1scmZVmChj7BxG6JqbeLJyo2aA', 'Size': '138461'}

        w = ipfsmapping(ipfsid=res['Hash'],fname=res['Name'],userid=u)
        w.save()

    s = status(uid=u, status="Approved")
    s.save()

    try:
        nn = notifications(nuid=u, notify="Your documents are successfully approved and uploaded to Blockchain", approvestatus="Approved")
        nn.save()
    except:
        g = notifications.objects.get(nuid=u.id)
        g.notify="Your documents are successfully approved and uploaded to Blockchain"
        g.approvestatus="Approved"

    messages.success(request, 'User ' + kid + ' documents are approved and uploaded to IPSF, and also the user is notified ')
    user = User_Profile.objects.all()
    fu = files_upload.objects.all()
    statuf = status.objects.all()

    return render(request, 'approvals.html', {'user': user, 'fu': fu, 'status': statuf})


def document_rejected(request, kid):
    u = User_Profile.objects.get(kycid=kid)
    s = status(uid=u, status="Rejected")
    s.save()
    messages.success(request, 'User ' + kid + ' documents are rejected !!! ')
    user = User_Profile.objects.all()
    fu = files_upload.objects.all()
    statuf = status.objects.all()

    nn = notifications(nuid=u, notify="Your documents are rejected, please recheck the documents", approvestatus="Rejected")
    nn.save()

    try:
        nn = notifications(nuid=u, notify="Your documents are rejected, please recheck the documents", approvestatus="Rejected")
        nn.save()
    except:
        g = notifications.objects.get(nuid=u.id)
        g.notify="Your documents are rejected, please recheck the documents"
        g.approvestatus="Rejected"

    return render(request, 'approvals.html', {'user': user, 'fu': fu, 'status': statuf})
