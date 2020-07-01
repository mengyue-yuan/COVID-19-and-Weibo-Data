import csv
import json


# 小区名称改正dic
title_dic = {}
with open('/Users/yuanmengyue/Desktop/title_dic.csv',encoding='gbk') as dicfile:
    reader = csv.reader(dicfile)
    for row in reader:
        title_dic[row[0]] = row[1]




poi_path = "/Users/yuanmengyue/Desktop/COVID-19_Data/高德地图API POI分类编码表.csv"
poi_dic3 = {'景点':'风景名胜','西餐厅':'外国餐厅','四川菜':'中餐厅','广东菜':'中餐厅','山东菜':'中餐厅','湖南菜':'中餐厅','安徽菜':'中餐厅','湖北菜':'中餐厅','牛扒店':'外国餐厅'}  # 三级POI对应的二级POI
poi_dic2 = {'商圈':'购物服务','熟食':'餐饮服务','烧烤':'餐饮服务','推荐景点':'风景名胜','校园生活':'科教文化服务','医院':'医疗保健服务','火车站中心点':'交通设施服务','飞机场中心点':'交通设施服务','高校':'科教文化服务',
            '生活娱乐':'体育休闲服务','餐饮美食':'餐饮服务','泰国／越南菜品餐厅':'餐饮服务','其他亚洲菜':'餐饮服务','美食':'餐饮服务','特色／地方风味餐厅':'餐饮服务','自助':'餐饮服务','夜店':'体育休闲服务'}  # 二级POI对应的一级POI
poi_list1 = [] # 一级POI列表




with open(poi_path) as csvfile1:
    reader = csv.reader(csvfile1)
    for row in reader:
        first_poi = row[2]
        third_poi = row[4]
        second_poi = row[3]
        poi_dic3[third_poi] = second_poi

        if first_poi not in poi_list1:
            poi_list1.append(first_poi)

        if second_poi not in poi_dic2.keys():
            poi_dic2[second_poi] = first_poi


# 写入每一小区/街区用户在外签到数据的csv
street_data_number = {}
def get_street_user_data(street_name):

    file_path = "/Users/yuanmengyue/Desktop/街区-用户.json"
    csv_write_path = '/Users/yuanmengyue/Desktop/Select_Street2/' + street_name + '.csv'

    count = 0
    no_count = 0

    with open(file_path) as jsonfile1:
        for line in jsonfile1.readlines():
            rline = json.loads(line)
            guanshan_list = rline[street_name]
            # 遍历每个住户
            for i in range(0, len(guanshan_list)):
                user_id = guanshan_list[i]
                user_data_path = "/Users/yuanmengyue/Desktop/武汉市12月1月数据按用户分类/" + user_id + '/' + user_id + '.json'
                user_location_path = "/Users/yuanmengyue/Desktop/武汉市一年数据按用户分类/" + user_id + '/' + 'living_place_校正后.json'

                f1 = open(user_location_path)
                living_data = f1.readline()
                line_data = json.loads(living_data)
                living_place = line_data['所在小区']
                location = line_data['经纬度']
                f1.close()

                with open(user_data_path) as jsonfile2:
                    # 遍历该用户的所有签到数据
                    for l in jsonfile2.readlines():
                        line_data = json.loads(l)
                        count += 1

                        annotations = 0
                        place = 0
                        place_title = 0
                        object = 0
                        address = 0
                        district = 0
                        cityBlock = 0
                        fax = 0
                        poi_type = 0

                        try:
                            created_at = line_data['created_at']
                            lat = line_data['geo']['coordinates'][0]
                            lon = line_data['geo']['coordinates'][1]
                            annotations = line_data["annotations"]
                            place = annotations[0]["place"]
                            place_title = place["title"]

                            object = line_data["url_objects"][0]["object"]["object"]
                            address = object["address"]
                            district = address['district']
                            cityBlock = address['cityBlock']
                            fax = address["fax"]

                            if fax in poi_list1:
                                poi_type = fax

                            elif fax in poi_dic2.keys():
                                poi_type = poi_dic2[fax]

                            elif fax in poi_dic3.keys():
                                poi_type = poi_dic3[fax]
                                poi_type = poi_dic2[poi_type]

                            else:
                                poi_type = fax


                            if place_title in title_dic.keys():
                                place_title = title_dic[place_title]


                            if place_title == living_place:
                                # print(living_place,'',place_title)
                                count -= 1
                                continue


                        except:
                            no_count += 1

                        with open(csv_write_path, 'a', encoding='gbk', errors='ignore') as write_file:
                            writer = csv.DictWriter(write_file,
                                                    ['USER_ID', 'TIME', 'Living_Lon', 'Living_Lat', 'Living_Place',
                                                     'Place_Title','Lon','Lat','District','CityBlock','Fax','POI_type'])

                            data = {}
                            data['USER_ID'] = user_id
                            data['TIME'] = created_at
                            data['Living_Lon'] = location[0]
                            data['Living_Lat'] = location[1]
                            data['Living_Place'] = living_place
                            data['Place_Title'] = place_title
                            data['Lon'] = lon
                            data['Lat'] = lat
                            data['District'] = district
                            data['CityBlock'] = cityBlock
                            data['Fax'] = fax
                            data['POI_type'] = poi_type
                            writer.writerow(data)
                            #print(data)
                            #print("写入成功")


    print(street_name)
    print(count)

    return count





Street_dic = {"中南路街道":'中南路街区',
              "珞南街道":'珞南街区',
              "洪山街道":'洪山街区',
              "南湖街道":'南湖街区',
              "粮道街街道":'粮道街街区',
              "杨园街道":'杨园街区',
              "徐家棚街道":'徐家棚街区',
              "首义路街道":'首义路街区',
              "中华路街道":'中华路街区',
              "积玉桥街道":'积玉桥街区',
              "黄鹤楼街道":'黄鹤楼街区',
              "白沙洲街道":'白沙洲街区',
              "紫阳街道":'紫阳街区',
              "九峰乡":'九峰乡',
              "青菱乡":'青菱乡',
              #"天兴乡":'天兴乡',
              "张家湾街道":'张家湾街区',
              "花山镇":'花山镇',
              #"红旗街道":'梨园街区',
              "狮子山街道":'狮子山街区',
              "东湖生态旅游风景区":'东湖风景区街区',
              "豹澥镇":'豹澥街区',
              "新沟桥街道":'新沟桥街区',
              "钢花村街道":'钢花村街区',
              "青山镇街道":'青山镇街区',
              "白玉山街道":'白玉山街区',
              "冶金街道":'冶金街区',
              "武东街道":'武东街区',
              "工人村街道":'工人村街区',
              "红卫路街道":'红卫路街区',
              "红钢城街道":'红钢城街区',
              "武汉钢铁集团公司":'',
              "水果湖街道":'水果湖街区',
              "珞珈山街道":'珞珈山街区',
              "关山街道":'关山街区',
              "建设乡":'建设乡',
              "和平街道":'和平街区',
              "厂前街道":'厂前街区',
              "纸坊街道":'纸坊街区',
              "五里界街道":'五里界街区',
              "流芳街道":'流芳街区'
}







for key,value in Street_dic.items():
    street_name = value


    try:
        data_number = get_street_user_data(street_name)

    except:
        print(key,'失败')





# with open("/Users/yuanmengyue/Desktop/街区-用户.json") as datafile:
#     for line in datafile.readlines():
#         rline = json.loads(line)
#
#         for key in rline.keys():
#             street_name = key
#             data_number = get_street_user_data(street_name)
#             street_data_number[street_name] = data_number













