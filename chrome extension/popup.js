console.log('popup running');
setup();
function setup(){
  let bgpage = chrome.extension.getBackgroundPage();
   window.word = bgpage.word ;
  console.log(word);
}

async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

document.getElementById("mybutton").addEventListener("click", postData('http://osamafityani.pythonanywhere.com/',{dscr: window.word} )
.then(data=>{
  console.log(data);
  document.getElementById("info").value = data;
  var msg = new SpeechSynthesisUtterance();
    msg.text = data;
    window.speechSynthesis.speak(msg);
}));
