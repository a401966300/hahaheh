'''
主要实现基础接口的封装
'''
import requests
from loguru import logger
from setting import base_url
from cacheout import cache


class Base():

    # 实现url拼接
    def get_url(self,path,params=None):
        '''
        功能：返回一个完整的url
        eg: base_url/接口地址/参数
        '''
        if params:
            full_url= base_url + path + '?' + params
            #logger.info('接口地址：{}'.format(full_url))
            return full_url
        return base_url + path
    #定义get方法
    def get(self,url):
        result = None
        response = requests.get(url,headers=self.get_headers())
        try:
            result = response.json()
            logger.debug('请求接口地址:{},请求接口返回结果:{}'.format(url,result))
            return result
        except Exception as e:
            logger.error('请求get方法错误，返回数据:{}'.format(result))
    def post(self,url,data):
        result = None
        response = requests.post(url,json=data,headers = self.get_headers())
        try:
            result = response.json()
            logger.debug('请求接口地址:{},请求接口返回结果:{}'.format(url,result))
            return result
        except Exception as e:
            logger.error('请求post方法错误，返回数据:{}'.format(result))

    # 定义请求头的处理
    def get_headers(self):
        headers = {'Content-type':'application/json'}
        token = cache.get('token')       # 获取缓存的token值
        if token:
            headers.update({'xxxxxxx'})    # update 更新字典，相当于把新增内容到原字典中
        logger.warning('请求头信息返回数据:{},注意，多数接口时需要带token参数'.format(headers))
        return headers

    # 定义登陆
    def login(self,username,password):
        login_path = '/admin/auth/login'
        login_url = self.get_url(login_path)
        login_data = {'username':'username','password':'password'}
        result = self.post(login_url,login_data)
        try:
            if 0 == result.get('error'):
                logger.info('请求登陆接口成功')
                token = result.get('data').get('token')
                cache.set('token',token)    # 将获取的token值缓存
            else:
                logger.error('请求登陆接口失败:{}'.format(result))
        except Exception as e:
            logger.error('请求登陆接口异常，异常数据:{}'.format(result))



if __name__ == '__main__':
    b = Base()
    #print(b.get_url('/admin','q=iphone'))
    print(b.login('admin123','admin123'))



