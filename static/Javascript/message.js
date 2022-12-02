document.querySelector("#submit").onclick = (e) => {
    ChatSocketDict[groupId].send(JSON.stringify({
        "message": document.querySelector("#message").value,
        "type": "message",
        "sender": id,
        "receiver": clickId,
    }))
    document.querySelector("#message").value = ""
}