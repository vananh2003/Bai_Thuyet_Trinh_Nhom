import pandas
xl = pandas.read_excel('Book1.xlsx')
monan= str(input('Nhập món ăn của bạn: '))
xl_monan= xl['Món ăn']
j=-1
for i in xl_monan:
    j=j+1
    if i == monan:
        h= xl.iloc[j]
        print(h)





