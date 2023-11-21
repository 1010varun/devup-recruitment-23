from .models import *
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
import json

class recruitmentFormData(APIView):

    def post(self, request):
        data = request.data

        name = data["name"]
        personal_email = data["personal_email"]
        kiet_email = data["kiet_email"]
        phone = data["phone"]
        domain = data["domain"]
        mode_of_payment = data["mode_of_payment"]
        library_id = data["library_id"]
        desk = data["desk"]
        gender = data["gender"]

        student = recruitment.objects.filter(library_id = library_id)

        print("after")

        if(len(student)):
            response = "student already exists!!"
            status = 400

        else:
            new_student = recruitment(name = name, 
                                        personal_email = personal_email, 
                                        kiet_email = kiet_email, 
                                        phone = phone, 
                                        domain = domain, 
                                        mode_of_payment = mode_of_payment, 
                                        library_id = library_id, 
                                        desk = desk, 
                                        gender = gender
                                    )
            new_student.save()

            response = "student data submitted successfully!!"
            status = 200

        return HttpResponse(response, status=status)



class sample(APIView):

    def get(self, request):
        return HttpResponse("sample request")

