
with open(r"report1.html", 'r', encoding="utf8") as fp:
    try:
        file = fp.read()
        # print(file)

        i = file.index("~Intello LogIn page Opened")
        j = file.index("<br/></div></td></tr></tbody></table></body></html>")
        print([file[i:j]])
        x = file[i:j].split("\n")
        print(x)
        # print(x.pop(-1))
        x.pop(-1)
        print(x)

        sl_no = 1
        html1 = ""
        for item in x:
            # desc = item.split("~")[1].replace(": Success", "")
            desc = item.split("~")[1].split(":")[0]
            status = item.split("~")[1].rsplit(":")[1]
            # status = item.split("~")[1].rsplit(":")[1].replace("\n", "")
            print(desc)
            if status == " Success":
                html1 = html1 + f'''
                <tr>
                  <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">XT-CX-{'{0:03}'.format(sl_no)}</td>
                  <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{desc}</td>
                  <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{status}</td>
                </tr>
                '''
            else:
                html1 = html1 + f'''
                <tr>
                  <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">XT-CX-{'{0:03}'.format(sl_no)}</td>
                  <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{desc}</td>
                  <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;color: red;font-weight: bold;">{status}</td>
                </tr>
                '''
            sl_no += 1
    finally:
        fp.close()
    # print(html1)
#
# with open(r"report.html", 'r', encoding="utf8") as fp:
#     try:
#         file = fp.read()
#         # print(file)
#
#         i = file.index("~LogIn page displayed")
#         j = file.index("End Aes")
#         print([file[i:j]])
#         x = file[i:j].split("\n")
#         print(x)
#         # print(x.pop(-1))
#         x.pop(-1)
#         print(x)
#
#         sl_no = 1
#         html4 = ""
#         for item in x:
#             # desc = item.split("~")[1].replace(": Success", "")
#             desc = item.split("~")[1].split(":")[0]
#             status = item.split("~")[1].rsplit(":")[1]
#             # status = item.split("~")[1].rsplit(":")[1].replace("\n", "")
#             print(desc)
#             if status == " Success":
#                 html4 = html4 + f'''
#                 <tr>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">XT-Aes-{'{0:03}'.format(sl_no)}</td>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{desc}</td>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{status}</td>
#                 </tr>
#                 '''
#             else:
#                 html4 = html4 + f'''
#                 <tr>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">XT-Aes-{'{0:03}'.format(sl_no)}</td>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{desc}</td>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;color: red;font-weight: bold;">{status}</td>
#                 </tr>
#                 '''
#             sl_no += 1
#     finally:
#         fp.close()
    # print(html1)

# with open(r"report1.html", 'r', encoding="utf8") as fp:
#     try:
#         file = fp.read()
#         i = file.index("~Agent (Email) LogIn")
#         j = file.index("End email ignore")
#         print([file[i:j]])
#         list1 = file[i:j].split("\n")
#         # print(list1)
#         list1.pop()
#         print(list1)
#         num = 1
#         html2 = ""
#         for item in list1:
#             # z = z + "\n" + "\n" + str(num) + ")    " + item.split("~")[1].replace("\n", "")
#             desc1 = item.split("~")[1].split(":")[0]
#             # status1 = item.split("~")[1].rsplit(":")[1].replace("\n", "")
#             status1 = item.split("~")[1].rsplit(":")[1]
#             print(status1)
#
#             if status1 == " Success":
#                 html2 = html2 + f'''
#                 <tr>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">XE-{'{0:03}'.format(num)}</td>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{desc1}</td>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{status1}</td>
#                 </tr>
#                 '''
#             else:
#                 html2 = html2 + f'''
#                    <tr>
#                      <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">XE-{'{0:03}'.format(num)}</td>
#                      <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{desc1}</td>
#                      <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;color: red;font-weight: bold;">{status1}</td>
#                    </tr>
#                    '''
#             num += 1
#     finally:
#         fp.close()

# with open(r"report1.html", 'r', encoding="utf8") as fp1:
#     try:
#         file = fp1.read()
#         i = file.index("~Agent (Chat) LogIn")
#         j = file.index("End chat ignore")
#         print([file[i:j]])
#         list2 = file[i:j].split("\n")
#         # print(list2)
#         list2.pop()
#         print(list2)
#         num = 1
#         html3 = ""
#         for item in list2:
#             # z = z + "\n" + "\n" + str(num) + ")    " + item.split("~")[1].replace("\n", "")
#             desc2 = item.split("~")[1].split(":")[0]
#             # status2 = item.split("~")[1].rsplit(":")[1].replace("\n", "")
#             status2 = item.split("~")[1].rsplit(":")[1]
#             print(status2)
#
#             if status2 == " Success":
#                 html3 = html3 + f'''
#                 <tr>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">XC-{'{0:03}'.format(num)}</td>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{desc2}</td>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{status2}</td>
#                 </tr>
#                 '''
#             else:
#                 html3 = html3 + f'''
#                 <tr>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">XC-{'{0:03}'.format(num)}</td>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;">{desc2}</td>
#                   <td style="border: 1px solid black;border-collapse: collapse;padding: 10px;color: red;font-weight: bold;">{status2}</td>
#                 </tr>
#                 '''
#             num += 1
#     finally:
#         fp1.close()

html = f'''\
<!DOCTYPE html>
<html>
   <head>

   </head>
   <body>

     <p> Dear Sir,<br>
     please find below automation test report for channel “call” performed on qa server (URL - https://qaradius.in.qamajor.radius-ois.ai/intello/login/).</p>
     <p> </p>
      <table style="border: 1px solid black;border-collapse: collapse;width: 95%">
         <tr>
            <th style="border: 1px solid black;border-collapse: collapse;padding: 10px;">SL No</th>
            <th style="border: 1px solid black;border-collapse: collapse;padding: 10px;">TestCase Description</th>
            <th style="border: 1px solid black;border-collapse: collapse;padding: 10px;">Status</th>
         </tr>
         <tr>
            <th style="border: 1px solid black;border-collapse: collapse;padding: 10px;" colspan="3">TELEPHONY(CrossX)</th>
         </tr>
         {html1}
         
         
      </table>

   </body>
</html>
'''
print(html)

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# sender_email = "demo_radius@visnet.in"
sender_email = "testing_radius@visnet.in"
receiver_email = ["suchismita.lenka@visnet.in"]
# receiver_email = ["suman@radius-ois.ai","biswajit.biswal@visnet.in","shreekant.nayak@visnet.in"]
cc_email = ["suchismita.lenka@visnet.in"]
# receiver_email = ["shreekant.nayak@visnet.in"]
# receiver_email = ["suman.subudhi@visnet.in", "sourya.dhal@visnet.in", "alok.kumar@visnet.in", "shreekant.nayak@visnet.in", "hitebrata.bhainsa@visnet.in", "suchilita.swain@visnet.in", "suvijoy.das@visnet.in", "taratarini.patnaik@visnet.in", "rashmirekha.sahu@visnet.in", "payal.mohanty@visnet.in"]
# password = "D#m0rad!us@123"
password = "yggvxsssbhjfcxwq"
# password = "R@dT#st!ng@123"

rfb_date = datetime.datetime.now().date().strftime("%d/%m/%Y")
print(rfb_date)

message = MIMEMultipart("alternative")
message["Subject"] = f"RADIUS QA automation test for Intello - {rfb_date}"
message["From"] = sender_email
message["To"] = ",".join(receiver_email)
message["Cc"] = ",".join(cc_email)
# message["Bcc"] = receiver_email  # Recommended for mass emails


# Turn these into plain/html MIMEText objects
# part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
# message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email + cc_email, message.as_string()
    )
