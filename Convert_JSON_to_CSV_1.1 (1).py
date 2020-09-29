import json, os
import csv

json_folder = os.getcwd()
json_list = [myJson for myJson in os.listdir(json_folder) if myJson.endswith('.json')]

for i in range(len(json_list)):
   print("i = ", i)
   filename = os.path.splitext(json_list[i])[0]
   print("filename = ", filename)

   img_data_in = open('%s.json' % filename, 'r')

   img_data_out = open('%s.csv' % filename, 'w')

   writer = csv.writer(img_data_out)

   count = 0
   for img in json.loads(img_data_in.read()):
       if count == 0:
           header = img.keys()
           writer.writerow(header)
           count += 1
       writer.writerow(img.values())
       count += 1















