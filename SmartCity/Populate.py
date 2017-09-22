import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'SmartCity.settings')

import django
django.setup()

from CityApp.models import CityInfo, UserProfile

def populate():
    add_landmark('Grilld', 'restuarant', 'General', 'General', '0456283567', '1', '27 Albert st', 'Brisbane', 'Queensland', '4000', 'Grilld@grill.com')
    add_landmark('State Library', 'Library', 'Student', 'Student', '04247152', '1', 'Stanley PL', 'South Brisbane', 'Queensland', '4101', 'StateLib@Library.com')
    add_landmark('Lone Pine', 'Zoo', 'General', 'General', '04521487', '1', '12 Lone Pine Rd', 'Logan', 'Queensland', '4201', 'LonePine@zoo.com')
    add_landmark('Factory Direct', 'Industry', 'Business', 'Business', '045412398', '1', '13 Busy Road', 'Browns Plains', 'Queensland', '4120', 'FacDirect@manufacturing.com')
    add_landmark('Mantra','Hotel', 'Student', 'Student', '04181995', '1', '9 Hussle ct', 'Brisbane', 'Queensland', '4000', 'MantraBrisbane@mantra.com')



def add_landmark(name, landmark_type, user_type, industry_type, phone_number, unit_number,
    street_number, suburb, state, postcode, email):
    cI = CityInfo.objects.get_or_create(name=name, landmark_type=landmark_type, user_type=user_type,
        industry_type=industry_type, phone_number=phone_number, unit_number=unit_number,
        street_number=street_number, suburb=suburb, state=state, postcode=postcode,
        email=email)[0]
    cI.save()

if __name__ == '__main__':
    print("Starting CityApp population script...")
    populate()
