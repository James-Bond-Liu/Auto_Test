# -*- coding: utf-8 -*-
# @Time :2020/10/11 14:33
# @Author : liufei
# @File :suds库操作.PY

from suds.client import Client

#创建一个webservice对象，来调用webservice里面的各类接口
api_url = r'http://cmdp-query.intsit.xxx.com.cn:1080/ws/saspClaims?wsdl' #这里是你的webservice访问地址
client = Client(api_url)  # Client里面直接放访问的URL，可以生成一个webservice对象
print(client) #打印出这个wsdl地址里面的所有接口信息：所有接口方法名称

# 利用soapui来看看webservice某个接口的组成和参数
params_dict = {"billingCode":"2", "sysCode":"111"} #用字典的方式传值

#findClaimsInfoList - 调用被测服务的接口
result = client.service.findClaimsInfoList(**params_dict)
#打印返回结果
print(result)

#查看webservice服务的所有接口
client = Client('xxxx_webservice_url')
def get_all_methods(client):
    return [method for method in client.wsdl.services[0].ports[0].methods]

# 查看某个具体接口的传输参数及类型
def get_method_args(client, method_name):
    method = client.wsdl.services[0].ports[0].methods[method_name]
    input_params = method.binding.input
    return input_params.param_defs(method)

# 调用接口服务
client.service.xxx_function('参数')

#关于调试
# 输出之前调用服务接口时发送了什么soap报文，以及收到什么样的soap报文
print('last sent:\n', client.last_sent())
print('last recv:\n', client.last_received())

