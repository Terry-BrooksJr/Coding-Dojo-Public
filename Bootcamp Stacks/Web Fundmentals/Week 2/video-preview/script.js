console.log("page loaded...");

function previewPause(this){
  var vid = document.getElementById(this);
  vid.pause()
  console.log(this+" Successfully Paused")
}
function previewPlay(this){
  var vid = document.getElementById(this);
  vid.play();
  window.setTimeout(previewPause(this), 2000);
  console.log(this+" Successfully Previewed")
}
