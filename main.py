from api import fofa_api
from setting import copyright, config, usage

if __name__ == '__main__':

    # 引入API KEY
    fofa_email, fofa_key, zoomeye_key, shodan_key = config.config()
    # 引入版权信息
    copyright.CopyRight()
    # 引入命令行参数设置
    search, szie, page = usage.Terminal()
    if search == "":

    # 三个任选
    #fofa_api.fofa().Terminal(fofa_email,fofa_key) # 调用Fofa API
    #shodan_api # 调用shodan API
    #zoomeye_api # 调用zoomeye API

