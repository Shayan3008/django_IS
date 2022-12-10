document.querySelectorAll(".messageOpen").forEach(el => el.onclick = (e) => {
    if (groupId !== "") {
        ChatSocketDict[groupId].close()
        delete ChatSocketDict[groupId]
    }
    clickId = e.target.id
    groupId = parseInt(id) < parseInt(clickId) ? id + clickId : clickId + id
    messages.innerHTML = ''
    $.ajax(
        {
            url: `/chat/chats/${groupId}/`,
            type: "GET",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            contentType: false,
            processData: false,
            success: function (getData) {
                const data = JSON.parse(getData)
                for (let i = 0; i < data.length; i++) {
                    if (data[i].EncryptedText != null) {
                        let div = document.createElement("div")
                        let p = document.createElement("p")
                        let text = document.createTextNode(data[i].EncryptedText)
                        p.append(text)
                        p.style.fontSize = "25px"
                        div.style.display = "flex"
                        if (data[i].sender !== id)
                            div.style.justifyContent = "flex-end"
                        else
                            div.style.justifyContent = "flex-start"
                        div.style.padding = "10px"
                        div.append(p)
                        messages.append(div)
                    }
                    else {
                        let div = document.createElement("div")
                        div.style.padding = "10px"
                        div.style.display = "flex"
                        if (data[i].sender !== id)
                            div.style.justifyContent = "flex-end"
                        else
                            div.style.justifyContent = "flex-start"
                        var x = document.createElement("AUDIO")
                        x.src = data[i].Audio
                        x.setAttribute("controls", "controls");
                        div.append(x)
                        messages.append(div)
                    }
                }
            }
        });
    url = `ws://${window.location.host}/ws/${groupId}`
    ChatSocketDict[groupId] = new WebSocket(url)
    ChatSocketDict[groupId].onmessage = (e) => {
        let data = JSON.parse(e.data)
        if (data.type == "chat") {
            let div = document.createElement("div")

            div.style.display = "flex"
            div.style.justifyContent = "flex-end"
            if (data.sender !== id)
                div.style.justifyContent = "flex-end"
            else
                div.style.justifyContent = "flex-start"
            let text = document.createTextNode(data.message)
            div.style.padding = "10px"
            div.append(text)
            messages.append(div)
        }

        else if (data.type == "audio") {
            let div = document.createElement("div")
            div.style.padding = "10px"
            if (data.sender !== id)
                div.style.justifyContent = "flex-end"
            else
                div.style.justifyContent = "flex-start"
            var x = document.createElement("AUDIO")
            x.src = data.message
            x.setAttribute("controls", "controls");
            div.append(x)
            messages.append(div)
        }
    }
    if (messagePage.classList.contains("hidden")) {
        messagePage.style.display = "block"
        messagePage.classList.remove("hidden")
    }
})