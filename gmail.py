import requests
import time
print( "         ")
print( "         ")
print( " \033[1;92m║══▒═✺═▒═✺═▒═══¤═¤═¤════════════¤═══║")
print( " \033[1;96m║✯ Creator ✯ AMIN MALAKE        ║")
print( " \033[1;98m║✯       𓆩 𝖆 𝖒 𝖎 𝖓 𓆪            ║")
print( " \033[1;96m║✯ instagram : i4m.amin         ║")                                          print( " \033[1;92m║══▒═✺═▒═✺═▒═══¤═¤═¤════════════¤═══║")
print( "          ")
print( "          ") 

print("[!] only Gmail yahoo hotmail ")
email = input("[=] Enter Email:")
def gmail():
 url = "https://mmo69.com/_check_live_email/api.php?email=" +email
 headers = {
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exc                   >
 "Accept-Encoding": "gzip, deflate, br",
 "Accept-Language": "ar",
 "Connection": "keep-alive",
 "Host": "mmo69.com",
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
 }
 data = {"email":email}
 rr = requests.get(url, headers=headers, data=data)
 if rr.text.find("LIVE") >= 0:
     print("[✅] Found in gmail:", email)
 else:
     print("[❌] Not Found in gmail:", email)
def instagram():
    url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip,deflate,br",
        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
        "content-length": "49",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/accounts/password/reset/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "x-csrftoken": "j4u26vxxC6D7eE63HhBde0ahZeN4mVfK",
        "x-ig-app-id": "936619743392459"
    }
    data = {"email_or_username":email, "recaptcha_challenge_field": ""}
    rr = requests.post(url, headers=headers, data=data)
    if rr.status_code == 200:
        print("[✅] Found in instagram:",email)
    else:
        print("[❌] Not Found in instagram:", email)
gmail()
instagram()
input("[x] Enter To exit")
exit()
