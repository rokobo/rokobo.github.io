html:
	# Run application for a few seconds
	python3 src/main.py &
	sleep 30

	# Download static version of the Dash app with the following options
	# -r: Recursively download files. It will follow and download all links found in the given URL.
	# -x: Create a hierarchy of directories when retrieving recursively.
	# -m: Mirror, recursive download for all of its elements, including all sub-pages, images, etc.
	# --no-clobber: Prevents overwriting existing files.
	# -p: Downloads all the files that are necessary to properly display a given HTML page.
	# -E: If files don't have a .html extension, this option will save them with a .html extension locally.
	# -k: Will make wget convert the links in the downloaded HTML files to make them suitable for offline viewing.
	# --restrict-file-names=windows: Ensures that filenames will be compatible with Windows filesystem conventions.
	# --no-parent: Does not retrieve files from parent directories.

	wget --no-clobber -x -m -p -E -k --restrict-file-names=windows --no-parent http://127.0.0.1:8080/
	wget -r --restrict-file-names=windows http://127.0.0.1:8080/_dash-layout
	wget -r --restrict-file-names=windows http://127.0.0.1:8080/_dash-dependencies

	# Changes references and renames files
	sed -i 's/_dash-layout/_dash-layout.json/g' 127.0.0.1+8080/_dash-component-suites/dash/dash-renderer/build/*.js 
	sed -i 's/_dash-dependencies/_dash-dependencies.json/g' 127.0.0.1+8080/_dash-component-suites/dash/dash-renderer/build/*.js
	mv 127.0.0.1+8080/_dash-layout 127.0.0.1+8080/_dash-layout.json	
	mv 127.0.0.1+8080/_dash-dependencies 127.0.0.1+8080/_dash-dependencies.json

	# Add additional assets
	touch .nojekyll
	cp -R thumbnail.png 127.0.0.1+8080/
	mkdir -p 127.0.0.1+8080/assets/
	cp -R assets/* 127.0.0.1+8080/assets/

	# Kill python process
	ps | grep python | awk '{print $$1}' | xargs kill -9	

clean:
	# Clean entire directory
	rm -rf 127.0.0.1+8080/
