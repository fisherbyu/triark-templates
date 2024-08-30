from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

TRIARK = [{"title": "Billing - Initial Invoice Due (Inspection Report)", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> We would like to share your Inspection Report Invoice with you. We accept the following payment methods: <ul> <li>All major credit/debit cards</li> <li>ACH/e-check</li> <li>Checks payable to Triark Roofing</li> </ul> If you have any questions or concerns, please reply to this email immediately and we'll be glad to help. <br> <br> Warmly, </p> </span>"},{"title": "Billing - Initial Invoice Due (Roof Install)", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Your Roof Install has been completed. We would like to share your Roof Install Invoice with you. We accept the following payment methods: <ul> <li>All major credit/debit cards</li> <li>ACH/e-check</li> <li>Checks payable to Triark Roofing</li> </ul> If you have any questions or concerns, please reply to this email immediately and we'll be glad to help. <br> <br> Warmly, </p> </span>"},{"title": "Billing - Initial Invoice Due (Roof Repairs)", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Your Roof Repairs have been completed. We would like to share your Roof Repair Invoice with you. We accept the following payment methods: <ul> <li>All major credit/debit cards</li> <li>ACH/e-check</li> <li>Checks payable to Triark Roofing</li> </ul> If you have any questions or concerns, please reply to this email immediately and we'll be glad to help. <br> <br> Warmly, </p> </span>"},{"title": "Billing - Invoice Balance Open", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> We show you still have an open balance on your invoice. Please make a payment on this balance as soon as possible to avoid any late fees. We accept the following payment methods: <ul> <li>All major credit/debit cards</li> <li>ACH/e-check</li> <li>Checks payable to Triark Roofing</li> </ul> If you have any questions or concerns, please reply to this email immediately and we'll be glad to help. <br> <br> Warmly, </p> </span>"},{"title": "Billing - Paid Receipt", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Thank you for choosing Triark Roofing. Your sales receipt is attached. <br> We appreciate the opportunity to serve you. If you have any questions or feedback regarding your project, please let us know. <br> <br> Thank You, </p> </span>"},{"title": "Billing - Warranty Information", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> We've attached your warranty information. Please contact us with any questions you have. <br> <br> Warmly, </p> </span>"},{"title": "Production - Installation Notification", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Your Installation Date is {{WorkOrderDateStart}}. <br><br> To prepare for your roofing project please be aware of the following: <br><br> Attic Access: We will need to enter your attic to ensure your ventilation is securely reattached after installation. <br><br> Inclement Weather Delays: Rain, hail, and excessive heat may force delays in our production schedule. We need the appropriate amount of time to ensure that the roof is properly installed. <br><br> Material Delivery: Please clear ALL vehicles from the driveway for delivery. The delivery trucks usually need to use the driveway to properly unload the material. If possible, they will unload the materials on the roof. Please let us know if you have any questions regarding this process. <br><br> Outdoor Furniture & Landscape: Please distance all items around the house (e.g. patio and pool furniture, potted plants, gardening equipment, and grills) into a SAFE AREA so that they won't be damaged by falling debris. <br><br> Wall and Shelved Items: Construction work can create vibrations which may cause loose items to fall or slide off of shelves and walls (e.g. mirrors, pictures, figurines, or plates). We recommend stowing valuable items in a safe place during construction. <br><br> Site Clean-Up: After the work is complete, we will clean-up the area as best as possible, but a few nails may remain that are hidden in the grass or shrubbery. <br><br> Noise: The process of installing a roof is quite noisy. Pets and family members who are sensitive to loud noises may want to be somewhere else during the installation. <br><br> Should you have any questions, please feel free to contact us. <br> <br> Warmly, </p> </span>"},{"title": "Production - Project Complete", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Good news! Your roof project has officially been completed. Thank you for letting us work with you on this milestone for your home and family. <br> If we are still working with you on other projects, please look for our future communication. <br> Our office is available to assist you with any pending invoices. Please reach out for help with your preferred payment method. <br> It has been a pleasure working with you and we truly appreciate the opportunity to elevate your home. <br> <br> Warmly, </p> </span>"},{"title": "Production - Project Complete - Final Inspection", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Thank you for choosing Triark Roofing. We want to check-in to makes sure you are happy with the results? <br> We will be coming back by to do a final inspection to make sure everything looks good. If you have any concerns at all, he will be happy to review them with you. <br> If there are any issues or concerns, please let us know so we can get everything done to your satisfaction. <br> <br> Warmly, </p> </span>"},{"title": "Production - Reschedule Appointment Due To Weather", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Due to inclement weather, we will need to reschedule your appointment. Please give us a call back at (916) 276-8632, so we can set up a new day and time. <br> <br> Warmly, </p> </span>"},{"title": "Production - Roof Install Information", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Thank you for choosing {{LocationName}}! Your roof will be installed within 1-2 weeks (weather permitting). Unfortunately, due to weather, unforeseen delays, and circumstances beyond our control, it's very hard to provide a firm install date until 1-2 days beforehand, but we will do our best to give you a heads up so you can plan for our crews arrive. <br><br> We look forward to serving you. <br> <br> Warmly, </p> </span>"},{"title": "Sales - Estimate", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Thank you for considering Triark Roofing. <br> I've attached your estimate for your project. <br> Please reply to this email or call us if you have any questions. <br> <br> Warmly, </p> </span>"},{"title": "Sales - Thanks For Contacting Us", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Thank you for contacting Triark Roofing for your roofing needs. We look forward to working on your home. <br> When you work with us, our whole team is at you service. Our mission is to provide with service that exceeds your expectations. If at any time you're unsatisfied with one of our employees or services, please let us know and we'll make it right. <br> You can reach our office at (916) 276-8632. <br> <br> Warmly, </p> </span>"}]
t = 0
JAY = [{"title": "FollowUp Roof Install Estimate (Client)", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> We hope you're having a great day! <br> We're following up to see if you have any questions regarding the bids we sent over. You can access it by clicking the link below. <br> Please feel free to reach out if you have any questions or concerns. We look forward to hearing from you! <br> <br> Warmly, </p> </span>"},{"title": "FollowUp Roof Repair Estimate (Client)", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> We hope you're having a great day! <br> We're following up to see if you have any questions regarding the bids we sent over. You can access it by clicking the link below. <br> Please feel free to reach out if you have any questions or concerns. We look forward to hearing from you! <br> <br> Warmly, </p> </span>"},{"title": "Billing - Thanks + Ask for Review (Homeowner)", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> We have enjoyed working with you in the past and are so grateful for the opportunity to have been able to work on your home. Triark is currently working on expanding our online presence and would greatly appreciate a review on your experience with us. Thank you so much for trusting us with your home and please consider leaving a review. <br> <br> Here is our Google Reviews link: https://g.page/r/CYwEgufezA6cEBI/review <br> <br> Warmly, </p> </span>"},{"title": "Billing - Thanks + Ask for Review(Realtor) ", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> We have enjoyed working with you in the past and are so grateful for the opportunity to have been able to assist your clients. Triark is currently working on expanding our online presence and would greatly appreciate a review on your experience with us. Thank you so much for trusting us to help with your business and please consider leaving a review. <br> <br> Here is our Google Reviews link: https://g.page/r/CYwEgufezA6cEBI/review <br> <br> Warmly, </p> </span>"},{"title": "FollowUp Roof Repair Estimate (Realtor)", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> I hope you're having a great day! <br> I'm following up to see if you have any questions regarding the bids we sent over. You can access it by clicking the link below. <br> Please feel free to reach out if you have any questions or concerns. I look forward to hearing from you! <br> <br> Warmly, </p> </span>"},{"title": "Inspection Report Finished", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Thanks for using our services! <br> I've just completed your Roof Inspection Report. Attached is a summary of inspection findings and a quote for recommended repairs. <br> <br> Warmly, </p> </span>"},{"title": "Estimate Finished", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Thanks for using our services! <br> I've just completed your Roof Work Estimate, which is attatched below. Please reach out if you have any questions <br> <br> Warmly, </p> </span>"},{"title": "Jay Template", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Email Content <br> <br> Warmly, </p> </span>"}]
j = 1
BARBARA = [{"title": "Inspection Appt Reminder", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Good Morning! We wanted to remind you of your Roof Inspection today at: {{TaskTimeStart}} <br> <br> Warmly, </p> </span>"},{"title": "Inspection Re-Scheduled", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Your Inspection has been re-scheduled, your new Inspection is on: {{TaskDateStart}} at: {{TaskTimeStart}} <br> <br> Warmly, </p> </span>"},{"title": "Inspection Scheduled", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Thanks so much for scheduling an inspection! You are in our schedule on: {{TaskDateStart}} at: {{TaskTimeStart}} <br> <br> Warmly, </p> </span>"},{"title": "Barbara Template", "content": " <p> Hi {{JobPrimaryContactFirstName}}, <br> <br> Email Content <br> <br> Warmly, </p> </span>"}]
b = 2
def SaveBlock(title, content, empID, type) :
    block = CodeBlock()
    block.title = title
    block.content = content
    emp = Employee.objects.get(empID = empID)
    type = ContentType.objects.get(title = type)
    block.empID = emp
    block.type = type

    block.save()



def ProcessData(list, number) :
    for data in list :
        title = data["title"]
        content = "<span> " + data["content"]
        empID = number
        type = "email content"
        SaveBlock(title, content, empID, type)

# ProcessData(TRIARK, t)
# ProcessData(JAY, j)
# ProcessData(BARBARA, b)


def indexPageView(request) :
    Employees = Employee.objects.all()
    content = {
        'emps' : Employees
    }
    return render(request, 'code_crunch/index.html', content)

def displayEmailPageView(request, empID) :
    emp = Employee.objects.get(empID = empID)
    head = (HeaderBlock.objects.get(title = 'head')).content
    footer = (HeaderBlock.objects.get(title = 'footer')).content
    sign = (CodeBlock.objects.get(empID = empID, type = 'signature')).content
    emails = CodeBlock.objects.all().filter(empID = empID, type = 'email content')
    
    content = {
        'emp' : emp,
        'blocks' : emails,
        'header' : head,
        'signature' : sign,
        'footer' : footer
    }
    
    return render(request, 'code_crunch/display.html', content)

def DisplayAllPageView(request) :
    blocks = CodeBlock.objects.all().filter(type = 'email content').order_by('title')
    head = (HeaderBlock.objects.get(title = 'head')).content
    footer = (HeaderBlock.objects.get(title = 'footer')).content
    
    emails = []
    for email in blocks :
        title = email.title
        emailContent = email.content
        ID = email.empID
        sign = (CodeBlock.objects.get(empID = ID, type = 'signature')).content
        code = head + emailContent + sign + footer
        output = {
            'title': title,
            'content': code
        }
        emails.append(output)
        
    content = {
        'emails': emails
    }
        
    return render(request, 'code_crunch/displayAll.html', content)

# def RenderEmail(request) :
#     if request.method == 'POST':
#         htmlContent = request.POST['html']
#         return render(request, htmlContent)
#     else:
#         return HttpResponseRedirect(reverse('displayAll'))
 