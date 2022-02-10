//
// function autoplayAndPause(this){
//     const video = this.autoplay;
// }
// function pauseP(this){
//     const video = this.pause;
// }

    const video = document.getElementByClassName("video")
    video.onmouseover = function(){
        video.play()
    }
    video.onmouseout = function(){
        video.pause()
    }
