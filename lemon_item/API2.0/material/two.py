# -*- coding: utf-8 -*-
# @Time :2020/7/17 20:58
# @Author : liufei
# @File :two.PY

s=[{'a':'jfdk${normal_tel}','b':'d4e${loan_id}'},{'a':'dfaudg43${member_id}','b':'jdfdor${admin_tel}'}]
for item in s:
    if item['a'].find('${normal_tel}')!=-1:
        b=item['a'].replace('${normal_tel}','liufei')
        print(b)
        print(item)
    elif item['a'].find('${member_id}')!=-1:
        a=item['a'].replace('${member_id}','liufei')
        print(a)
        print(item)

# print(s)
# for x in s:
#     print(x['a'])