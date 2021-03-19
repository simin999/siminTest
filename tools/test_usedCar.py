import unittest
from tools.http_requests import HttpResuest
from tools.do_excel import DoExcle
from tools.get_path import *
from tools.login_getCookies import login
from tools.get_data import GetData
from tools.my_log import MyLog
from ddt import ddt, data
import json

cookies, headers = login()
test_data = DoExcle(test_data_path).get_data()


@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_usedCar_collection(self, item):
        print("用例名称：{}".format(item["title"]))
        # print("car_id:{}".format(getattr(GetData,'car_id')))
        if item['url'].find('#{car_id}') != -1:
            '''从反射里拿到car_id替换#{car_id}'''
            item['url'] = item['url'].replace('#{car_id}', getattr(GetData, 'car_id'))
        if item['url'].find('#{car_info_id}') != -1:
            '''从反射里拿到{car_info_id}替换#{car_info_id}'''
            item['url'] = item['url'].replace('#{car_info_id}', getattr(GetData, 'car_info_id'))
        if item['data'].find('${car_num}') != -1:
            '''从反射里拿到车牌号替换${car_num}'''
            item['data'] = item['data'].replace('${car_num}', getattr(GetData, 'car_num'))
        else:
            pass
        d = eval(item["data"])
        print("url:{}".format(item['url']))
        # 如果参数类型是json，要在header里加上“Content-Type：application/json”，并且要对data进行处理
        if item['contentType'] == 'json':
            headers["Content-Type"] = "application/json"
            d = json.dumps(eval(item["data"]))
            res = HttpResuest.http_request(url=item['url'], data=d, method=item['method'], headers=headers,
                                           cookies=cookies)
            # 请求结束后删除headers里面的Content-Type,因为后续接口的传参格式不一定是json
            del headers["Content-Type"]

        else:
            res = HttpResuest.http_request(url=item['url'], data=d, method=item['method'], headers=headers,
                                           cookies=cookies)
        r = json.loads(res.text)  # 将response格式转化为python字典格式
        print("code:{}".format(r["code"]), "message:{}".format(r["message"]))
        if item['title'] == '新建线索':
            '''将新建线索生成的车辆id保存，用于下一个接口查询car_id'''
            car_id = r["data"]["id"]
            setattr(GetData, 'car_id', str(car_id))
            # MyLog().info('存储car_id为{0}'.format(car_id))
            print('存储car_id为{0}'.format(car_id))
        elif item['title'] == '获取car_info_id':
            '''将新建线索生成的车辆的car_info_id获取到并储存起来，用于后续接口'''
            car_info_id = r["data"]["car_info_id"]
            setattr(GetData, 'car_info_id', str(car_info_id))
            # MyLog().info('存储car_id为{0}'.format(car_id))
            print('存储car_info_id为{0}'.format(car_info_id))
        try:
            self.assertEqual(str(r["code"]), str(item['excepted']))
            test_result = 'pass'
        except AssertionError as e:
            test_result = 'fail'
            MyLog().error("执行用例出错：{0}".format(e))
            print(e)
            raise
        finally:
            '''结果写回excel'''
            DoExcle(test_data_path).write_back(item['sheetname'], int(item['case_id']) + 1, 9, str(r))
            DoExcle(test_data_path).write_back(item['sheetname'], int(item['case_id']) + 1, 10, test_result)
            # MyLog().error("获取到的结果是：{0}".format(res))
