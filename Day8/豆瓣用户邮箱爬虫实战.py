import requests         #下载网页
import bs4              #解析网页
import re               #文本处理

#请求头部声明
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
#下载url指定的网页及其所有的分页
def download_page(url):
    #获取初始网页源码
    current_page_obj=requests.get(url,headers=headers)
    current_bs4_obj=bs4.BeautifulSoup(current_page_obj.text,"lxml")
    bs4_obj_list = [current_bs4_obj]  # 存储所有网址源码的列表
    #获取分页网址
    paginator_element=current_bs4_obj.find("div",attrs={"class":"paginator"})#当前网页中存取其他分页网址的代码块在paginator中
    if paginator_element:
        url_set = set()  # 集合存其他分页网址
        for a_ele in paginator_element.find_all("a"):#某个特定分页网址存在paginator的a块中
            url_set.add(a_ele.attrs.get("href"))
        for url in url_set:
            print(f"下载分页{url}")
            page_obj=requests.get(url,headers=headers)
            bs4_page_obj=bs4.BeautifulSoup(page_obj.text,"lxml")
            bs4_obj_list.append(bs4_page_obj)
    return bs4_obj_list

#获取邮箱
def get_email(bs4_obj_list):
    email_list=[]
    for bs4_obj in bs4_obj_list:
        comment_element=bs4_obj.find_all("div",attrs={"class":"reply-doc"})
        for element in comment_element:
            address_ele=element.find("p",attrs={"class":"reply-content"})
            pubtime_ele=element.find("span",attrs={"class":"pubtime"})
            address=re.search("\w+@\w+.\w+",address_ele.text,flags=re.A)
            pubtime=pubtime_ele.text
            if address and pubtime:
                email_list.append({"address":address.group(),"pubtime":pubtime})
    for email in email_list:
        print("pubtime:"+email["pubtime"]+"   address:"+email["address"])
    print("共收集到"+str(len(email_list))+"条记录")

bs4_obj_list=download_page("https://www.douban.com/group/topic/198233257/")
get_email(bs4_obj_list)