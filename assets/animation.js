function animateSquares() {
    var retryInterval = setInterval(function() {
        console.log("Trying to animate squares...")
        var iElements = Array.from(document.getElementsByTagName("i"));

        if (iElements.length > 0 & tabs !== null) {
            clearInterval(retryInterval)
            iElements.forEach(function(element) {
                element.style.position = 'absolute';
                element.style.width = '60px';
                element.style.height = '60px';
                element.style.overflow = 'hidden';
                element.style.background_color = 'transparent';
                element.style.border = '6px solid rgba(255, 255, 255, 0.8)';
                setRandomValues(element);
                element.addEventListener('animationiteration', function() {
                    element.style.visibility = 'hidden';
                    setRandomValues(element);
                    setTimeout(function() {  
                        element.style.visibility = 'visible'; 
                    }, 10);  
                });
            });

            console.log("Animation sucessfull for", iElements.length, "squares.");
            
            function setRandomValues(element) {
                const maxHeight = element.parentElement.offsetHeight;
                const maxWidth = element.parentElement.offsetWidth;
                element.style.top = (Math.random() * maxHeight * 0.9).toFixed(0) + 'px';
                element.style.left = ((Math.random() * maxWidth) - 60).toFixed(0) + 'px';
                var randomDuration = ((Math.random() * 10) + 10).toFixed(0) + 's';
                element.style.animation = 'animate ' + randomDuration + ' linear infinite';
            }
        }
    }, 500);
};

animateSquares();