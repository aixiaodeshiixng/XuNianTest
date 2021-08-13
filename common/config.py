class Config:
    @property
    def URL(self):
        # return 'http://192.168.0.129:'
        # return 'http://47.119.114.16:'
        # 叙年文学开发环境
        return 'http://192.168.0.147:'
    @property
    def PORT(self):
        # return '8090'
        # return '8098'
        # 叙年文学开发端口号
        return '8085'
local_config = Config()

if __name__=='__main__':
    print(local_config.URL+local_config.PORT)