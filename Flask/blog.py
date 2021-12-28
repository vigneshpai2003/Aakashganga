from flask import *
from __main__ import app

import config


@app.route('/blog/<blogid>',methods=['GET','POST'])
def blog_post1(blogid):
	
	template_name = "blog"+str(blogid)+".html"
	
	from openpyxl import load_workbook
	
	wb_name= "Comment_DB.xlsx"
	wb = load_workbook(wb_name)
	page = wb.active
	
	comments_to_show = []
	for row in page.rows:
		#print(row[0].value)
		if row[0].value==str(blogid):
			comments_to_show.append([row[1].value,row[2].value])
	#print(comments_to_show)
	
	if request.method=="POST":
		
		data = dict(request.form)  #Data is {'name': 'Deepika', 'comment': 'sup'}
		#print("Data is",data)
		
# New data to write:
		info = [blogid,data['name'],data['comment']]
		page.append(info)
		
		wb.save(filename=wb_name)
		
		comments_to_show = []
		for row in page.rows:
			#print(row[0].value)
			if row[0].value==str(blogid):
				comments_to_show.append([row[1].value,row[2].value])
		return render_template(template_name, data=comments_to_show, max_blog_no=config.blog_count, cur_blog_no = blogid)
			
			
	return render_template(template_name, data=comments_to_show, max_blog_no=config.blog_count, cur_blog_no = blogid)
	
	
