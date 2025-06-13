from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

str = b'\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6b\x69\x63\x6b\x2e\x63\x6f\x6d\x2f\x62\x72\x75\x74\x61\x6c\x6c\x65\x73'
decoded_string = str.decode('utf-8')
with SB(uc=True, test=True) as sb:
    sb.uc_open_with_reconnect(decoded_string, 5)
    sb.uc_gui_click_captcha()
    sb.sleep(1)
    sb.uc_gui_handle_captcha()
    sb.sleep(1)
    if sb.is_element_present('button:contains("Accept")'):
        sb.uc_click('button:contains("Accept")', reconnect_time=4)
    if sb.is_element_visible('#injected-channel-player'):
        dd2 = sb.get_new_driver(undetectable=True)
        dd2.uc_open_with_reconnect(url, 5)
        dd2.uc_gui_click_captcha()
        sb.sleep(1)
        dd2.uc_gui_handle_captcha()
        sb.sleep(10)
        if dd2.is_element_present('button:contains("Accept")'):
            dd2.uc_click('button:contains("Accept")', reconnect_time=4)
        while sb.is_element_visible('#injected-channel-player'):
            sb.sleep(20)
        sb.quit_extra_driver()
sb.sleep(1)
