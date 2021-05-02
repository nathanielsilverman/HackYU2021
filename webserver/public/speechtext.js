window.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("button");
    const result = document.getElementById("result");
    const main = document.getElementsByTagName("main")[0];
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    if (typeof SpeechRecognition === "undefined") {
      button.remove();
      const message = document.getElementById("message");
      message.removeAttribute("hidden");
      message.setAttribute("aria-hidden", "false");
    } 
    else {
      let listening = false;
      const recognition = new SpeechRecognition();
      const start = () => {
        listening = true;
        recognition.start();
        button.textContent = "Stop listening";
        main.classList.add("speaking");
      };
      const stop = () => {
        listening = false
        recognition.stop();
        button.textContent = "Start listening";
        main.classList.remove("speaking");
      };
      const onResult = event => {
        result.innerHTML = "";
        for (const res of event.results) {
          const text = document.createTextNode(res[0].transcript);
          // const lang = document.getElementById("lang");
          // const translated_text = await translate(text, {to: lang.value})
          // result.append(translated_text);
          result.append(text);
        }
      };
      recognition.continuous = true;
      recognition.interimResults = true;
      recognition.addEventListener("result", onResult)
      button.addEventListener("click", () => {
        listening ? stop() : start();
      });
    }  
  }); 