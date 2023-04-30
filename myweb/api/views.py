from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from twilio.rest import Client

# Create your views here.
class SendSms(APIView):
    def get(self,request):


        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid ='AC4628a2327ba9240efbd749308e942668'
        auth_token = '718e1846a71e6d84b27c6dbbc9e8a668'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Hii Monu bhai  shopping ke liye chale",
                            from_='+14697079076',
                            to='+919582185588'
                        )

        print(message.sid)
        return Response({'status':'sent sms!!'})