import json
import os


def walk(date):
    data_path = "/Users/yuanmengyue/Desktop/微博数据201912-202001/" + date + "/湖北省/武汉市.json"
    with open(data_path) as jsonfile:
        for line in jsonfile.readlines():
            rline = json.loads(line)
            user_id = rline["user"]["id"]
            idstr = rline["mid"]

            path_to_write  = "/Users/yuanmengyue/Desktop/武汉市12月1月数据按用户分类/" + str(user_id)
            path_to_write_json = path_to_write + "/" + str(user_id) + ".json"

            judgeExisting = os.path.exists(path_to_write)

            if not judgeExisting:
                os.makedirs(path_to_write)
                #print(str(path_to_write) + '创建成功！')


            write_Json_data(path_to_write_json, rline,idstr)

    return 0


def write_Json_data(path_to_write,rline,idstr):
    judgeExisting = os.path.exists(path_to_write)
    if not judgeExisting:
        f1 = open(path_to_write, mode='w')
        a = json.dumps(rline)
        b = str(a) + "\n"
        f1.write(b)
        #print(idstr,"写入成功！")

    else:
        # 若该json已存在
        f1 = open(path_to_write, mode='a')
        a = json.dumps(rline)
        b = str(a) + "\n"
        f1.write(b)
        #print(idstr,"写入成功！")

    return 0


if __name__ == '__main__':


    date = "2020-01-01"

    day = int(date.split('-')[2])

    while day < 10:
        date = "2020-01-0" + str(day)
        print(date)
        walk(date)
        day += 1

    while day >= 10 and day <= 31:
        date = "2020-01-" + str(day)
        print(date)
        walk(date)
        day += 1










