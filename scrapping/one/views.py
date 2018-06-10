from django.shortcuts import render
from selenium import webdriver
from one.models import Restaurant
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def load_zomato_data_to_database(request):

    #data once loaded then no need to load same data again
    if Restaurant.objects.all():

        return HttpResponse("Data Already loaded no need to load same data again database")


    else:

        browser = webdriver.Chrome(executable_path='C:/Users/User/Downloads/chromedriver_win32/chromedriver')
        browser.get(" https://www.zomato.com/bangalore/restaurants")
        restaurant_name_link=browser.find_elements_by_xpath("//a[@class='result-title hover_feedback zred bold ln24   fontsize0 ']")
        restaurant_loaction=browser.find_elements_by_xpath("//div[@class][@title][@style]")
        restaurant_rating=browser.find_elements_by_xpath("//div[@class][@data-res-id][@data-variation][@data-content]")

        for i,j,k in zip(restaurant_name_link,restaurant_loaction,restaurant_rating):
            #saving data to data base
            r=Restaurant(restaurant_name=i.text,restaurant_url=i.get_attribute('href'),restaurant_location=j.text,restaurant_rating=k.text)
            r.save()
        while(True):
            try:
                browser.find_element_by_xpath("//a[@class='paginator_item   next item']").click()

            except:

                break

            restaurant_name_link=browser.find_elements_by_xpath("//a[@class='result-title hover_feedback zred bold ln24   fontsize0 ']")
            restaurant_loaction=browser.find_elements_by_xpath("//div[@class][@title][@style]")
            restaurant_rating=browser.find_elements_by_xpath("//div[@class][@data-res-id][@data-variation][@data-content]")

            for i,j,k in zip(restaurant_name_link,restaurant_loaction,restaurant_rating):

                r=Restaurant(restaurant_name=i.text,restaurant_url=i.get_attribute('href'),restaurant_location=j.text,restaurant_rating=k.text)
                r.save()

        browser.quit()

        return render(request,'data1.html')





#view to view results on map

def maps(request):
    all=Restaurant.objects.all()
    dict={'object':all}

    return render(request,'maps1.html',dict)
