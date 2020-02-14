
const showFrame = (num) => {
    const imgs = $("#images img");
    imgs.hide();
    $("#frame-num").text(num);
    $(`#images img:eq(${num})`).show();
};

$(document).ready(() => {
    $("#upload").fileupload();
    let frameCount = 0;
    let frame = 0;
    $.get("/frames?name=test", (data) => {
        const cont = $("#images");
        $(data).appendTo(cont);
        frameCount = $("#images img").length;
        showFrame(0);
    });
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
