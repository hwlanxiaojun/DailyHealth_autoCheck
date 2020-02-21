# coding=utf-8
import time
import requests
import datetime
import os
import logging
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

FILE = os.getcwd()
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=os.path.join(FILE,'log.txt'),level=logging.INFO, format=LOG_FORMAT)

def main():
    # sign_time = 30   # 表示 十点十分 开始发起签到
    # time_now = int(str_time("%H%M"))
    # print(time_now)
    # while time_now < sign_time:
    #     logging.info('未到指定的签到时间')
    #     time.sleep(3600)
    #     time_now = int(str_time("%H%M"))
    username = ('hw','xqj')
    data_hw = "__EVENTTARGET=btn_save&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTEzNTEwODU3MzVkZDhM0W2mmY%2FQcBGYFZvZdKtttGlswbEBjPre34vuLU76&__VIEWSTATEGENERATOR=6440A837&__EVENTVALIDATION=%2FwEdABnVHyl9a9AOCn2G8OhlSE5JnPdgn5d6iO4LuTjGeN2JM3llOAzR6kycDzMfToHX0QOa6jYEaUq7hqoikcwmGDr%2F8yaCO%2BVJK%2FabEf%2F%2BDoN4OdH1TgiXWJ3vBZveMs%2Bmp1OuBsgevre4owTMJ%2F%2F00S9EYdp8PLLcr00Ykm6GIg%2FQPi9I311nTmVD04G0BwQ8Mpm%2BsJbANGHcqYHApfGsIQ8QYGLhwJiw6sD7UIfRwxLSY6%2FnOzRMBX93ORT3mHUsq162CDn2UEuzIfI1sUP90tnx5P8BqRj8hMmLTrb0G2e3sglqBIjug3flekZR5fVAziWFR5XBaovvqbAL2ZPavURuVtaUX72GBYV4O9smDpp6ckppvV9lNremNdT%2FieJVcmpZvp9ClIOsG4ZuNkbyjee%2B5S9s1nGw%2BswGhIm9M52iPLVrCx%2FB%2FjV0FGA%2BCpMLOAX6CaSK%2BG9A1e3mRYerTC1Ms58OqStYqDOkSsiO020Mm5VOETTRN6RG%2FlVMY%2BNME9bdhTji1LNIN94nXMo1QgrAcjj%2BucA48KUp6Nh4Qkv%2BHy56%2BNt7wIhVGv6gjZjJeh0%3D&personname=%E9%9F%A9%E7%8E%AE&personcode=201730210423&txtCreateTime=" + datetime.datetime.now().strftime('%Y-%m-%d') + "&DATA_3=%E5%81%A5%E5%BA%B7&DATA_4=%E5%90%A6&DATA_5=%E5%90%A6&DATA_6=%E5%90%A6&DATA_7=&DATA_8=%E5%90%A6&DATA_17=%E5%90%A6&DATA_18=%E5%90%A6&DATA_19=&DATA_9=&hidDATA_3=%E5%81%A5%E5%BA%B7&hidDATA_4=%E5%90%A6&hidDATA_5=%E5%90%A6&hidDATA_6=%E5%90%A6&hidDATA_7=&hidDATA_8=%E5%90%A6&hidDATA_9=&hidDATA_10=&hidDATA_11=&hidDATA_12=&hidDATA_13=&hidDATA_14=&hidDATA_15=&hidDATA_16=&hidDATA_17=%E5%90%A6&hidDATA_18=%E5%90%A6&hidDATA_19="
    data_xqj = "__EVENTTARGET=btn_save&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTEzNTEwODU3MzVkZDhM0W2mmY%2FQcBGYFZvZdKtttGlswbEBjPre34vuLU76&__VIEWSTATEGENERATOR=6440A837&__EVENTVALIDATION=%2FwEdABnVHyl9a9AOCn2G8OhlSE5JnPdgn5d6iO4LuTjGeN2JM3llOAzR6kycDzMfToHX0QOa6jYEaUq7hqoikcwmGDr%2F8yaCO%2BVJK%2FabEf%2F%2BDoN4OdH1TgiXWJ3vBZveMs%2Bmp1OuBsgevre4owTMJ%2F%2F00S9EYdp8PLLcr00Ykm6GIg%2FQPi9I311nTmVD04G0BwQ8Mpm%2BsJbANGHcqYHApfGsIQ8QYGLhwJiw6sD7UIfRwxLSY6%2FnOzRMBX93ORT3mHUsq162CDn2UEuzIfI1sUP90tnx5P8BqRj8hMmLTrb0G2e3sglqBIjug3flekZR5fVAziWFR5XBaovvqbAL2ZPavURuVtaUX72GBYV4O9smDpp6ckppvV9lNremNdT%2FieJVcmpZvp9ClIOsG4ZuNkbyjee%2B5S9s1nGw%2BswGhIm9M52iPLVrCx%2FB%2FjV0FGA%2BCpMLOAX6CaSK%2BG9A1e3mRYerTC1Ms58OqStYqDOkSsiO020Mm5VOETTRN6RG%2FlVMY%2BNME9bdhTji1LNIN94nXMo1QgrAcjj%2BucA48KUp6Nh4Qkv%2BHy56%2BNt7wIhVGv6gjZjJeh0%3D&personname=%E8%82%96%E7%90%A6%E5%A9%A7&personcode=201730210415&txtCreateTime=" + datetime.datetime.now().strftime('%Y-%m-%d') + "&DATA_3=%E5%81%A5%E5%BA%B7&DATA_4=%E5%90%A6&DATA_5=%E5%90%A6&DATA_6=%E5%90%A6&DATA_7=&DATA_8=%E5%90%A6&DATA_17=%E5%90%A6&DATA_18=%E5%90%A6&DATA_19=&DATA_9=&hidDATA_3=%E5%81%A5%E5%BA%B7&hidDATA_4=%E5%90%A6&hidDATA_5=%E5%90%A6&hidDATA_6=%E5%90%A6&hidDATA_7=&hidDATA_8=%E5%90%A6&hidDATA_9=&hidDATA_10=&hidDATA_11=&hidDATA_12=&hidDATA_13=&hidDATA_14=&hidDATA_15=&hidDATA_16=&hidDATA_17=%E5%90%A6&hidDATA_18=%E5%90%A6&hidDATA_19="
    datas = (data_hw,data_xqj)

    cookies_hw = '''gr_user_id=ce6abdb6-0f28-4028-ae98-34197f3eca27; grwng_uid=3009382d-d595-4b0b-9aab-9b8203029e7f; 8a762667df5cb9d5_gr_last_sent_cs1=567465; LastUserCode=201730210423; old_device_token=8c2958342a6eb78183eee18de2da62b3; device_token=3d66c2ed6d953b57c1d0a9a2fb0093ec; 8a762667df5cb9d5_gr_cs1=567465; ASP.NET_SessionId=byouw3qymnyu1zybrvgmsdbh; yxkj_ticket=LleRyH/Xwz1/AXtwEEs9Mw=='''
    cookies_xqj = '''gr_user_id=ce6abdb6-0f28-4028-ae98-34197f3eca27; grwng_uid=3009382d-d595-4b0b-9aab-9b8203029e7f; 8a762667df5cb9d5_gr_last_sent_cs1=567465; LastUserCode=201730210415; 8a762667df5cb9d5_gr_cs1=567465; ASP.NET_SessionId=h4libveubpo4najj3op5hvvf; yxkj_ticket=LleRyH/Xwz0k2d3z2pgJVw=='''
    cookies = (cookies_hw,cookies_xqj)

    for i in range(len(datas)):
        sign_res = sign_in(datas[i],cookies[i])
        logging.info(username[i]+"开始提交")
        if sign_res != "":
            if sign_res.find("PK_ZJSFDX_DailyHealthDisease")!=-1:
                logging.info(username[i]+"重复提交")
            elif sign_res.find("提交成功！若本人现居住地和健康码情况有变动，请及时到“基本信息”中更新！")!=-1:
                logging.info(username[i]+"提交成功")

def sign_in(data,cookie):
    url = "http://zyt.zjnu.edu.cn/H5/ZJSFDX/CheckDaily.aspx"
    url = "http://zyt.zjnu.edu.cn/H5/ZJSFDX/DailyHealth.aspx"
    try:
        headers = {
            "Cookie": cookie,
            "content-type": "application/x-www-form-urlencoded",
            "Referer": "http://zyt.zjnu.edu.cn/H5/ZJSFDX/DailyHealth.aspx"
        }
        response=requests.post(url,headers=headers,data=data,timeout=(2, 30))  #timeout(2, 30)表示的连接时间是2，响应时间是30
        response.encoding = response.apparent_encoding
        print(response.text)
        return response.text
    except requests.exceptions.ReadTimeout:
        print("requests.exceptions.ReadTimeout:[%s]" % url)
        return ""
    except requests.exceptions.ConnectionError:
        print("requests.exceptions.ConnectionError:[%s]" % url)
        return ""

def str_time(pattern='%Y-%m-%d %H:%M:%S'):
    return time.strftime(pattern, time.localtime(time.time()))
if __name__ == "__main__":
    main()