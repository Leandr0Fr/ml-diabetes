const check_inputs = document.querySelectorAll(".input-container.check");
check_inputs.forEach(check_container => {
    check_container.addEventListener('click', () => {
        let icon = check_container.querySelector("i");
        let check = check_container.querySelector("input");
        check.value = (check.value == "0" ? "1" : "0");

        if (icon === document.getElementById('sex-icon')) {
            icon.classList.toggle('fa-mars');
        }
        else {
            icon.classList.toggle('on');
            check_container.querySelector('label').classList.toggle('on');
        }
    })
});

document.querySelector('.btn').addEventListener('click', async e => {
    e.preventDefault();
    const response = await fetch(
        "/predict", {
        method: 'POST',
        body: new FormData(document.querySelector('form'))
    });
    if (!response.ok) {
        throw new Error('Hubo un problema al realizar la petición.');
    }
    else {
        const predict = await response.text();
        showAlert(predict);
    }
});

function showAlert(predict) {
    const fullBox = document.createElement("DIV");
    const msgBox = document.createElement("SECTION");
    const msg = document.createElement("B");
    const comment = document.createElement("p");
    const acceptBtn = document.createElement("BUTTON");
    msg.id = "msg";
    acceptBtn.classList.add("btn");

    fullBox.style.cssText = 
    `
        background-color: #2224;
        width: 100%;
        height: 100%;
        position: fixed;
        left: 0;
        top: 0;
        display: flex;
        justify-content: center;
        align-items: center;
    `;

    msgBox.style.cssText =
    `
        width: 400px;
        height: 220px;
        text-align: center;
        background-color: var(--color-dark);
        opacity: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
        border-radius: 14px;
        font-size: 32px;
        font-weight: bold;
    `;

    acceptBtn.style.cssText = 
    `
        max-width: 50%;
        max-height: 50px;
        padding: 4px 8px;
        font-weight: bold;
    `

    msg.innerHTML = `Probabilidad del <span>${predict}%</span>`;
    if(predict >= 60) {
        comment_text = "Deberías recibir atención médica";
        msg.querySelector("span").style.color = '#800020'
    }
    else if (predict >=40) {
        comment_text = "Mejorá tus hábitos";
        msg.querySelector("span").style.color = '#E35335'
    }
    else {
        comment_text = "Seguí cuidándote";
        msg.querySelector("span").style.color = '#097969'
    }
    comment.innerHTML = comment_text;

    acceptBtn.innerHTML = "Aceptar";

    msgBox.appendChild(msg);
    msgBox.appendChild(comment);
    msgBox.appendChild(acceptBtn);
    fullBox.appendChild(msgBox);

    const container =  document.querySelector("html");
    container.appendChild(fullBox);

    acceptBtn.addEventListener('click', function(){
        container.removeChild(container.lastChild);
    });
    
}
