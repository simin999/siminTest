from tools.random_str import *
class GetData():
    car_info_id=None
    car_id=None
    car_num="粤C"+''.join(random.choices(string.ascii_uppercase + string.digits, k=5))  #生成随机车牌
    vin_num=random_vin()
    img_path="https://test-images-cdn.cheanjia.com/zhongsheng/rXxCKC6VigHegewpbrkTcK.jpg"  #服务器上的一个图片地址

if __name__ == '__main__':
    print(GetData().car_num)