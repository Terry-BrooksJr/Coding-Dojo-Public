let likeCount = 0;

function likeCounter(){
    likeCount ++
    var eventLogging = Date.toUTCString(self)
    var likeCountElement = document.querySelector("#likeCountElement")
    likeCountElement.innerText = likeCount;
    console.log("Like number "+likeCount+" added at "+ eventLogging)
}
