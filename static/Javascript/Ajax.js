// AJAX
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function sendAudio(blob) {
    var wavFile = new File([blob], "audio.wav");
    var form = new FormData();
    form.append("myAudio", wavFile);
    form.append("id", groupId)
    $.ajax(
        {
            url: "/chat/audio/aud/",
            type: "POST",
            data: form,
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            contentType: false,
            processData: false,
            success: function (getData) {
                console.log(getData)
                let doc = getData
                console.log(doc)
                ChatSocketDict[groupId].send(JSON.stringify({
                    "message": doc,
                    "type": "audio",
                    "sender": id,
                    "receiver": clickId,
                }))


                // ChatSocket.send(JSON.stringify({
                //     "type":"audio",
                //     "path":getData
                // }))

            }
        });
}