// Inspired by https://codepen.io/sarazond/pen/LYGbwj (saranshsinha)
function animateStars() {
    var retryInterval = setInterval(function () {
        console.log("Trying to animate stars...")
        const areaToStarRatio = 2400;
        var starCount = 1000;
        const canvas = document.getElementById('stars');

        if (canvas) {
            clearInterval(retryInterval)
            const starSizes = [0.4, 0.8, 1.2];
            const starSpeeds = [0.6, 0.4, 0.2];
            const starBlurs = [10, 15, 50];

            function setCanvasSize() {
                canvas.width = window.innerWidth;
                canvas.height = Math.max(document.body.scrollHeight, window.innerHeight);
                starCount = (canvas.width * canvas.height / areaToStarRatio) | 0;
                console.log("Canvas size set " + canvas.width + " x " + canvas.height
                    + ", using " + starCount + " stars");
            }
            const ctx = canvas.getContext('2d');

            class Star {
                constructor() {
                    this.x = Math.random() * canvas.width;
                    this.y = Math.random() * canvas.height;
                    this.index = (Math.random() * 3) | 0;
                    this.size = starSizes[this.index];
                    this.speed = starSpeeds[this.index];
                }
                update() {
                    this.y -= this.speed;
                    if (this.y < 0) {
                        this.y = canvas.height;
                        this.x = Math.random() * canvas.width;
                    }
                }
                draw() {
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.shadowBlur = 5;
                    ctx.shadowColor = "rgba(255, 255, 255, 0.9)";
                    ctx.fillStyle = "rgb(255, 255, 255)";
                    ctx.fill();
                }
            }

            const stars = [];
            function createStars(count) {
                stars.length = 0;
                for (let i = 0; i < count; i++) {
                    stars.push(new Star());
                }
            }

            function animate() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                stars.forEach(star => {
                    star.update();
                    star.draw();
                });
                requestAnimationFrame(animate);
            }

            setCanvasSize();
            createStars(starCount);
            animate();

            // Change parameters on window resize or tab change (body size change)
            const observedElement = document.body;
            const resizeObserver = new ResizeObserver(entries => {
                setCanvasSize();
                createStars(starCount);
            });
            resizeObserver.observe(observedElement);

            console.log("Animation sucessfull for stars.");
        }
    }, 500);
};

animateStars();
