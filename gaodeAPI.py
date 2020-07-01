import requests
import csv

def max_list(lt):
    temp = 0
    for i in lt:
        if lt.count(i) > temp:
            max_str = i
            temp = lt.count(i)
    return max_str


def use_poiID(id):
    url = 'https://restapi.amap.com/v3/place/detail'
    parameters = {'key': '146d87211350436db32901f5d9abaa97'}
    parameters.update({'id':id,'output':'json'})

    try:
        response = requests.get(url,params=parameters)
        data = response.json()
        poi = data['pois'][0]
        name = poi['name']
        location = poi['location']
        lng = str(location).split(',')[0]
        lat = str(location).split(',')[1]

    except:
        name = 0
        lng = 0
        lat = 0

    return name,lng,lat

def get_name_and_location(poi_keyword):
    url = "https://restapi.amap.com/v3/place/text"

    parameters = {'key':'146d87211350436db32901f5d9abaa97'}

    parameters.update({'keywords':poi_keyword,'city':'武汉','extensions':'all',
                  'types':'120300','citylimit':'true','children':'0'})

    try:
        response = requests.get(url,params=parameters)
        data = response.json()

        # parent_poi_list = []
        # poi_id_list = []
        # poi_name_list = []
        # poi_location_list = []

        if data['status']=='1':
            poi_id = data['pois'][0]['id']
            poi_name = data['pois'][0]['name']
            # poi_id_list.append(poi_id)
            # poi_name_list.append(poi_name)
            poi_location = data['pois'][0]['location']
            # poi_location_list.append(poi_location)

            #

                # poi_id = data['pois'][i]['id']
                # poi_name = data['pois'][i]['name']
                # poi_id_list.append(poi_id)
                # poi_name_list.append(poi_name)
                # poi_location = data['pois'][i]['location']
                # poi_location_list.append(poi_location)


            if data['pois'][0]['parent']!=[]:
                parent_poi = data['pois'][0]['parent']
                name, lng, lat = use_poiID(parent_poi)
                return name, lng, lat

            else:
                name = poi_name
                location = poi_location
                lng = location.split(',')[0]
                lat = location.split(',')[1]
                return name, lng, lat



                #parent_poi_list.append(data['pois'][i]['parent'])




            # if len(parent_poi_list) !=0:
            #     parent_poi = max_list(parent_poi_list)
            #     name, lng, lat = use_poiID(parent_poi)
            #     return name, lng, lat




    except:
        print("fail")
        print(poi_keyword)


        return poi_keyword,0,0

