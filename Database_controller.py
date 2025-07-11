import ProtectedData
import psycopg2
from nicegui import app as nicegui_app


def RunQuery(query: str):
    DB_info = ProtectedData.getDatabaseKey()
    conn = psycopg2.connect(
        database=DB_info["DB_NAME"],
        password=DB_info["DB_PASS"],
        user=DB_info["DB_USER"],
        host=DB_info["DB_HOST"],
        port=DB_info["DB_PORT"],
    )
    print("Connected successfully---")
    # conn = nicegui_app.storage.general.get("db_conn")
    # print(type(conn), "<----")
    print("->{}<-".format(query))
    print("----------------------")
    cur = conn.cursor()
    stage = cur.execute(query)
    try:
        rows = cur.fetchall()
        print(rows)
    except:
        rows = "-No results-"
        # print("Stage:", stage)
        # input()
    finally:
        cur.close()
        conn.commit()
        conn.close()
        return rows


def RevenueOfProduct(StartTime="CURRENT_DATE", EndTime="CURRENT_DATE"):
    if StartTime != "CURRENT_DATE":
        StartTime = "'" + StartTime + "'"
    if StartTime == "":
        StartTime = "CURRENT_DATE"
    if EndTime != "CURRENT_DATE":
        EndTime = "'" + EndTime + "'"
    #     rows = RunQuery(
    #         """
    # SELECT name,TotalQuantity*price AS Revenue
    # FROM store_product AS sp JOIN
    #     (SELECT product_id,SUM(quantity) AS TotalQuantity
    #     FROM orders_orderproduct AS op
    #     WHERE updated_at>={} AND updated_at<={}
    #     GROUP BY product_id
    #     ORDER BY product_id) AS opt
    #     ON sp.id=opt.product_id
    # ORDER BY Revenue DESC
    #                     """.format(
    #             StartTime, EndTime
    #         )
    #     )
    rows = RunQuery(
        """
SELECT name, SUM(quantity)*price AS Revenue
FROM orders_orderproduct AS op
JOIN   orders_orderproduct_variations AS opv 
	ON opv.orderproduct_id= op.id
JOIN store_variation AS ov
	ON opv.variation_id=ov.id
JOIN store_product AS sp 
	ON ov.product_id=sp.id
WHERE op.updated_at>={} AND op.updated_at<= {}
GROUP BY sp.id
ORDER BY Revenue DESC;
                    """.format(
            StartTime, EndTime
        )
    )
    print(rows)
    # rows = (
    #     ("ATX Jeans", 1500000),
    #     ("NEU Jacket", 5000000),
    #     ("HUCE T Shirt", 4000000),
    #     ("UEB Shoes", 7500000),
    #     ("FTU Jacket", 8000000),
    #     ("HUST Shirt", 12000000),
    # )
    Total = sum(i[1] for i in rows)
    Data = list(
        {"value": i[1], "name": i[0] + "({:.2f}%)".format(100 * (i[1] / Total))}
        for i in rows
    )
    return Data


def MonthlyRevenue(StartTime="CURRENT_DATE", EndTime="CURRENT_DATE"):
    if StartTime != "CURRENT_DATE":
        StartTime = "'" + StartTime + "'"
    if StartTime == "":
        StartTime = "CURRENT_DATE"
    if EndTime != "CURRENT_DATE":
        EndTime = "'" + EndTime + "'"
    rows = RunQuery(
        """
SELECT sc.name, time,SUM(ptotal),sc.id
FROM (
SELECT TO_CHAR(op.updated_at,'YYYY-MM') as time,SUM(quantity)*sp.price as ptotal,category_id
FROM store_product AS sp
LEFT JOIN orders_orderproduct AS op ON sp.id=op.product_id
WHERE op.updated_at>={} AND op.updated_at<={}
GROUP BY product_id,time,sp.price,category_id) AS tempt
JOIN store_category AS sc ON tempt.category_id=sc.id
GROUP BY sc.id,time
ORDER BY time ASC
""".format(
            StartTime, EndTime
        )
    )
    # rows = (
    #     ("2025-1", 34000000),
    #     ("2025-2", 40000000),
    #     ("2025-3", 27000000),
    #     ("2025-4", 31234000),
    #     ("2025-5", 36056000),
    #     ("2025-6", 47000000),
    # )
    print(rows)
    Data = {
        "name": "",
        "data": [],
        "type": "line",
        "stack": "Total",
        "areaStyle": {},
        "emphasis": {"focus": "series"},
        # "smooth": "true",
    }
    DataX = []
    Series = []
    Index = {}
    for i in rows:
        if i[3] not in Index:
            Index[i[3]] = [i[0], dict()]
        Index[i[3]][1][i[1]] = i[2]
        if i[1] not in DataX:
            DataX.append(i[1])
    print(DataX)
    print(Index)
    for i in Index:
        Y = Data.copy()
        Y["name"] = Index[i][0]
        Y["data"] = list()
        for j in DataX:
            Y["data"].append(Index[i][1].get(j, 0))
        Series.append(Y.copy())

    # for i in rows:
    #     # i = list(i)
    #     # i[2] = float(i[2])
    #     if i[1] not in DataX:
    #         DataX.append(i[1])
    #     if i[3] not in Index:
    #         Index[i[3]] = len(Series)
    #         Y = Data.copy()
    #         Y["data"] = list()
    #         Y["name"] = i[0]
    #         for j in DataX[:-1]:
    #             if j != i[1]:
    #                 Y["data"].append(0)
    #         Y["data"].append(i[2])
    #         Series.append(Y.copy())
    #     else:
    #         index = Index[i[3]]
    #         for j in DataX[:-1]:
    #             if j != i[1]:
    #                 Series[index]["data"].append(0)
    #         Series[index]["data"].append(i[2])
    # print(Series)
    # for i in Series:
    #     if len(i["data"]) < len(DataX):
    #         i["data"] += [0] * (len(DataX) - len(i["data"]))
    return DataX, Series


def StockOfProduct():
    rows = RunQuery(
        """
SELECT name,stock
FROM store_product
ORDER BY id
"""
    )
    # rows = (
    #     ("ATX Jeans", 34),
    #     ("NEU Jacket", 57),
    #     ("HUCE T Shirt", 60),
    #     ("UEB Shoes", 67),
    #     ("FTU Jacket", 79),
    #     ("HUST Shirt", 98),
    # )
    print(rows)
    DataX = [i[0] for i in rows]
    DataY = [i[1] for i in rows]
    return DataX, DataY


def SoldOfProduct(StartTime="CURRENT_DATE", EndTime="CURRENT_DATE"):
    if StartTime != "CURRENT_DATE":
        StartTime = "'" + StartTime + "'"
    if StartTime == "":
        StartTime = "CURRENT_DATE"
    if EndTime != "CURRENT_DATE":
        EndTime = "'" + EndTime + "'"
    rows = RunQuery(
        """
SELECT SUM(quantity)
FROM orders_orderproduct AS op
WHERE updated_at>={} AND updated_at<={}
GROUP BY product_id
ORDER BY product_id""".format(
            StartTime, EndTime
        )
    )
    DataY = [i[0] for i in rows]
    return DataY
