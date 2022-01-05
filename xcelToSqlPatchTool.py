from openpyxl import load_workbook

class MetaData:
    def __init__(self, wb, sh, colNamesRowNum, fromRange, to, procedureName) -> None:
        self.wb = wb
        self.sh = sh
        self.colNamesRowNum = colNamesRowNum
        self.fromRange = fromRange
        self.to = to
        self.procedureName = procedureName

obj = MetaData("WorkbookName", "SheetName", "RowNum of Your Column names", "DataStartRange", "DataEndRange", "ProcedureName")

wb = load_workbook(obj.wb)
sh = wb[obj.sh]

def complete():
    colHeaderList = [cell.value for cell in sh[obj.colNamesRowNum]]
    dataList = [list(x) for x in sh[obj.fromRange : obj.to]]
    i = 0
    mainStr = ""
    for val in dataList:
        if i == len(colHeaderList):
            i = 0
        s = f"""GO\nEXEC {obj.procedureName}\n"""
        for x in val:
            if isinstance(x.value, str):
                s += f"""@{colHeaderList[i]} = '{x.value}'\n"""
            else:
                if str(x.value).split('.')[1] == '0':
                    s += f"""@{colHeaderList[i]} = {str(x.value).split('.')[0]}\n"""
                else:
                    s += f"""@{colHeaderList[i]} = {x.value}\n"""
            i += 1
        mainStr += s + "\n"
    with open('patch.sql', 'w') as f:
        f.write(mainStr)
complete()