import os
import csv



def get_key(dict,value):
    return [k for k, v in dict.items() if v == value]

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
              #"武汉钢铁集团公司":'',
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


# 遍历街道.csv文件，获取各个街道居民在外签到的数量，在某些区域签到POI数量，不同种类POI签到数量
# 先统计签到数量吧，写一个csv表，各街道对应的在外签到数量
data_path = "/Users/yuanmengyue/Desktop/COVID-19/DATA/Select_Street2"
for root,dir,file in os.walk(data_path):
    for filename in file:
        if filename != '.DS_Store' and filename !='.csv':
        


            filepath = os.path.join(root,filename)
            # csv文件名为街区，这里注意转换成街道记录
            street_name = filename.split('.')[0]
            streetname = get_key(Street_dic, street_name)[0]


            with open(filepath,encoding='gbk') as csvfile:
                reader = csv.reader(csvfile)
                count = 0
                for row in reader:
                    count +=1

            # 先统计签到数量吧，写一个csv表，各街道对应的在外签到数量
            write_path = "/Users/yuanmengyue/Desktop/COVID-19/DATA/street_checkin_number.csv"
            with open(write_path,'a',encoding='gbk') as writefile:
                writer = csv.DictWriter(writefile,['Street_Name','checkin_number'])
                data = {}
                data['Street_Name'] = streetname
                data['checkin_number'] = count
                writer.writerow(data)
                print(data)
                print("写入成功")





