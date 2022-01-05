from openpyxl import load_workbook

class MetaData:
    def __init__(self, wb, sh, colNamesRowNum, fromRange, to, query) -> None:
        self.wb = wb
        self.sh = sh
        self.colNamesRowNum = colNamesRowNum
        self.fromRange = fromRange
        self.to = to
        self.query = query

obj = MetaData("WorkbookName", "SheetName", "RowNum of Your Column names", "DataStartRange", "DataEndRange", "INSERT INTO tblname VALUES")

wb = load_workbook(obj.wb)
sh = wb[obj.sh]

def complete():
    colHeaderList = [cell.value for cell in sh[obj.colNamesRowNum]]
    dataList = [list(x) for x in sh[obj.fromRange : obj.to]]
    i = 0
    mainStr = ""
    for val in dataList:
        s = f"""{obj.query}("""
        for indx, x in enumerate(val):
            if isinstance(x.value, str):
                s += f"""'{x.value}',"""
            else:
                if str(x.value).split('.')[1] == '0':
                    s += f"""{str(x.value).split('.')[0]},"""
                else:
                    s += f"""{x.value},"""
            if indx == len(val) - 1:
                s = s[:-1] +  ")\n"
        mainStr += s + "\n"
    with open('patch.sql', 'w') as f:
        f.write(mainStr)
complete()