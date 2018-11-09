import time
import requests
import re


class Login:

    def __init__(self):
        # 检测间隔时间，单位为秒
        self.every = 30

    # 模拟登录
    def login(self):

        print(self.getCurrentTime(), u"拼命连网中...")

        url = "http://202.204.48.82/"
        # 消息头
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '55',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '__guid=60303022.1266821893518176300.1531809304239.62; myusername=%s; ' % id +
                      'username=%s; monitor_count=12' % id,
            'Host': '202.204.48.82',
            'Origin': 'http://202.204.48.82',
            'Referer': 'http://202.204.48.82/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }

        data = {
            'DDDDD': id,
            'upass': psw,
            'v6ip': '',
            '0MKKey': '123456789'
        }

        try:
            requests.post(url, headers=headers, data=data)
            print(self.getCurrentTime(), u'连上了...现在开始看连接是否正常')
        except:
            print("error")

    # 判断当前是否可以连网
    def canConnect(self):
        try:
            q = requests.get("http://www.baidu.com", timeout=5)
            m = re.search(r'STATUS OK', q.text)
            if m:
                return True
            else:
                return False
        except:
            print('error')
            return False

    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    # 主函数
    def main(self):
        print(self.getCurrentTime(), u"Hi，欢迎使用自动登陆系统")
        while True:
            self.login()
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print(self.getCurrentTime(), u"断网了...")
                    self.login()
                else:
                    print(self.getCurrentTime(), u"一切正常...")
                time.sleep(self.every)
            time.sleep(self.every)


#######################################################

id = '41624621'  # 请在这里输入学号！

psw = '02070207'  # 请在这里输入密码！

#########################################################


login = Login()
login.main()
