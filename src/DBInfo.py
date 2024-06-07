
from pymilvus import connections, db

conn = connections.connect(host="192.168.10.10", port=19530, token="root:Milvus")
dataList = db.list_database()
print(dataList)