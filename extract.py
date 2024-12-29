import pandas as pd

def xls_columns_to_csv(xls_file, csv_file, columns):
    """convert Excel file to CSV file with specified columns"""
    data = pd.read_excel(xls_file, usecols=columns, engine="xlrd")
    data = data.dropna()
    data.columns = ['Student No.', 'Name', 'Email']
    data.to_csv(csv_file, index=False)

csv_file_path = "data/mailing_list.csv"

is_Chinese = True

if __name__ == "__main__":
    # download the Excel file from Web Learning
    if is_Chinese:
        xls_file_path = "data/学生信息.xls"
        columns_to_extract = ["学号", "姓名", "电子邮件"]
    else:
        xls_file_path = "data/Students.xls"
        columns_to_extract = ["Student No.", "Name", "Email"]

    xls_columns_to_csv(xls_file_path, csv_file_path, columns_to_extract)