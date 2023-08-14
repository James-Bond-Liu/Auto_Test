import pandas as pd
sheet_names = pd.ExcelFile(r'./test_data.xlsx')
print(sheet_names.sheet_names)
test_data=[]
for sheet in sheet_names.sheet_names:
    file = pd.read_excel(r'./test_data.xlsx', sheet_name=sheet, header=0)
    rows = file.index.values
    for i in rows:
        data = file.loc[i, ['case_id', 'url', 'data', 'title', 'http_method', 'expected', 'result', 'test_result']].to_dict()
        test_data.append(data)
print(test_data)



