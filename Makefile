html:
	python3 app.py &
	sleep 30
	wget --recursive --no-clobber --page-requisites --html-extension --convert-links --no-parent http://127.0.0.1:8080/
	wget -r http://127.0.0.1:8080/_dash-layout
	wget -r http://127.0.0.1:8080/_dash-dependencies

	sed -i 's/_dash-layout/_dash-layout.json/g' 127.0.0.1:8080/_dash-component-suites/dash/dash-renderer/build/*.js 
	sed -i 's/_dash-dependencies/_dash-dependencies.json/g' 127.0.0.1:8080/_dash-component-suites/dash/dash-renderer/build/*.js

	# sed -i '/<head>/ r head.html' 127.0.0.1:8080/index.html
	mv 127.0.0.1:8080/_dash-layout 127.0.0.1:8080/_dash-layout.json	
	mv 127.0.0.1:8080/_dash-dependencies 127.0.0.1:8080/_dash-dependencies.json

	cp thumbnail.png 127.0.0.1:8080/
	cp assets/* 127.0.0.1:8080/assets/
	# cp _static/async* 127.0.0.1:8080/_dash-component-suites/dash/dcc/
	# cp _static/async-table* 127.0.0.1:8080/_dash-component-suites/dash/dash_table/

	ps | grep python | awk '{print $$1}' | xargs kill -9	

clean:
	rm -rf 127.0.0.1:8080/
