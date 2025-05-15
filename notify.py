from dotenv import load_dotenv
import os
import sys
import requests

load_dotenv()

def init():
    # Check Environment Variables
    if os.environ.get('PB_PHONE_DEVICE_ID') is None:
        print("[FAIL]: Environment Variable PB_PHONE_DEVICE_ID is not set")
        sys.exit()
    if os.environ.get('PB_ACCESS_TOKEN') is None:
        print("[FAIL]: Environment Variable PB_ACCESS_TOKEN is not set")
        sys.exit()
    if os.environ.get('PB_ADDRESS') is None:
        print("[FAIL]: Environment Variable PB_ADDRESS is not set")
        sys.exit()

def send_sms(message):
    post_data = {
        'data' : {
            'addresses' : [os.environ.get('PB_ADDRESS')],
            'message' : message,
            'target_device_iden' : os.environ.get('PB_PHONE_DEVICE_ID')
        }
    }
    post_headers = {
        'Access-Token' : os.environ.get('PB_ACCESS_TOKEN')
    }
    r = requests.post('https://api.pushbullet.com/v2/texts', json=post_data, headers=post_headers)
    print('Notifying by SMS: ' + os.environ.get('PB_ADDRESS'))