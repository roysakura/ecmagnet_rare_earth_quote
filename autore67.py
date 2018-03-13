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

	client = WeChatClient('wx62c42eca1fa1c67d', '8ab2a57cf2b04fbd2fb9a6db66eaee95')
	follow_image = client.media.upload_image(open('follow.gif','r'))
	h1_image = client.media.upload_image(open('h1.gif','r'))
	quote_image = client.media.upload_image(open('quote.png','r'))
	thumb_image = client.media.upload('image',open('xitu.jpg','r'))
	
	 
	articles = []
	
	news_datas = get_news_json()
	i = 0
	for category in [u'稀土',u'稀土',u'稀土',u'磁材',u'磁材']:
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
			r = requests.get(news_datas['data']['detail'][i]['article_thumbnail'],stream=True)
			open('temp.jpg','wb').write(r.content)
			news_thumb_image = client.media.upload('image',open('temp.jpg','r'))
		else:
			news_thumb_image = client.media.upload('image',open('default-thumb.jpg','r'))
		article['thumb_media_id'] = news_thumb_image['media_id']
		article['title'] = news_datas['data']['detail'][i]['article_title']
		article['digest'] =  news_datas['data']['detail'][i]['article_abstract']
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

	article_data = client.media.upload_articles(articles)

	print client.message.send_mass_article(None,article_data['media_id'],True)

if __name__ == "__main__":
	auto_gen_quote_pic()




