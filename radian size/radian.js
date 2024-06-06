const canvas = document.getElementById('circleCanvas');
const ctx = canvas.getContext('2d');
const radius = 150;

function drawCircle() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    ctx.arc(canvas.width / 2, canvas.height / 2, radius, 0, 2 * Math.PI);
    ctx.stroke();
}

function drawAngle() {
    const degrees = document.getElementById('angleInput').value;
    if (degrees < 0 || degrees > 360 || isNaN(degrees)) {
        alert('Please enter a valid angle between 0 and 360 degrees.');
        return;
    }
    const radians = degrees * (Math.PI / 180);

    drawCircle();
    ctx.beginPath();
    ctx.moveTo(canvas.width / 2, canvas.height / 2);
    ctx.lineTo(canvas.width / 2 + radius * Math.cos(0), canvas.height / 2 + radius * Math.sin(0));
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(canvas.width / 2, canvas.height / 2);
    ctx.lineTo(canvas.width / 2 + radius * Math.cos(radians), canvas.height / 2 + radius * Math.sin(radians));
    ctx.stroke();
    
    ctx.font = '16px Arial';
    ctx.fillText(`${degrees} degrees = ${radians.toFixed(2)} radians`, 10, canvas.height - 10);
}

drawCircle();