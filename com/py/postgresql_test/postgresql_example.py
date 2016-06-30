#!/usr/bin/python
#coding=utf-8

import psycopg2
import psycopg2.extras

##连接到一个存在的数据库
conn=psycopg2.connect(
        database='crm_analy', user='crm_analy', password='crm_analy', host='10.0.3.36', port=2345)
#connect()也可以使用一个大的字符串参数，比如：“database=crm_analy, user=crm_analy, password=crm_analy, host=10.0.3.36, port=2345”

#打开一个光标，用来执行数据库操作,参数不传入，返回元组形式的结果集 传递参数 以字典形式返回
cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#执行sql时传入参数，无论什么数据类型，要使用占位符%s,传递参数必须以元组的形式提供，
cur.execute("select goods_id,goods_name from public.ymall_goods limit %s;",(100,))
list=cur.fetchone()
print list
#fetchone 返回一条结果，找不到返回null
#fetchall 返回所有结果，找不到返回空list
#fetchmany(100) 每次调用，游标向后移动，返回值如同fetchall

#query属性 是一个只读属性，可以返回上次执行的sql脚本
print list[1].decode('utf-8')
print cur.description[0].name
cur.close()
conn.close()