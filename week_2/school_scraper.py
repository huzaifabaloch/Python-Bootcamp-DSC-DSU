import requests
import json
import csv
import time


class SchoolScraper:
    def __init__(self):
        self.source = " https://directory.ntschools.net/api/System/GetAllSchools"
        self.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "X-Requested-With": "Fetch"
        }

        self.all_data = []


    def get_all_school_names(self):
        """
            To get all school codes from this endpoint and will use it
            to the endpoint of school informartion.
        """

        data = requests.get(self.source, headers=self.headers).json()
        
        # Here I used set, because some schools are being repeated.
        school_codes = set([school['itSchoolCode'] for school in data])

        # Total schools from this endpoint.
        print(len(school_codes))

        self.extract_schools_data(school_codes)



    def extract_schools_data(self, school_codes):

        # Creating endpoint link to fetch data
        
        for school in list(school_codes)[:50]:
            
            endpoint_link = f"https://directory.ntschools.net/api/System/GetSchool?itSchoolCode={school}"
            print('\n', endpoint_link)
            school_data = requests.get(endpoint_link, headers=self.headers).json()
            time.sleep(2)

            name = school_data.get('name')
            address = school_data.get('physicalAddress').get('displayAddress')
            principle_admin_name = school_data.get('schoolManagement')[0].get("firstName") + ' ' + \
                                    school_data.get('schoolManagement')[0].get("lastName")
            position = school_data.get('schoolManagement')[0].get("position")
            email = school_data.get('schoolManagement')[0].get("email")
            phone = school_data.get('schoolManagement')[0].get("phone")

            self.all_data.append([name, address, principle_admin_name, position, email, phone])

        self.save_school_data()


    def save_school_data(self):
        
        with open('all_school_data.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['name', 'addresss', 'principle_admin_name', 'position', 'email', 'phone'])
            writer.writerows(self.all_data)
        
        print('\n========================')
        print('SCHOOL DATA SAVED SUCCESS!')
        print('==========================')







scraper = SchoolScraper()
scraper.get_all_school_names()