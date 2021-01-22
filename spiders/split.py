import csv
import os


def split_csv(path, total_len, per):

    with open(path, 'r', newline='') as file:
        csvreader = csv.reader(file)
        i = 0
        for row in csvreader:

            if i < round(total_len * per/100):
                # train.csv存放路径
                csv_path = os.path.join("F:/PycharmProjects/API-csv/data", 'class_to_method5.csv')
                print(csv_path)
                # 不存在此文件的时候，就创建
                if not os.path.exists(csv_path):
                    with open(csv_path, 'w', newline='') as file:
                        csvwriter = csv.writer(file)
                        csvwriter.writerow(row)
                    i += 1
                # 存在的时候就往里面添加
                else:
                    with open(csv_path, 'a', newline='') as file:
                        csvwriter = csv.writer(file)
                        csvwriter.writerow(row)
                    i += 1
            elif (i >= round(total_len * per/100)) and (i < total_len):
            	# vali.csv存放路径
                csv_path = os.path.join("F:/PycharmProjects/API-csv/data", 'class_to_method6.csv')
                print(csv_path)
                # 不存在此文件的时候，就创建
                if not os.path.exists(csv_path):
                    with open(csv_path, 'w', newline='') as file:
                        csvwriter = csv.writer(file)
                        csvwriter.writerow(row)
                    i += 1
                # 存在的时候就往里面添加
                else:
                    with open(csv_path, 'a', newline='') as file:
                        csvwriter = csv.writer(file)
                        csvwriter.writerow(row)
                    i += 1
            else:
                break

    print("分割成功")
    return
if __name__ == '__main__':

    path = 'F:/PycharmProjects/API-csv/data/class_to_method2.csv'
    total_len = len(open(path, 'r').readlines())# csv文件行数
    per = 50 # 分割比例%

    split_csv(path, total_len, per)
