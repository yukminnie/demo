# coding=utf-8
import json

text = '''
mtopjsonp4({"api":"mtop.taobao.maserati.personal.works","data":{"context":{},"ok":"true","result":{"data":{"total":"5078","isLast":"false","feeds":[{"cardType":"video","cover":"//img.alicdn.com/imgextra/i3/2830069487/O1CN01nZyijt2Jx682sthoG_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"342"},"id":"294103032257","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=294103032257&source=darenhomepage&type=darenhomepage","whRate":"0.56"},{"cardType":"video","cover":"//img.alicdn.com/imgextra/i4/2830069487/O1CN01XkHXXS2Jx67znRvZq_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"419"},"id":"294394853333","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=294394853333&source=darenhomepage&type=darenhomepage","whRate":"1.0"},{"cardType":"video","cover":"//img.alicdn.com/imgextra/i2/2830069487/O1CN01vvCiqd2Jx6829EEqK_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"354"},"id":"294070356589","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=294070356589&source=darenhomepage&type=darenhomepage","whRate":"1.0"},{"cardType":"video","cover":"//img.alicdn.com/imgextra/i3/2830069487/O1CN01aDNtA32Jx67yYsRxj_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"308"},"id":"294390445600","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=294390445600&source=darenhomepage&type=darenhomepage","whRate":"1.0"},{"cardType":"video","cover":"//img.alicdn.com/imgextra/i2/2830069487/O1CN01hXgc1i2Jx67ziyWrb_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"240"},"id":"294663202317","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=294663202317&source=darenhomepage&type=darenhomepage","whRate":"1.0"},{"cardType":"video","cover":"//img.alicdn.com/imgextra/i1/2830069487/O1CN015bSE8p2Jx683T3GA5_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"385"},"id":"294662318031","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=294662318031&source=darenhomepage&type=darenhomepage","whRate":"1.0"},{"cardType":"normal","cover":"//img.alicdn.com/imgextra/i4/2830069487/O1CN01NqFBvP2Jx682y6EIN_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"386"},"id":"294835627856","top":"false","url":"//scontent.m.taobao.com/detail?pageType=pgc_detail&contentId=294835627856&source=darenhome&sourcePageName=darenhome&disableNav=YES","whRate":"1.0"},{"cardType":"video","cover":"https://img.alicdn.com/imgextra/i3/2830069487/O1CN01tRjTzT2Jx681qV5h9_!!2830069487-2-tmap.png","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"657"},"id":"294851323759","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=294851323759&source=darenhomepage&type=darenhomepage","whRate":"0.56"},{"cardType":"video","cover":"//img.alicdn.com/imgextra/i1/2830069487/O1CN010TYe1l2Jx67xAhcuJ_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"521"},"id":"294279761174","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=294279761174&source=darenhomepage&type=darenhomepage","whRate":"0.56"},{"cardType":"video","cover":"//img.alicdn.com/imgextra/i3/2830069487/O1CN01SU8GOH2Jx687CIuLD_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"575"},"id":"294847507521","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=294847507521&source=darenhomepage&type=darenhomepage","whRate":"0.56"},{"cardType":"video","cover":"//img.alicdn.com/imgextra/i2/2830069487/O1CN01L40cJl2Jx682yS7K9_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"615"},"id":"293942436959","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=293942436959&source=darenhomepage&type=darenhomepage","whRate":"0.56"},{"cardType":"video","cover":"//img.alicdn.com/imgextra/i2/2830069487/O1CN01LDr7WI2Jx67y7t3w7_!!2830069487-0-beehive-scenes.jpg","coverHeight":"0","coverWidth":"0","feedCount":{"viewCount":"336"},"id":"293940420366","top":"false","url":"https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?wh_weex=true&wx_navbar_hidden=true&wx_navbar_transparent=true&id=293940420366&source=darenhomepage&type=darenhomepage","whRate":"0.56"}],"userId":"2830069487"}}},"ret":["SUCCESS::调用成功"],"v":"1.0"})'''

rv = json.loads(text[12:-1])
containList = rv['data']['result']['data']['feeds']
# print(type(containList), containList.values)
# list = [url for url in containList][0].value]
print(containList[0])
# videoList = [{}.format(url) for url in containList.values]
# print('videoList')