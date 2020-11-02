import xlrd
import xlwt

file = '/root/spider/WeiboSpider/weibospider/output/relationships.xls'
data = xlrd.open_workbook(file)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

print(nrows, ncols)

workbook = xlwt.Workbook(encoding='utf-8')
news_sheet = workbook.add_sheet('select')
news_sheet.write(0, 0, '_id')
news_sheet.write(0, 1, 'fan_id')
news_sheet.write(0, 2, 'followed_id')

rank_list = []
for i in range(1, nrows):
	for j in range(1,nrows):
		if table.row_values(i)[3] == table.row_values(j)[4]:
			if table.row_values(i)[4] == table.row_values(j)[3]:
				rank_list.append(i)
		continue
print(rank_list)
'''			
	if table.row_values(i)[-1] == data:
		print(table.row_values(i)[-1])
		print(i)
		rank_list.append(i)
print(rank_list)

for i in range(len(rank_list)):
	news_sheet.write(i+1, 0, table.row_values(int(rank_list[i]))[0])
	news_sheet.write(i+1, 1, table.row_values(int(rank_list[i]))[1])

workbook.save('%s-网易新闻.xls' %(data))
'''