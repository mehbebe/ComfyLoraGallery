async function fetchLoRAs() {
    const response = await fetch('/get_loras?directory=./Models/loras');
    const data = await response.json();

    const gallery = document.getElementById('lora-gallery');
    gallery.innerHTML = '';

    if (data.error) {
        const errorMsg = document.createElement('p');
        errorMsg.textContent = data.error;
        gallery.appendChild(errorMsg);
        return;
    }

    data.forEach(lora => {
        const card = document.createElement('div');
        card.className = 'lora-card';

        const img = document.createElement('img');
        img.src = lora.preview || 'placeholder.png';
        img.alt = lora.name;

        const title = document.createElement('h3');
        title.innerText = lora.name;

        const trigger = document.createElement('p');
        trigger.innerText = `Trigger: ${lora.trigger_word}`;

        const model = document.createElement('p');
        model.innerText = `Model: ${lora.base_model}`;

        card.appendChild(img);
        card.appendChild(title);
        card.appendChild(trigger);
        card.appendChild(model);
        gallery.appendChild(card);
    });
}

document.addEventListener('DOMContentLoaded', fetchLoRAs);
