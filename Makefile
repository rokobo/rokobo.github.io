html:
	# Run application for a few seconds
	python3 src/app.py &
	sleep 60

	# Download static version of the Dash app with the following options
	# -r: Recursively download files. It will follow and download all links found in the given URL.
	# --no-clobber: Prevents overwriting existing files.
	# --page-requisites: Downloads all the files that are necessary to properly display a given HTML page.
	# --html-extension: If files don't have a .html extension, this option will save them with a .html extension locally.
	# --convert-links: Will make wget convert the links in the downloaded HTML files to make them suitable for offline viewing.
	# --restrict-file-names=windows: Ensures that filenames will be compatible with Windows filesystem conventions.
	# --no-parent: Does not retrieve files from parent directories.

	wget -r --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --no-parent http://127.0.0.1:8080/
	wget -r --restrict-file-names=windows http://127.0.0.1:8080/_dash-layout
	wget -r --restrict-file-names=windows http://127.0.0.1:8080/_dash-dependencies

	# Changes references and renames files
	sed -i 's/_dash-layout/_dash-layout.json/g' 127.0.0.1+8080/_dash-component-suites/dash/dash-renderer/build/*.js 
	sed -i 's/_dash-dependencies/_dash-dependencies.json/g' 127.0.0.1+8080/_dash-component-suites/dash/dash-renderer/build/*.js
	mv 127.0.0.1+8080/_dash-layout 127.0.0.1+8080/_dash-layout.json	
	mv 127.0.0.1+8080/_dash-dependencies 127.0.0.1+8080/_dash-dependencies.json

	# Add additional assets
	touch .nojekyll
	cp thumbnail.png 127.0.0.1+8080/
	mkdir -p 127.0.0.1+8080/assets/
	cp assets/* 127.0.0.1+8080/assets/

	# Kill python process
	ps | grep python | awk '{print $$1}' | xargs kill -9	

clean:
	# Clean entire directory
	rm -rf 127.0.0.1+8080/
