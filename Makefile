html:
	python3 app.py &
	sleep 60
	wget -r --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --no-parent http://127.0.0.1:8080/
	wget -r --restrict-file-names=windows http://127.0.0.1:8080/_dash-layout
	wget -r --restrict-file-names=windows http://127.0.0.1:8080/_dash-dependencies

	sed -i 's/_dash-layout/_dash-layout.json/g' 127.0.0.1+8080/_dash-component-suites/dash/dash-renderer/build/*.js 
	sed -i 's/_dash-dependencies/_dash-dependencies.json/g' 127.0.0.1+8080/_dash-component-suites/dash/dash-renderer/build/*.js

	mv 127.0.0.1+8080/_dash-layout 127.0.0.1+8080/_dash-layout.json	
	mv 127.0.0.1+8080/_dash-dependencies 127.0.0.1+8080/_dash-dependencies.json

	cp thumbnail.png 127.0.0.1+8080/
	cp assets/* 127.0.0.1+8080/assets/

	ps | grep python | awk '{print $$1}' | xargs kill -9	

clean:
	rm -rf 127.0.0.1+8080/
