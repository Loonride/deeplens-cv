
const showFrame = (num) => {
    const imgs = $("#images img");
    imgs.hide();
    $("#frame-num").text(num);
    $(`#images img:eq(${num})`).show();
};

let frameCount = 0;

const handleImageData = (data) => {
    const cont = $("#images");
    $(data).appendTo(cont);
    frameCount = $("#images img").length;
    showFrame(0);
}

$(document).ready(() => {
    let frame = 0;
    $("#fileupload").fileupload({
        done: (e, data) => {
            handleImageData(data.result);
        }
    });
    // $.get("/frames?name=test", (data) => {
    //     const cont = $("#images");
    //     $(data).appendTo(cont);
    //     frameCount = $("#images img").length;
    //     showFrame(0);
    // });
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
        if (frameCount == 0) {
            frame = 0;
        }
        showFrame(frame);
    });
});
