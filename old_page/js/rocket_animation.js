const icon = document.querySelector(".icon");
const rectangle = document.querySelector(".container");
let angle = 0;
const speed = 0.01;

function animateIcon() {
  const rectWidth = rectangle.offsetWidth;
  const rectHeight = rectangle.offsetHeight;
  const centerX = rectangle.offsetLeft + rectWidth / 2;
  const centerY = rectangle.offsetTop + rectHeight / 2;
  const radius = Math.min(rectWidth, rectHeight) / 2;
  const x = centerX + radius * Math.cos(angle);
  const y = centerY + radius * Math.sin(angle);
  icon.style.left = x - icon.offsetWidth / 2 + "px";
  icon.style.top = y - icon.offsetHeight / 2 + "px";
  angle += speed;
  requestAnimationFrame(animateIcon);
}

animateIcon();
