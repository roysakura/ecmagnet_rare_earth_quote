# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw,ImageFont
import requests
import json
from datetime import datetime, timedelta
import os
import lxml.html as LH

from wechatpy import WeChatClient

def get_quote_json(date):
	url = 'http://www.ecmagnet.com/magnet/materialquoteexact/?quote_date=%s' % date.strftime('%Y-%m-%d')
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
	r = requests.get(url,headers=headers)
	data = json.loads(r.text)

	return data['data']['detail']

def get_news_json():
	url = 'http://www.ecmagnet.com/api1.0/newsmaterial/'
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
	r = requests.get(url,headers=headers)
	data = json.loads(r.text)

	return data

def auto_gen_quote_pic():
	ttfont = ImageFont.truetype("hwfs.ttf",30)
	ttfont_title = ImageFont.truetype("hwfs.ttf",30)
	date = datetime.today()

	mc_current,mq_last = [],[]
	current,last = None,None

	while mc_current==[]:
		mc_current = get_quote_json(date)
		if mc_current!=[]:
			current = date
		date = date - timedelta(days=1)
	while mq_last==[]:	
		mq_last = get_quote_json(date)
		if mq_last!=[]:
			last = date
		#print mq_last
		date = date - timedelta(days=1)

	im = Image.open("re_template.png")
	#im_nv = Image.open("nvfeb.png")
	draw = ImageDraw.Draw(im)
	#draw_nv = ImageDraw.Draw(im_nv)

	r0_l, r0_c = '',''
	r1_l, r1_c = '',''
	r2_l, r2_c = '',''
	r3_l, r3_c = '',''
	r4_l, r4_c = '',''
	r5_l, r5_c = '',''
	r6_l, r6_c = '',''
	r7_l, r7_c = '',''
	r8_l, r8_c = '',''
	r9_l, r9_c = '',''
	r10_l, r10_c = '',''
	r11_l, r11_c = '',''
	r12_l, r12_c = '',''
	r13_l, r13_c = '',''
	r14_l, r14_c = '',''
	r15_l, r15_c = '',''
	r16_l, r16_c = '',''
	r17_l, r17_c = '',''
	r18_l, r18_c = '',''
	r19_l, r19_c = '',''

	r20_l, r20_c = '',''
	r21_l, r21_c = '',''
	r22_l, r22_c = '',''
	r23_l, r23_c = '',''
	r24_l, r24_c = '',''
	r25_l, r25_c = '',''
	r26_l, r26_c = '',''
	r27_l, r27_c = '',''
	r28_l, r28_c = '',''
	r29_l, r29_c = '',''

	r30_l, r30_c = '',''
	r31_l, r31_c = '',''
	r32_l, r32_c = '',''
	r33_l, r33_c = '',''
	r34_l, r34_c = '',''
	r35_l, r35_c = '',''
	r36_l, r36_c = '',''
	r37_l, r37_c = '',''
	r38_l, r38_c = '',''
	r39_l, r39_c = '',''

	r40_l, r40_c = '',''


	draw.text((308,0),current.strftime('%m-%d'),fill=(255,255,255),font=ttfont_title)
	draw.text((442,40),last.strftime('%m-%d'),fill=(0,0,0),font=ttfont_title)
	draw.text((617,40),current.strftime('%m-%d'),fill=(0,0,0),font=ttfont_title)

	draw.text((515,40),u'报价',fill=(0,0,0),font=ttfont_title)
	draw.text((690,40),u'报价',fill=(0,0,0),font=ttfont_title)

	for m in mq_last:
		if m['name'] == u'氧化镨钕':
			r0_l = int(m['avg_quote'])
			draw.text((445,80),str(r0_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'镨钕金属':
			r1_l = int(m['avg_quote'])
			draw.text((445,116),str(r1_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化镧':
			r2_l = int(m['avg_quote'])
			draw.text((445,156),str(r2_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属镧':
			r3_l = int(m['avg_quote'])
			draw.text((445,196),str(r3_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化铈':
			r4_l = int(m['avg_quote'])
			draw.text((445,235),str(r4_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属铈':
			r5_l = int(m['avg_quote'])
			draw.text((445,270),str(r5_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化铽':
			r6_l = int(m['avg_quote'])
			draw.text((445,308),str(r6_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属铽':
			r7_l = int(m['avg_quote'])
			draw.text((445,348),str(r7_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化镝' and r8_l == '':
			r8_l = int(m['avg_quote'])
			draw.text((445,385),str(r8_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属镝':
			r9_l = int(m['avg_quote'])
			draw.text((445,425),str(r9_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'镧铈金属':
			r10_l = int(m['avg_quote'])
			draw.text((445,462),str(r10_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化镨':
			r11_l = int(m['avg_quote'])
			draw.text((445,500),str(r11_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属镨' and r12_l == '':
			r12_l = int(m['avg_quote'])
			draw.text((445,538),str(r12_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化钕':
			r13_l = int(m['avg_quote'])
			draw.text((445,575),str(r13_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属钕':
			r14_l = int(m['avg_quote'])
			draw.text((445,610),str(r14_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化钐':
			r15_l = int(m['avg_quote'])
			draw.text((445,648),str(r15_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属钐':
			r16_l = int(m['avg_quote'])
			draw.text((445,685),str(r16_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'钆铁':
			r17_l = int(m['avg_quote'])
			draw.text((445,723),str(r17_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'镝铁' and r18_l =='':
			r18_l = int(m['avg_quote'])
			draw.text((445,760),str(r18_l),fill=(0,0,0),font=ttfont)
		



	for m in mc_current:
		if m['name'] == u'氧化镨钕':
			r0_c = int(m['avg_quote'])
			draw.text((620,80),str(r0_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'镨钕金属':
			r1_c = int(m['avg_quote'])
			draw.text((620,116),str(r1_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化镧':
			r2_c = int(m['avg_quote'])
			draw.text((620,156),str(r2_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属镧':
			r3_c = int(m['avg_quote'])
			draw.text((620,196),str(r3_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化铈':
			r4_c = int(m['avg_quote'])
			draw.text((620,235),str(r4_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属铈':
			r5_c = int(m['avg_quote'])
			draw.text((620,270),str(r5_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化铽':
			r6_c = int(m['avg_quote'])
			draw.text((620,308),str(r6_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属铽':
			r7_c = int(m['avg_quote'])
			draw.text((620,348),str(r7_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化镝' and r8_c == '':
			r8_c = int(m['avg_quote'])
			draw.text((620,385),str(r8_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属镝':
			r9_c = int(m['avg_quote'])
			draw.text((620,425),str(r9_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'镧铈金属':
			r10_c = int(m['avg_quote'])
			draw.text((620,462),str(r10_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化镨':
			r11_c = int(m['avg_quote'])
			draw.text((620,500),str(r11_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属镨' and r12_c=='':
			r12_c = int(m['avg_quote'])
			draw.text((620,538),str(r12_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化钕':
			r13_c = int(m['avg_quote'])
			draw.text((620,575),str(r13_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属钕':
			r14_c = int(m['avg_quote'])
			draw.text((620,610),str(r14_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'氧化钐':
			r15_c = int(m['avg_quote'])
			draw.text((620,648),str(r15_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'金属钐':
			r16_c = int(m['avg_quote'])
			draw.text((620,685),str(r16_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'钆铁':
			r17_c = int(m['avg_quote'])
			draw.text((620,723),str(r17_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'镝铁' and r18_c=='':
			r18_c = int(m['avg_quote'])
			draw.text((620,760),str(r18_c),fill=(0,0,0),font=ttfont)
		

	diff = '-' if r0_c-r0_l==0 else r0_c-r0_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,80),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r1_c-r1_l==0 else r1_c-r1_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,116),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r2_c-r2_l==0 else r2_c-r2_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,156),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r3_c-r3_l==0 else r3_c-r3_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,196),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r4_c-r4_l==0 else r4_c-r4_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,235),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r5_c-r5_l==0 else r5_c-r5_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,270),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r6_c-r6_l==0 else r6_c-r6_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,308),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r7_c-r7_l==0 else r7_c-r7_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,348),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r8_c-r8_l==0 else r8_c-r8_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,385),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r9_c-r9_l==0 else r9_c-r9_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,425),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r10_c-r10_l==0 else r10_c-r10_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,462),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r11_c-r11_l==0 else r11_c-r11_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,500),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r12_c-r12_l==0 else r12_c-r12_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,538),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r13_c-r13_l==0 else r13_c-r13_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,575),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r14_c-r14_l==0 else r14_c-r14_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,610),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r15_c-r15_l==0 else r15_c-r15_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,648),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r16_c-r16_l==0 else r16_c-r16_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,685),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r17_c-r17_l==0 else r17_c-r17_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,723),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r18_c-r18_l==0 else r18_c-r18_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw.text((780,760),str(diff),fill=fill_c,font=ttfont)

	save_filename = u'xt.png'
	im.save(save_filename)

	client = WeChatClient('wx62c42eca1fa1c67d', '8ab2a57cf2b04fbd2fb9a6db66eaee95')
	xtimage = client.media.upload_image(open((save_filename),'r'))
	follow_image = client.media.upload_image(open('follow.gif','r'))
	h1_image = client.media.upload_image(open('h1.gif','r'))
	quote_image = client.media.upload_image(open('quote.png','r'))
	thumb_image = client.media.upload('image',open('xitu.jpg','r'))
	
	articles = []
	
	news_datas = get_news_json()
	i = 0
	for category in [u'磁材',u'磁材',u'永磁']:
		article = {}
		keywords = news_datas['data']['detail'][i]['article_keywords']
		while keywords.find(category) == -1:
			i+=1
			if i==10:
				break
			keywords = news_datas['data']['detail'][i]['article_keywords']
		if i==10:
			i=0
			continue

		if len(news_datas['data']['detail'][i]['article_thumbnail']) > 0:
			print news_datas['data']['detail'][i]['article_thumbnail']
			r = requests.get(news_datas['data']['detail'][i]['article_thumbnail'],stream=True)
			open('temp.jpg','wb').write(r.content)
			news_thumb_image = client.media.upload('image',open('temp.jpg','r'))
		else:
			news_thumb_image = client.media.upload('image',open('default-thumb.jpg','r'))

		article['thumb_media_id'] = news_thumb_image['media_id']
		article['title'] = news_datas['data']['detail'][i]['article_title']
		article['digest'] =  news_datas['data']['detail'][i]['article_abstract'][:100]
		article['show_cover_pic'] = 0
		header = '<section style="border: 0px none;"><p style="width:100%; text-align:center;"><img style="width:80%;" src="{0}" data-width="80%"/></p>'.format(follow_image)
		body = news_datas['data']['detail'][i]['article_content']

		doc = LH.fromstring(body)
		images = doc.xpath('//img/@src')
		for image in images:
			r = requests.get(image,stream=True)
			open('temp.jpg','wb').write(r.content)
			temp_image = client.media.upload_image(open('temp.jpg','r'))
			body = body.replace(image,temp_image)


		body = body.replace('<p>','<p style="margin-left: 10px; margin-right: 10px; margin-top: 25px;"><span style="font-family: arial, helvetica, sans-serif; color: #3F3F3F;">')
		body = body.replace('</p>','</span></p>')
		body = body.replace('<h1>',u'<section class="_135editor" data-tools="135编辑器" data-id="91641" style="border: 0px none;"> <section style="width:100%; text-align:center; margin-top:10px;" data-width="100%"> <section style="display:inline-block;"> <section style="width:100%; display:flex; display:-webkit-flex;" data-width="100%"> <section style="width:35px; background-color:#fefefe; margin-right:-35px; margin-top:-10px;"> <section style="width:30px;"> <img style="vertical-align:middle; width:100%;" src="{0}" data-width="100%"/> </section> </section> <section style="width:100%;" data-width="100%"> <section style="padding-left:35px;"> <section style="width:100%; height:10px; border-top:solid 3px #333; border-right:solid 3px #333;" data-width="100%"></section> </section> </section> </section> <section style="padding:0px 30px; margin-top:-11px;" class="135brush" data-brushtype="text">'.format(h1_image))
		body = body.replace('</h1>',u'</section> <section style="display:flex; display:-webkiy-flex; margin-top:-5px; margin-left:10px;"> <section style="width:100%;" data-width="100%"> <section style="height:10px; border-bottom:solid 3px #333; border-left:solid 3px #333;"></section> </section> <section style="width:30px; margin-left:-30px; background-color:#fefefe;margin-top: -3px;"> <section style="width:30px; height:10px; margin-top:10px; border-left:solid 3px #333;"></section> </section> </section> </section> </section></section><p> <br/></p>')

		footer = u'<section class="layout" style="margin:15px auto;"><section style="width:100%;margin-bottom: -30px;text-align:center;" data-width="100%"><section style="width: 64px;height: 64px;background:#fefefe;border-radius: 50%;margin-right: auto;margin-left: auto;display: inline-block;"><section data-role="width" style="display:inline-block;width:32px"><img class="assistant" style="margin: 18px 0px 0px;width: 32px !important;" src="{0}" width="2rem" height="" border="0" mapurl="" title="" alt=""/></section></section></section><section class="135brush" style="font-size:14px;color:#b0b0b1;padding:30px 30px;background-color:#f2f4f5;border-radius:10px;margin-top: -16px;"><p>来源: {1}</p></section></section>'.format(quote_image,news_datas['data']['detail'][i]['article_author'])
		content = header + body + footer
		article['content'] = content
		
		articles.append(article)
		i+=1

	article = {}
	content = u'<section style="border: 0px none;"><p style="width:100%; text-align:center;"><img style="width:80%;" src="{0}" data-width="80%"/></p><p style="width: 100%;"><span style="caret-color: red; white-space: pre-wrap;"></span><img src="{1}" alt="xitu.png" style="caret-color: red; white-space: pre-wrap;"/><span style="caret-color: red; white-space: pre-wrap"></span></p><p style="width: 100%"><br/></p><p style="width: 100%">价格如图</p></section>'.format(follow_image,xtimage)
	article['thumb_media_id'] = thumb_image['media_id']
	article['title'] = u'%s月%s日,稀土报价' % (current.strftime('%m'),current.strftime('%d'))
	article['content'] = content
	article['digest'] = u'价格上涨,点开查看' if r0_c-r0_l >0 else u'点开查看'
	article['show_cover_pic'] = 0

	articles.append(article)
	article_data = client.media.upload_articles(articles)

	print client.message.send_mass_article(None,article_data['media_id'],True)

if __name__ == "__main__":
	auto_gen_quote_pic()


'''
elif m['name'] == u'N38':
			r20_l = int(m['avg_quote'])
			draw_nv.text((645,105),str(r20_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N40':
			r21_l = int(m['avg_quote'])
			draw_nv.text((645,130),str(r21_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N42':
			r22_l = int(m['avg_quote'])
			draw_nv.text((645,155),str(r22_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N45':
			r23_l = int(m['avg_quote'])
			draw_nv.text((645,180),str(r23_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N48':
			r24_l = int(m['avg_quote'])
			draw_nv.text((645,205),str(r24_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N50':
			r25_l = int(m['avg_quote'])
			draw_nv.text((645,230),str(r25_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N35M':
			r26_l = int(m['avg_quote'])
			draw_nv.text((645,255),str(r26_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N38M':
			r27_l = int(m['avg_quote'])
			draw_nv.text((645,280),str(r27_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N40M':
			r28_l = int(m['avg_quote'])
			draw_nv.text((645,305),str(r28_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N42M':
			r29_l = int(m['avg_quote'])
			draw_nv.text((645,330),str(r29_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N45M':
			r30_l = int(m['avg_quote'])
			draw_nv.text((645,355),str(r30_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N48M':
			r31_l = int(m['avg_quote'])
			draw_nv.text((645,380),str(r31_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N50M':
			r32_l = int(m['avg_quote'])
			draw_nv.text((645,405),str(r32_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N35H':
			r33_l = int(m['avg_quote'])
			draw_nv.text((645,430),str(r33_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N38H':
			r34_l = int(m['avg_quote'])
			draw_nv.text((645,455),str(r34_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N40H':
			r35_l = int(m['avg_quote'])
			draw_nv.text((645,480),str(r35_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N42H':
			r36_l = int(m['avg_quote'])
			draw_nv.text((645,505),str(r36_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N45H':
			r37_l = int(m['avg_quote'])
			draw_nv.text((645,530),str(r37_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N48H':
			r38_l = int(m['avg_quote'])
			draw_nv.text((645,550),str(r38_l),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N50H':
			r39_l = int(m['avg_quote'])
			draw_nv.text((645,580),str(r39_l),fill=(0,0,0),font=ttfont)

elif m['name'] == u'N35':
			r19_c = int(m['avg_quote'])
			draw_nv.text((788,80),str(r19_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N38':
			r20_c = int(m['avg_quote'])
			draw_nv.text((788,105),str(r20_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N40':
			r21_c = int(m['avg_quote'])
			draw_nv.text((788,130),str(r21_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N42':
			r22_c = int(m['avg_quote'])
			draw_nv.text((788,155),str(r22_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N45':
			r23_c = int(m['avg_quote'])
			draw_nv.text((788,180),str(r23_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N48':
			r24_c = int(m['avg_quote'])
			draw_nv.text((788,205),str(r24_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N50':
			r25_c = int(m['avg_quote'])
			draw_nv.text((788,230),str(r25_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N35M':
			r26_c = int(m['avg_quote'])
			draw_nv.text((788,255),str(r26_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N38M':
			r27_c = int(m['avg_quote'])
			draw_nv.text((788,280),str(r27_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N40M':
			r28_c = int(m['avg_quote'])
			draw_nv.text((788,305),str(r28_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N42M':
			r29_c = int(m['avg_quote'])
			draw_nv.text((788,330),str(r29_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N45M':
			r30_c = int(m['avg_quote'])
			draw_nv.text((788,355),str(r30_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N48M':
			r31_c = int(m['avg_quote'])
			draw_nv.text((788,380),str(r31_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N50M':
			r32_c = int(m['avg_quote'])
			draw_nv.text((788,405),str(r32_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N35H':
			r33_c = int(m['avg_quote'])
			draw_nv.text((788,430),str(r33_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N38H':
			r34_c = int(m['avg_quote'])
			draw_nv.text((788,455),str(r34_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N40H':
			r35_c = int(m['avg_quote'])
			draw_nv.text((788,480),str(r35_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N42H':
			r36_c = int(m['avg_quote'])
			draw_nv.text((788,505),str(r36_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N45H':
			r37_c = int(m['avg_quote'])
			draw_nv.text((788,530),str(r37_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N48H':
			r38_c = int(m['avg_quote'])
			draw_nv.text((788,550),str(r38_c),fill=(0,0,0),font=ttfont)
		elif m['name'] == u'N50H':
			r39_c = int(m['avg_quote'])
			draw_nv.text((788,580),str(r39_c),fill=(0,0,0),font=ttfont)

diff = '-' if r19_c-r19_l==0 else r19_c-r19_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,80),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r20_c-r20_l==0 else r20_c-r20_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,105),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r21_c-r21_l==0 else r21_c-r21_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,130),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r22_c-r22_l==0 else r22_c-r22_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,155),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r23_c-r23_l==0 else r23_c-r23_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,180),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r24_c-r24_l==0 else r24_c-r24_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,205),str(diff),fill=fill_c,font=ttfont)


	diff = '-' if r25_c-r25_l==0 else r25_c-r25_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,230),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r26_c-r26_l==0 else r26_c-r26_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,255),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r27_c-r27_l==0 else r27_c-r27_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,280),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r28_c-r28_l==0 else r28_c-r28_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,305),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r29_c-r29_l==0 else r29_c-r29_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,330),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r30_c-r30_l==0 else r30_c-r30_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,355),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r31_c-r31_l==0 else r31_c-r31_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,380),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r32_c-r32_l==0 else r32_c-r32_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,405),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r33_c-r33_l==0 else r33_c-r33_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,430),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r34_c-r34_l==0 else r34_c-r34_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,455),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r35_c-r35_l==0 else r35_c-r35_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,480),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r36_c-r36_l==0 else r36_c-r36_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,505),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r37_c-r37_l==0 else r37_c-r37_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,530),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r38_c-r38_l==0 else r38_c-r38_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,555),str(diff),fill=fill_c,font=ttfont)

	diff = '-' if r39_c-r39_l==0 else r39_c-r39_l
	fill_c = (255,0,0) if diff>=0 else (22,163,43)
	draw_nv.text((938,570),str(diff),fill=fill_c,font=ttfont)

'''

