# -*- coding:utf-8 -*-
import requests
import json
from tools.my_log import MyLog

class HttpResuest():
    @staticmethod
    def http_request(url,data,method,cookies=None,headers=None):
        requests.packages.urllib3.disable_warnings()
        # headers = {"Content-Type": "application/json"}
        # data = json.dumps(data)
        if method=="get":
            MyLog().info("接口{0}的请求参数是：{1}".format(url, data))
            try:
                r = requests.get(url=url,data=data,headers=headers,cookies=cookies,verify=False)
                response=r.text
                print("get请求结果为：{}".format(response))
                MyLog().info("接口{0}的请求结果是：{1}".format(url,response))
                return r
            except BaseException as e:
                print("get请求错误，错误原因：{}".format(e))
                MyLog().info("get请求错误，错误原因：{}".format(e))
        elif method=="post":
            MyLog().info("接口{0}的请求参数是：{1}".format(url, data))
            try:
                r = requests.post(url=url, data=data,headers=headers,cookies=cookies,verify=False)
                response = r.text
                print("post请求结果为：{}".format(response))
                MyLog().info("接口{0}的请求结果是：{1}".format(url, response))
                return r
            except BaseException as e:
                print("post请求错误，错误原因：{}".format(e))
                MyLog().info("post请求错误，错误原因：{}".format(e))
        elif method=="put":
            MyLog().info("接口{0}的请求参数是：{1}".format(url,data))
            try:
                r = requests.put(url=url, data=data, headers=headers,cookies=cookies, verify=False)
                response = r.text
                print("put请求结果为：{}".format(response))
                MyLog().info("接口{0}的请求结果是：{1}".format(url, response))
                return r
            except BaseException as e:
                print("put请求错误，错误原因：{}".format(e))
                MyLog().info("put请求错误，错误原因：{}".format(e))
