from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd
import seaborn as sns
import numpy as np
import os
sns.set_theme()
from sklearn import linear_model


# import data
from os import listdir
from sklearn import linear_model

province_dict = {
    '北京市': 'Beijing',
    '天津市': 'Tianjin',
    '河北省': 'Hebei',
    '山西省': 'Shanxi',
    '内蒙古自治区': 'Inner Mongolia',
    '辽宁省': 'Liaoning',
    '吉林省': 'Jilin',
    '黑龙江省': 'Heilongjiang',
    '上海市': 'Shanghai',
    '江苏省': 'Jiangsu',
    '浙江省': 'Zhejiang',
    '安徽省': 'Anhui',
    '福建省': 'Fujian',
    '江西省': 'Jiangxi',
    '山东省': 'Shandong',
    '河南省': 'Henan',
    '湖北省': 'Hubei',
    '湖南省': 'Hunan',
    '广东省': 'Guangdong',
    '广西壮族自治区': 'Guangxi',
    '海南省': 'Hainan',
    '重庆市': 'Chongqing',
    '四川省': 'Sichuan',
    '贵州省': 'Guizhou',
    '云南省': 'Yunnan',
    '西藏自治区': 'Tibet',
    '陕西省': 'Shaanxi',
    '甘肃省': 'Gansu',
    '青海省': 'Qinghai',
    '宁夏回族自治区': 'Ningxia',
    '新疆维吾尔自治区': 'Xinjiang',
    '台湾省': 'Taiwan',
    '香港特别行政区': 'Hong Kong',
    '澳门特别行政区': 'Macao'
}

path="./region/"
alpha = 0.7
w = 0.7
tax= 0.32
ratio=(tax+1)*(0.25*1.08+0.5*(1.08**-1+1.05**1)+0.25*(1.08**-2+1.05**2))

r0=(0.7+0.25+0.05)*800
ret=0


names=os.listdir(path)

store=[]

j=0

for name in names:
    # investment

    origin=pd.read_csv(path+name)

    alpha = 0.5
    w = 0.5
    tax= 0.32

    ratio=(tax+1)*(0.25*1.08+0.5*(1.08**-1+1.05**1)+0.25*(1.08**-2+1.05**2))

    df=pd.DataFrame()
    df["K"]=origin["new_product_fund"]+w*origin["st_fund"]
    df["L"]=(origin["st_people"]+origin["tech_job"])*origin["wage_tech"]*ratio
    df["I"]=(np.exp(alpha*np.log(df["K"]))+(1-alpha)*np.log(df["L"]))
    df["out_sci"]=origin["invention_granted"]
    df["out_cap"]=origin["new_product_sales_revenue"]
    df["env_market"]=origin["tech_market_turnover"]
    df["env_gdp"]=origin["GDP"]
    df["stable_index"]=origin["财政收入稳健指数"]
    df["epu"]=origin["EPU"]
    df.set_index(origin["Year"],inplace=True)

    # nan
    df.drop(range(2004,2008), inplace=True)

    l=[0,2,4]
    for i in l:
        df.iloc[2,i]=(df.iloc[1,i]+df.iloc[3,i])/2

    df.drop(["K","L"],axis=1,inplace=True)

    for t in range(1,16):
        rt=r0*np.exp(-0.15*t)
        ret+=rt

    df["out_sci"]=df["out_sci"]*ret

    # df["stable_index"]=np.log(df["stable_index"])
    # df["epu"]=np.log(df["epu"])
    # df["env_gdp"]=np.log(df["env_gdp"])
    # df["env_market"]=np.log(df["env_market"])
    df["out_cap"]=np.log(df["out_cap"])
    df["out_sci"]=np.log(df["out_sci"])

    # time window

    # Convolution

    df_sale=pd.DataFrame()
    df_research=pd.DataFrame()
    df_sale=df.copy().drop("out_sci",axis=1)
    df_research=df.copy().drop(["I","out_cap"],axis=1)
    df_research.drop(index=[2008,2009,2010],inplace=True)
    df_research["I"]=df["I"].drop(index=[2022,2021,2008]).values*0.15+df["I"].drop(index=[2022,2008,2009]).values*0.15+df["I"].drop(index=[2008,2009,2010]).values*0.7

    reg_sale=linear_model.LinearRegression()
    X_sale=df_sale[["I","env_market","env_gdp","stable_index","epu"]]
    X_sale=X_sale.fillna(0)
    df_sale=df_sale.fillna(0)

    reg_sale.fit(X_sale,df_sale["out_cap"].to_numpy().reshape(-1,1))
    # print(f"Capital coeff: {reg_sale.coef_}")
    # print(f"Capital intercept: {reg_sale.intercept_}")

    reg_research=linear_model.LinearRegression()
    X_research=df_research[["I","env_market","env_gdp","stable_index","epu"]]
    X_research=X_research.fillna(0)
    df_research=df_research.fillna(0)
    reg_research.fit(X_research,df_research["out_sci"].to_numpy().reshape(-1,1))
    # print(f"Research coeff: {reg_research.coef_}")
    # print(f"Research intercept: {reg_research.intercept_}")

    store.append((province_dict[name[:-4]],reg_sale.coef_[0][0]+0.7*reg_research.coef_[0][0]))

print(store)

map_chart = (
    Map()
    .add("Heat Map", store, "china",name_map=province_dict,is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="China Map"),
        visualmap_opts=opts.VisualMapOpts(max_=5),
    )
)

# 渲染地图
map_chart.render("china_map.html")
