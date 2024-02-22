from connection import conn, db, division

# select all the columns from the division table
query = division.select()
another_query = db.select(division)

# use the connection object to extract the first five rows
exe = conn.execute(query)  # executing query
result = exe.fetchmany(5)  # extracting the top 5 results


if __name__ == "__main__":
    print("##### Query One ######", query)
    print("##### Query Two #####", another_query)
    print("##### Top 5 results #####", result)
