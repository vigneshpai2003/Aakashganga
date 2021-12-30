from pathlib import Path
import os

blog_count=0

CWD = Path(__file__).parent

TEMPLATE_DIR = CWD / "templates"


for filename in os.listdir(TEMPLATE_DIR):
	if filename.startswith('blog'):  # not to remove other images
		blog_count+=1
