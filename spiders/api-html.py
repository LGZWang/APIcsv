from bs4 import BeautifulSoup
import csv

f = open('F:/PycharmProjects/API-csv/data/api-data.csv','w', newline='',encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["package_name","package_description","class_name","class_definition","class_description","method_name","method_full_name","method_type","method_description"])
fp = open('F:/API-data/tool.oschina.net/uploads/apidocs/jdk_7u4/overview-summary.html','r',encoding='utf-8')
soup = BeautifulSoup(fp,'lxml')

#package
project = soup.find_all('td',class_='colFirst')


for a_list in project:
    a = a_list.find("a").get("href")
    package = a.split(".")[0].replace("/package-summary","").replace("/",".")
    print(package)

    try:
        summary = open('F:/API-data/tool.oschina.net/uploads/apidocs/jdk_7u4/' + a, 'r', encoding='utf-8')
    except:
        pass


    detail_summary = BeautifulSoup(summary, 'lxml')

    description = detail_summary.findAll('div', class_="block")
    api_desc = description[len(description) - 1].text.strip()

    if detail_summary.find(summary="Class Summary table, listing classes, and an explanation") is None:
        pass
    else:
        detail_class = detail_summary.find(summary="Class Summary table, listing classes, and an explanation")

    api_class_alt = detail_class.find_all('tr', class_='altColor')
    api_class_row = detail_class.find_all('tr', class_='rowColor')
    api_class_list = api_class_alt + api_class_row
   # print(len(api_class_list))

    num = 0
    for api_class in api_class_list:
        # API类名
        # class_name = package + "." + api_class.find(class_='colFirst').text
        if api_class.find(class_='colFirst') is None:
            class_name = "NULL"
        else:
            class_name1 = api_class.find(class_='colFirst').text
            class_name = package+"."+class_name1

        if api_class.find(class_="colLast") is None:
            class_desc = "NULL"
        else:
            class_desc = api_class.find(class_="colLast").text
        try:
            class_summary = open('F:/API-data/tool.oschina.net/uploads/apidocs/jdk_7u4/' + package.replace(".",
                                                                                                           "/") + "/" + class_name1 + '.html',
                                 'r', encoding='utf-8')
        except:
            pass

        try:
            class_detail_summary = BeautifulSoup(class_summary, 'lxml')
        except:
            pass

        '''if class_detail_summary.find('pre') is None:
            class_code = "NULL"
        else:'''
        try:
            class_code = class_detail_summary.find('pre').text
        except:
            pass

        #print(package)
        print(class_name)
        #print(class_desc)
        #print(class_code)
        # class_desc= class_detail_summary.find('div',class_="block").text

        if class_detail_summary.find(summary="Method Summary table, listing methods, and an explanation") is None:
            pass
        else:
            detail_method = class_detail_summary.find(
                summary="Method Summary table, listing methods, and an explanation")
        api_method_alt = detail_method.find_all('tr', class_="altColor")

        api_method_row = detail_method.find_all('tr', class_="rowColor")
        api_method = api_method_alt + api_method_row
        # print(api_method)
        # num=0
        for api_method_detail in api_method:
            if api_method_detail.find('td', class_='colFirst') is None:
                modifier_type = "NULL"
            else:
                modifier_type = api_method_detail.find('td', class_='colFirst').text

            if api_method_detail.find('td', class_="colLast") is None:
                pass
            else:
                api_method_name = api_method_detail.find('td', class_="colLast")
            if api_method_name.find('code') is None:
                method_name = "NULL"
                method_full_name = "NULL"
            else:
                method_name = api_method_name.find('code').text
                method_full_name = class_name + "." + method_name


            if api_method_name.find('div', class_="block") is None:
                method_desc = "NULL"
            else:
                method_desc = api_method_name.find('div', class_="block").text
            # num = num +1
            #print(method_name)
            #print(modifier_type)
            #print(method_desc)
            csv_writer.writerow([package, api_desc, class_name, class_code, class_desc,method_name,method_full_name,modifier_type,method_desc])

        num = num + 1
    print(num)



    print(package + " is Done!\n")


f.close()
fp.close()
summary.close()
class_summary.close()

print("OK! It's Done!")


