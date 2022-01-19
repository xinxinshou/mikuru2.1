from selenium import webdriver
from bs4 import BeautifulSoup
import re
from time import sleep 

#获取公司简介和岗位要求
option = webdriver.ChromeOptions()
#prefs = {"profile.managed_default_content_settings.images": 2}
#option.add_experimental_option("prefs", prefs)
#option.add_argument("--headless")   
url=input('请输入岗位网址（目前仅支持51招聘和boss直聘网站）')
driver = webdriver.Chrome(options=option)
driver.get(url)
#51招聘
#url='https://jobs.51job.com/hefei-gxq/121766663.html?s=sou_sou_soulb&t=0'（示例）
company_name=''
job_bonus=''
sleep(10)
soup=BeautifulSoup(driver.page_source,'lxml')
if('51job' in url):
    '''job_require=soup.find(class_='bmsg job_msg inbox')
    job_requirements_list=[]
    for i in job_require.contents:
        if(i.string is not None):
            job_requirements_list.append(i.string.strip())
        if((i.name is 'div')or(i is None)):
            break'''
    job_requirements=driver.find_element_by_class_name('tBorderTop_box').text.replace('\n','')
    company_info_list=[i.string for i in soup.find(class_='tmsg inbox').contents if i.string is not None]
    company_name=str(soup.find(class_='catn').contents[0])
    company_info=''.join(company_info_list).replace(" ",'')
    #job_requirements=''.join(job_requirements_list)
    job_bonus=driver.find_element_by_class_name("jtag").text.replace("\n",'、')
elif('zhipin' in url):
    job_bonus='、'.join([i.string.strip() for i in soup.find('div',class_='job-tags') if len(i.string)>1])
    job_requirements=''.join([i.string.replace('\n','').strip() for i in soup.find('div',class_='text').contents if(i.string is not None)])
    company_name=soup.find(string='工商信息').parent.parent.find('div',class_='name').string
    t=soup.find(string='公司介绍').parent.parent.find('div',class_='text')
print('公司名称:'+company_name)
print('福利待遇:'+job_bonus)
print('岗位需求:'+job_requirements)
print('公司信息:'+company_info)
#通过上企查查判断企业是否为失信企业、有营业执照
#判断经营状况（未实现）
url2='https://www.qcc.com/web/search?key='+company_name
driver.get(url2)
while('405' in driver.current_url):
    driver.get(url2)
soup2=BeautifulSoup(driver.page_source,'lxml')
try:
    url3=str(soup2.find_all(class_='maininfo')[0].find_all(class_='title')[0]['href'])#获得企查查第一个搜索结果的详细界面的链接
    driver.get(url3.replace('firm','cbase'))
    soup3=BeautifulSoup(driver.page_source,'lxml')
    print('是否失信:',end="")
    if(re.search('失信',soup3.prettify()) == '失信'):
        print('是')
    else:
        print('否')
except:
    print('企查查中未能找到该企业的相关信息')