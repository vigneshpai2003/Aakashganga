blog_count=0
import os
cur_dir = str(os.getcwd()) 
new_dir = cur_dir + r"\templates"
for filename in os.listdir(new_dir):
	if filename.startswith('blog'):  # not to remove other images
		blog_count+=1


