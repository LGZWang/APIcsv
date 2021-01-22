import pandas as pd


df = pd.read_csv('F:/PycharmProjects/API-csv/data/api-data.csv',encoding='utf-8')
df_package = pd.read_csv('F:/PycharmProjects/API-csv/data/package.csv', encoding='utf-8')
df_class = pd.read_csv('F:/PycharmProjects/API-csv/data/class.csv', encoding='utf-8')
df_method = pd.read_csv('F:/PycharmProjects/API-csv/data/method.csv', encoding='utf-8')

package_classes, class_methods = [],[]

for index, row in df.iterrows():

    package_name = row['package_name']
    class_name = row['class_name']
    method_name = row['method_full_name']

    #methodList, classList, packageList =[], [], []

    packageID = df_package['index:ID'].loc[df_package['package'] == package_name].values[0]
    classID = df_class['index:ID'].loc[df_class['class'] == class_name].values[0]
    package_class = [packageID, classID, 'hasCLass', 'hasClass']
    package_classes.append(package_class)

    methodID = df_method['index:ID'].loc[df_method['fullName'] == method_name].values[0]
    class_method = [classID, methodID, 'hasMethod', 'hasMethod']
    class_methods.append(class_method)


#df_package_class = pd.DataFrame(data=package_classes, columns=[':START_ID',':END_ID','relation',':TYPE'])
#df_package_class = df_package_class.drop_duplicates()
#df_package_class.to_csv('F:/PycharmProjects/API-csv/data/package_to_class.csv', index=False,encoding='utf-8')
#print('package_to_class')

df_class_method = pd.DataFrame(data=class_methods, columns=[':START_ID',':END_ID','relation',':TYPE'])
#df_class_method = df_class_method.drop_duplicates()
df_class_method.to_csv('F:/PycharmProjects/API-csv/data/class_to_method.csv', index=False,encoding='utf-8')
print('class_to_method')


