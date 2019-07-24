venv:
	python3 -m venv venv --clear
	venv/bin/pip install --requirement requirements.txt

style: venv
	pygmentize -f html -a .highlight -S colorful > theme/fmind/static/styles/pygment.css

serve: venv
	venv/bin/pelican --verbose --listen --autoreload --relative-urls --output local content

build: venv
	venv/bin/pelican --verbose --ignore-cache --delete-output-directory --output output content

deploy: build
	git add output && git commit -m "RELEASE" && git subtree push --prefix output origin master
