import psycopg2
conn = psycopg2.connect(
    host = "localhost", 
    port ="5432",
    database ="giavang",
    user = "postgres",
    password = "123"
)
def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines

data = read_txt_file('gold_price.txt')

# Lấy chuỗi từ danh sách
data_str = data[0]
# Phân tách chuỗi thành danh sách các giá trị
data_list = data_str.split('##')

# Loại bỏ dấu '%' khỏi giá trị cuối cùng
data_list[-1] = data_list[-1].replace('%', '')
#replace
data_list[0] = data_list[0].replace('.','').replace(',','.')
data_list[1] = data_list[1].replace('.','').replace(',','.')
data_list[2] = data_list[2].replace('.','').replace(',','.')
data_list[3] = data_list[3].replace('.','').replace(',','.')
data_list[4] = data_list[4].replace('.','').replace(',','.')

if len(data_list)==6:
    cur = conn.cursor()
    cur.execute(""" INSERT INTO dulieu.thegioi ("Date", "price", "Open", "high", "low","ChangePercent") VALUES (%s, %s, %s, %s, %s, %s)""",
            (data_list[0],data_list[1],data_list[2],data_list[3],data_list[4],data_list[5]))
    conn.commit()
    print("ok")