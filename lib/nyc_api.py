
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://makeup-api.herokuapp.com/api/v1/products.json"

    response = requests.get(URL)
    return response.content
  
  def program_school(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
    product_list = []
    products = json.loads(self.get_programs())
    for product in products:
            product_list.append(product["product_type"])

    return product_list

# programs = GetPrograms().get_programs()
# print(programs)
programs = GetPrograms()
programs_schools = programs.program_school()

for product in set(programs_schools):
    print(product)
