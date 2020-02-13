
const showFrame = (num) => {
    const imgs = $("#images img");
    imgs.hide();
    $("#frame-num").text(num);
    $(`#images img:eq(${num})`).show();
};

$(document).ready(() => {
    showFrame(0);
    const frameCount = $("#images img").length;
    let frame = 0;
    $("#left").click(() => {
        frame--;
        if (frame < 0) {
            frame = 0;
        }
        showFrame(frame);
    });
    $("#right").click(() => {
        frame++;
        if (frame >= frameCount) {
            frame = frameCount - 1;
        }
        showFrame(frame);
    });
});
