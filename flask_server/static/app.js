const showFrame = (num) => {
    const imgs = $("#images img");
    imgs.hide();
    $("#frame-num").text(num);
    $(`#images img:eq(${num})`).show();
};

let frameCount = 0;

const handleImageData = (rawData) => {
    const data = JSON.parse(rawData);
    const cont = $("#images");
    cont.empty();
    $(decodeURIComponent(data.imgs)).appendTo(cont);
    $('#clip-name').text(data.name);
    frameCount = $("#images img").length;
    $("#slider").attr("max", "" + (frameCount - 1));
    showFrame(0);
}

const getClips = () => {
    $.get("/clips", (data) => {
        let clipNames = data.split(",");
        clipNames.splice(clipNames.length - 1, 1);
        const cont = $("#clips");
        cont.empty();
        clipNames.forEach(clipName => {
            const elem = $(`<button data-name=${clipName}>${clipName}</button>`);
            elem.appendTo(cont);
        });


        $("#clips button").click(function() {
            const elem = $(this);
            const clipName = elem.attr('data-name');

            $.get("/frames?name=" + clipName, (data) => {
                handleImageData(data);
            });
        });
    });
}

$(document).ready(() => {
    getClips();
    let frame = 0;
    $("#fileupload").fileupload({
        done: (e, data) => {
            handleImageData(data.result);
            getClips();
        }
    });
    // $.get("/frames?name=test", (data) => {
    //     const cont = $("#images");
    //     $(data).appendTo(cont);
    //     frameCount = $("#images img").length;
    //     showFrame(0);
    // });

    // $("#left").click(() => {
    //     frame--;
    //     if (frame < 0) {
    //         frame = 0;
    //     }
    //     showFrame(frame);
    // });
    // $("#right").click(() => {
    //     frame++;
    //     if (frame >= frameCount) {
    //         frame = frameCount - 1;
    //     }
    //     if (frameCount == 0) {
    //         frame = 0;
    //     }
    //     showFrame(frame);
    // });

    $("#slider").on("input", function () {
        const val = $(this).val();
        showFrame(parseInt(val));
    });
});
