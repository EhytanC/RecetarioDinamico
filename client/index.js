const API_URL = 'http://127.0.0.1:8000/'
const xhr = new XMLHttpRequest();

function onRequestHandler(){
    if(this.readyState == 4 && this.status == 200){
        console.log(this.response);
    }
}

xhr.addEventListener("load", onRequestHandler);
xhr.open('GET','${API_URL}/recetas')