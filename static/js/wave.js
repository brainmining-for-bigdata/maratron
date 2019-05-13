// SOUND WAVE JS
var Spectrum = WaveSurfer.create({
    container: '#audio-spectrum',
    progressColor: '#b03c36',
    barWidth: 1,
    barHeight: 1.5,
    hideScrollbar: true,
    cursorWidth:0,
  });    
  
  window.addEventListener("resize", function(){
    var currentProgress = Spectrum.getCurrentTime() / Spectrum.getDuration();
  
    Spectrum.empty();
    Spectrum.drawBuffer();
  
    Spectrum.seekTo(currentProgress);
  });
        
  Spectrum.load("/static/audio/kor_version.wav");
  
  var originalTime = "";
  Spectrum.on('ready', function () {
    originalTime = Spectrum.getDuration().toFixed(1);
    document.getElementById('audio-time').innerText =  originalTime;
  });

  Spectrum.on('audioprocess', function() {
    if(Spectrum.isPlaying()) {
        var totalTime = Spectrum.getDuration(),
        currentTime = Spectrum.getCurrentTime(),
        remainingTime = totalTime - currentTime;
        console.log(remainingTime.toFixed(2));
        document.getElementById('audio-time').innerText = Math.round(remainingTime).toFixed(1);
        if(remainingTime.toFixed(2) < 0.02) {
          Spectrum.stop();
          document.getElementById('btn-pause').value = 'Play';
          document.getElementById('btn-pause').id = 'btn-play';
          document.getElementById('icon').className = 'fa fa-play';
          document.getElementById('audio-time').innerText = originalTime;          
        };
    }; 
  });


// SOUND WAVE JS
var Spectrum2 = WaveSurfer.create({
    container: '#audio-spectrum2',
    progressColor: '#b03c36',
    barWidth: 1,
    barHeight: 1.5,
    hideScrollbar: true,
    cursorWidth:0,
  });    
  
  
  window.addEventListener("resize", function(){
    var currentProgress = Spectrum2.getCurrentTime() / Spectrum2.getDuration();
  
    Spectrum2.empty();
    Spectrum2.drawBuffer();
  
    Spectrum2.seekTo(currentProgress);
  });
        
  Spectrum2.load("/static/audio/eng_version.wav");
  

  var originalTime2 = "";
  Spectrum2.on('ready', function () {
    originalTime2 = Spectrum2.getDuration().toFixed(1);
    document.getElementById('audio-time2').innerText =  originalTime2;
  });
  
  Spectrum2.on('audioprocess', function() {
    if(Spectrum2.isPlaying()) {
        var totalTime2 = Spectrum2.getDuration(),
        currentTime2 = Spectrum2.getCurrentTime(),
        remainingTime2 = totalTime2 - currentTime2;
        document.getElementById('audio-time2').innerText = Math.round(remainingTime2).toFixed(1);
        if(remainingTime2.toFixed(2) < 0.02) {
          Spectrum2.stop();
          document.getElementById('btn-pause2').value = 'Play';
          document.getElementById('btn-pause2').id = 'btn-play2';
          document.getElementById('icon2').className = 'fa fa-play';
          document.getElementById('audio-time2').innerText = originalTime2;          
        };
    }; 
  });
  