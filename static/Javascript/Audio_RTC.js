// Socket Messages


// RTC FOR AUDIO
record.onclick = (e) => {
    console.log("Recorde")
    recorded = true
    navigator.mediaDevices.getUserMedia({
        audio: true,
        video: false
    }).then(handleSuccess)
}
const handleSuccess = (stream) => {
    const options = { mimeType: 'audio/webm' };
    const recordedChunks = [];
    const mediaRecorder = new MediaRecorder(stream, options);
    mediaRecorder.addEventListener('dataavailable', function (e) {
        if (e.data.size > 0) recordedChunks.push(e.data);
    });

    mediaRecorder.addEventListener('stop', function () {
        let blob = new Blob(recordedChunks)
        sendAudio(blob)

    });

    stop.addEventListener('click', function () {
        recorded = false
        mediaRecorder.stop();
        stream.getTracks().forEach(function (track) {
            if (track.readyState == 'live' && track.kind === 'audio') {
                track.stop();
            }
        });
    });
    mediaRecorder.start();
};