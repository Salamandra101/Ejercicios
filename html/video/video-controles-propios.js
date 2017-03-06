// Javascript //

var mivideo, reproducir, progress, maximo;

maximo=100;

function comenzar() {

  mivideo=document.getElementById("mivideo")
  reproducir=document.getElementById("reproducir");
  progress=document.getElementById("progress");

  reproducir.addEventListener("click",clicando,false);
  progress.addEventListener("click",adelantando,false);
}

function clicando() {
  if((mivideo.paused==false) && (mivideo.ended==false)){
    mivideo.pause();
    reproducir.innerHTML="Play"
  }
  else{
    mivideo.play();
    reproducir.innerHTML="Pausa";
    estado;
  }
}

function estado() {
  if(mivideo.ended==false){
    var total=parseInt(mivideo.currentTime*maximo/mivideo.duration);
    progress.
  }
}

window.addEventListener("load",comenzar,false);
