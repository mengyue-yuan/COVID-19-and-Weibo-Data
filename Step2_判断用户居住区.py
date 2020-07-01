import os
import json
import csv
from gaodeAPI import get_name_and_location



count = 0

#建立一个矫正前后小区名的映射
title_dic = {}

# 建立一个矫正后小区名与经纬度的映射
location_dic = {}


data_path = "/Users/yuanmengyue/Desktop/武汉市一年数据按用户分类"

for root,dir,file in os.walk(data_path):
    for filename in file:
        if filename != ".DS_Store":
            file_path = os.path.join(root,filename)
            user_id = filename.split('.')[0]
            # 对该用户在各个小区内的签到次数进行统计
            living_place_dic = {}
            living_district_dic = {}
            living_cityBlock_dic = {}

            with open(file_path) as jsonfile:
                for line in jsonfile.readlines():
                    rline = json.loads(line)
                    try:

                        annotations = rline["annotations"]
                        place = annotations[0]["place"]
                        place_title = place["title"]

                        object = rline["url_objects"][0]["object"]["object"]
                        address = object["address"]
                        district = address['district']
                        cityBlock = address['cityBlock']
                        fax = address["fax"]
                        if fax =="住宅区":

                            if place_title not in title_dic.keys():

                                place_name, lng, lat = get_name_and_location(place_title)

                                print("调用API:",place_title,' -> ',place_name)
                                location_dic[place_name] = [lng, lat]
                                title_dic[place_title] = place_name

                                # with open('/Users/yuanmengyue/Desktop/title_dic.csv', 'a', encoding='gbk',
                                #           errors='ignore') as csvfile:
                                #     writer = csv.DictWriter(csvfile,
                                #                             ['Title', 'Name'])
                                #
                                #     data = {}
                                #     data['Title'] = place_title
                                #     data['Name'] = place_name
                                #     writer.writerow(data)
                                #     print("写入成功！")



                            else:
                                place_name = title_dic[place_title]
                                lng = location_dic[place_name][0]
                                lat = location_dic[place_name][1]

                            #print(place_title,place_name,' ',lng,' ',lat)
                            if place_name not in living_place_dic.keys():
                                living_place_dic[place_name] = 1
                            else:
                                living_place_dic[place_name] += 1

                            if district not in living_district_dic.keys():
                                living_district_dic[district] = 1
                            else:
                                living_district_dic[district] += 1

                            if cityBlock not in living_cityBlock_dic.keys():
                                living_cityBlock_dic[cityBlock] = 1
                            else:
                                living_cityBlock_dic[cityBlock] += 1


                    except:
                        continue

            #
            # # 返回签到次数最多的小区
            # if living_place_dic != {}:
            #     living_place_list = []
            #     for key, value in living_place_dic.items():
            #         if value == max(living_place_dic.values()):
            #             max_key = key
            #             living_place_list.append(max_key)
            #
            #     # 这一步是为了排除，在两个小区签到次数一样多的情况
            #     if len(living_place_list)==1:
            #         living_place = living_place_list[0]
            #
            #
            #
            #         location = location_dic[living_place]
            #
            #     # 顺便获取该用户所在的街区，和行政区
            #     cityBlock_list = []
            #     for k_,v_ in living_cityBlock_dic.items():
            #         if v_ ==max(living_cityBlock_dic.values()):
            #             max_k_ = k_
            #             cityBlock_list.append(max_k_)
            #     if len(cityBlock_list)==1:
            #         living_cityBlock = cityBlock_list[0]
            #
            #
            #     district_list = []
            #
            #     for k,v in living_district_dic.items():
            #         if v == max(living_district_dic.values()):
            #             max_k = k
            #             district_list.append(max_k)
            #     if len(district_list)==1:
            #         living_district = district_list[0]
            #
            #     try:
            #         write_dic = {'所在小区':living_place,'经纬度':location,'街区':living_cityBlock,'行政区':living_district }
            #         # write_path = os.path.join(root,"living_place_校正后.json")
            #         # f1 = open(write_path, mode='w')
            #         # a = json.dumps(write_dic)
            #         # b = str(a) + "\n"
            #         # f1.write(b)
            #         # print(write_dic)
            #         # print("写入成功")
            #
            #
            #     except:
            #         continue
            #








