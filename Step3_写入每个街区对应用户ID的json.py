import os
import json


data_path = "/Users/yuanmengyue/Desktop/武汉市12月1月数据按用户分类"
source_path = "/Users/yuanmengyue/Desktop/武汉市一年数据按用户分类"


living_place_dic = {}
cityBlock_list_dic = {}

count = 0

for root,dir,file in os.walk(data_path):
    for filename in file:
        filepath = os.path.join(root,filename)
        user_id = filename.split('.')[0]
        location_path = source_path + '/'+ user_id+'/'+'living_place_校正后.json'
        if os.path.exists(location_path):

            count +=1
            print(count)

            with open(location_path) as jsonfile1:
                for line in jsonfile1.readlines():
                    rline = json.loads(line)
                    living_place = rline["所在小区"]
                    #cityBlock = rline['街区']
                    #district = rline['行政区']

                    # if living_place not in living_place_dic.keys():
                    #     living_place_dic[living_place] = 1
                    # else:
                    #     living_place_dic[living_place] += 1

                    if living_place not in cityBlock_list_dic.keys():
                        cityBlock_list_dic[living_place] = []
                        cityBlock_list_dic[living_place].append(user_id)
                    else:
                        cityBlock_list_dic[living_place].append(user_id)






# living_place_dic_s = sorted(living_place_dic.items(), key=lambda item:item[1],reverse=True)
#
# cityBlock_list_dic_s = sorted(cityBlock_list_dic.items(), key=lambda item:item[1],reverse=True)
#
# print(living_place_dic_s)
#
# print(cityBlock_list_dic_s)


f1 = open("/Users/yuanmengyue/Desktop/小区-用户-修正.json", mode='w',encoding='utf-8')
a = json.dumps(cityBlock_list_dic,ensure_ascii=False)
b = str(a) + "\n"
f1.write(b)
print("写入成功")



