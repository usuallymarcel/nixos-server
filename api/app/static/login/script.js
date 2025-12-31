const API_URL = window.ENV.API_URL

document.addEventListener('DOMContentLoaded', function() {
    // const client_id = Date.now()
    // document.querySelector("#ws-id").textContent = client_id;

    // const protocol = location.protocol === "https:" ? "wss://" : "ws://";
    // ws = new WebSocket(protocol + location.host + `/ws/${client_id}`);

    // ws.onmessage = function(event) {
    //     const messages = document.getElementById('messages')
    //     const message = document.createElement('li')
    //     message.textContent = event.data
    //     messages.appendChild(message)
    //     message.scrollIntoView({ behavior: 'smooth', block: 'end' })
    // };
});

async function login() {
    const emailInput = document.getElementById("email")
    const passwordInput = document.getElementById("password")
    const email = emailInput.value
    const password = passwordInput.value

    if (!email || !password) {
        console.error("invalid signup details")
        return
    }
    
    const res = await fetch(API_URL + '/users/login', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password })
    }).catch(err => {
        console.error("Error: ", err)
    })
    const data = await res.json()

    console.log(data)
}

async function sign_up() {
    const emailInput = document.getElementById("email")
    const passwordInput = document.getElementById("password")
    const email = emailInput.value
    const password = passwordInput.value

    if (!email || !password) {
        console.error("invalid signup details")
        return
    }

    console.log(emailInput.value + passwordInput.value)

    const res = await fetch(API_URL + '/users/sign_up', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password })
    })
    const data = await res.json()

    console.log(data)
}