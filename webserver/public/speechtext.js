class SpeechRecognitionAPI{
    constructor(options){
        const SpeechToText = window.SpeechRecognition || window.webkitSpeechRecognition;
        this.speechAPI = new SpeechToText();
        this.output = options.output ? options.output : document.createElement("div");
        this.speechAPI.continous = true;
        this.speechAPI.interimResult = true;
        this.speechAPI.onresult = (event) => {
            const resultIndex = event.resultIndex;
            const transcript = event.results[resultIndex][0].transcript;
            this.output.textContent = transcript;
        }
     }
     init() {
         this.speechAPI.start();
     }
     stop() {
         this.speechAPI.stop();
     }
 }
 window.onload = function(){
     const speech = new SpeechRecognitionAPI({
         output : document.querySelector('.output')
     })
     speech.init()
    //  document.querySelector('.btm-start').addEventListener("click", ()=>{
    //      speech.init();
    //  })
    //  document.querySelector('.btm-end').addEventListener("click", ()=>{
    //     speech.stop();
    // })
 }