document.addEventListener("DOMContentLoaded", () => {
    const robot = document.getElementById("robot");
    if (!robot) return;

    const frameHeight = 250;
    const totalFrames = 4;
    let frame = 0;

    setInterval(() => {
        robot.style.backgroundPosition = `0px -${frame * frameHeight}px`;
        frame = (frame + 1) % totalFrames;
    }, 300);
});
