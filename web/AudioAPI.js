export default class AudioAPI{
    constructor(document){
        this.audioContext = new AudioContext();
        this.document = document;
        this.audioElement;
    }

    setupAudio(){
        this.audioElement = document.querySelector("audio");
        const track = this.audioContext.createMediaElementSource(this.audioElement);
        track.connect(this.audioContext.destination);
    }

    playAudio(){
        if(this.audioElement) {
            this.audioContext.resume().then(() => {
                this.audioElement.play();
            });
        }
    }

    stopAudio(){
        if (this.audioElement) {
            this.audioElement.pause();
            this.audioElement.currentTime = 0;
        };
    }
}