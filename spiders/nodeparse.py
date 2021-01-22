import pandas as pd

df = pd.read_csv('F:/PycharmProjects/API-csv/data/api-data.csv',encoding='utf-8')

#获取package、class、method的集合，方便ID编号
df_package = df['package_name']
df_package1 = df['package_description']
df_class = df['class_name']
df_class1 = df['class_definition']
df_class2 = df['class_description']
df_method = df['method_name']
df_method1 = df['method_full_name']
df_method2 = df['method_type']
df_method3 = df['method_description']
#print(df_package)

packageID, classID, methodID = [], [], []

#获取不重复package的列表、数量、df表
packageList = []
for pack in df_package:
    packageList.append(pack)
package_List = list(set(packageList))
package_List.sort(key= packageList.index)
package_num = len(package_List)
df_package_name = pd.DataFrame(data=package_List, columns=['packageName'])
#print(packageList)
#获取不重复package的列表、数量、df表
packageList1 = []
for pack in df_package1:
    packageList1.append(pack)
package_List1 = list(set(packageList1))
package_List1.sort(key= packageList1.index)
df_package_desc = pd.DataFrame(data=package_List1, columns=['packageDesc'])
#print(packageList)


#获取不重复class的列表、数量、df表
classList = []
for cl in df_class:
    classList.append(cl)
class_List = list(set(classList))
class_List.sort(key=classList.index)
class_num = len(class_List)
df_class_name = pd.DataFrame(data=class_List, columns=['className'])
#获取不重复class的列表、数量、df表
classList1 = []
for cl in df_class1:
    classList1.append(cl)
class_List1 = list(set(classList1))
class_List1.sort(key=classList1.index)
df_class_defi = pd.DataFrame(data=class_List1, columns=['classDefi'])
#获取不重复class的列表、数量、df表
classList2 = []
for cl in df_class2:
    classList2.append(cl)
class_List2 = list(set(classList2))
class_List2.sort(key=classList2.index)
df_class_desc = pd.DataFrame(data=class_List2, columns=['classDesc'])

#获取method的列表、数量、df表
methodList = list(df_method)
method_num = len(methodList)
df_method_name = pd.DataFrame(data=methodList, columns=['methodName'])
#获取method的列表、数量、df表
methodList1 = list(df_method1)
df_method_fullName = pd.DataFrame(data=methodList1, columns=['methodFullName'])
#获取method的列表、数量、df表
methodList2 = list(df_method2)
df_method_type = pd.DataFrame(data=methodList2, columns=['methodType'])
#获取method的列表、数量、df表
methodList3 = list(df_method3)
df_method_desc = pd.DataFrame(data=methodList3, columns=['methodDesc'])

#生成package的ID
for i in range(10001,10001+package_num):
    packageID.append(i)
df_package_ID = pd.DataFrame(data=packageID, columns=['packageID'])

#生成class的ID
for i in range(20001,20001+class_num):
    classID.append(i)
df_class_ID = pd.DataFrame(data=classID, columns=['classID'])

#生成method的ID
for i in range(30001,30001+method_num):
    methodID.append(i)
df_method_ID = pd.DataFrame(data=methodID, columns=['methodID'])

#拼接package表
pack = pd.concat([df_package_ID,df_package_name,df_package_desc],axis=1)
pack['label']='Package'

#拼接class表
cl = pd.concat([df_class_ID,df_class_name,df_class_defi,df_class_desc],axis=1)
cl['label']='Class'

#拼接class表
me = pd.concat([df_method_ID,df_method_name,df_method_fullName,df_method_type,df_method_desc],axis=1)
me['label']='Method'

#生成package节点文件
#pack.columns = ['index:ID','package','description',':LABEL']
#pack.to_csv('F:/PycharmProjects/API-csv/data/package.csv',index=False, encoding='utf-8')
#print('package导出CSV成功！')

#生成class节点文件
#cl.columns = ['index:ID','class','definition','description',':LABEL']
#cl.to_csv('F:/PycharmProjects/API-csv/data/class.csv',index=False, encoding='utf-8')
#print('class导出CSV成功！')

#生成method节点文件
me.columns = ['index:ID','method','fullName','type','description',':LABEL']
me.to_csv('F:/PycharmProjects/API-csv/data/method.csv',index=False, encoding='utf-8')
print('method导出CSV成功！')