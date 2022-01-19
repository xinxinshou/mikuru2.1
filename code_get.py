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
info={}
#51招聘
#url='https://jobs.51job.com/hefei-gxq/121766663.html?s=sou_sou_soulb&t=0'（示例）
company_name=''
job_bonus=''
sleep(15)
'''soup=BeautifulSoup(driver.page_source,'lxml')'''
if('51job' in url):
    '''job_require=soup.find(class_='bmsg job_msg inbox')
    job_requirements_list=[]
    for i in job_require.contents:
        if(i.string is not None):
            job_requirements_list.append(i.string.strip())
        if((i.name is 'div')or(i is None)):
            break'''
    '''company_name=str(soup.find(class_='catn').contents[0])'''
    try:
        title=driver.find_elements_by_css_selector('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1').text
    except:
        title=''
    info['title']=title
    try:
        salary_range=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong').text
    except:
        salary_range=''
    info['salary_range']=salary_range
    try:
        location=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/a').get_attribute('onclick').split('\'')[3]
    except:
        location=''
    info['location']=location
    try:
        department=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[3]/div').text[5:].split('\n')[0]
    except:
        department=''
    info['department']=department
    try:
        benefit=driver.find_element_by_class_name("jtag").text.replace("\n",'、')
    except:
        benefit=''
    info['benefit']=benefit
    try:
        required_education=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]').text.split('|')[2].split()[0]
    except:
        required_education=''
    info['required_education']=required_education
    try:
        required_experience=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]').text.split('|')[1].split()[0]
    except:
        required_experience=''
    info['required_experience']=required_experience
    try:
        industry=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[1]/div[2]/p[3]').text
    except:
        industry=''
    info['industry']=industry
    try:
        fuction=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/div[1]/p[1]/a').text
    except:
        fuction=''
    info['fuction']=fuction
    if len(driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[1]/div[1]/a').find_elements_by_tag_name('img'))==0:
        has_company_logo=0
    else:
        has_company_logo=1
    try:
        description_origin=[i for i in driver.find_element_by_class_name('bmsg').text.replace(' ','').split('\n') if i!='']
    except:
        description_origin=''
    if '岗位职责' in description_origin:
        index1=description_origin.index('岗位职责')
    elif '工作职责' in description_origin:
        index1=description_origin.index('工作职责')
    elif '岗位职责：' in description_origin:
        index1=description_origin.index('岗位职责：')
    elif '工作职责：' in description_origin:
        index1=description_origin.index('工作职责：')
    elif 'Responsibility:' in description_origin:
        index1=description_origin.index('Responsibility:')
    else:
        index1=0
    if '任职要求' in description_origin:
        index2=description_origin.index('任职要求')
    elif '任职资格' in description_origin:
        index2=description_origin.index('任职资格')
    elif '任职要求：' in description_origin:
        index2=description_origin.index('任职要求：')
    elif '任职资格：' in description_origin:
        index2=description_origin.index('任职资格：')
    elif 'Requirements::' in description_origin:
        index2=description_origin.index('Requirements:')
    if index2>index1:
        description=description_origin[index1:]
        requirements=description_origin[index2:index1-1]
    else:
        description=description_origin[index2:]
        requirements=description_origin[index1:index2-1]
    info['description']=''.join(description[1:])
    info['requirements']=''.join(requirements[1:])
'''elif('zhipin' in url):
    job_bonus='、'.join([i.string.strip() for i in soup.find('div',class_='job-tags') if len(i.string)>1])
    job_requirements=''.join([i.string.replace('\n','').strip() for i in soup.find('div',class_='text').contents if(i.string is not None)])
    company_name=soup.find(string='工商信息').parent.parent.find('div',class_='name').string
    t=soup.find(string='公司介绍').parent.parent.find('div',class_='text')'''


print(info)
#print('公司信息:'+company_profile)
#通过上企查查判断企业是否为失信企业、有营业执照
#判断经营状况（未实现）
'''url2='https://www.qcc.com/web/search?key='+company_name
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
    print('企查查中未能找到该企业的相关信息')'''
        
