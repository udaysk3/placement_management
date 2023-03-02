from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from home.models import User
import json
import os

from placements_management.settings import BASE_DIR
# Create your views here.

def login(req):
    return render(req, 'index.html')

def universitiesdb(req):
    if(req.method=='POST'):
        name = req.POST['name']
        email = req.POST['email']
        password = req.POST['password']
        if(User.objects.filter(email=email).exists() or req.POST['role'] == 'Recruiter'):
            if( User.objects.get(email=email).password == password):
                print('valid user')
                # print('User exists Already')
                filename = 'home/university_details.json'
                with open(filename, "r") as file:
                    data = json.load(file)
                return render(req,'universitiesdb.html',{
                    'data' : data,
                    'len' : len(data)
                })
            else:
                print('Invalid User')
                return render(req,'index.html',{'invalid':True})
        else:
            print('User doesnt exist')
            user = User(name=name, email = email, password = password)
            user.save()
            return render(req,'addcollege.html')
    
    print('entered get')
    filename = 'home/university_details.json'
    with open(filename, "r") as file:
            data = json.load(file)
    return render(req,'universitiesdb.html',{
        'data' : data,
        'len' : len(data)
    })

def addtojson(req):
    if(req.method=='POST'):
        print('enetred')
        college = req.POST['college']
        id = req.POST['id']
        region = req.POST['region']
        total = req.POST['total']
        placed = req.POST['placed']
        unplaced = req.POST['unplaced']
        

        filename = 'home/university_details.json'
        uni_data = {
            "college": college,
            "Id": id,
            "region": region,
            "unplaced": unplaced,
            "placed": placed,
            "total": total
        }

        # 1. Read file contents
        with open(filename, "r") as file:
            data = json.load(file)

        # 2. Update json object
        data.append(uni_data)

        # 3. Write json file
        with open(filename, "w") as file:
            json.dump(data, file)
        print(data)
        print(type(data))
        return render(req,'universitiesdb.html',{
            'data' : data,
            'len' : len(data)
        })
    

def collegedetails(req):
    return render(req,'collegedetails.html')

