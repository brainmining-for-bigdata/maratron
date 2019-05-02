// SOUND WAVE JS
var Spectrum = WaveSurfer.create({
    container: '#audio-spectrum',
    progressColor: 'lightseagreen',
    //barWidth: 4,
    barHeight: 1.7,
    hideScrollbar: true,
    cursorWidth:0,
  });    
  
  window.addEventListener("resize", function(){
    var currentProgress = Spectrum.getCurrentTime() / Spectrum.getDuration();
  
    Spectrum.empty();
    Spectrum.drawBuffer();
  
    Spectrum.seekTo(currentProgress);
  });
        
  Spectrum.load("/static/audio/step-40000-audio.wav");
  
  Spectrum.on('ready', function () {
    console.log('ready');
  });

  Spectrum.on('audioprocess', function() {
    if(Spectrum.isPlaying()) {
        var totalTime = Spectrum.getDuration(),
        currentTime = Spectrum.getCurrentTime(),
        remainingTime = totalTime - currentTime;
        console.log(Math.round(remainingTime));
        if(Math.round(remainingTime)===0.0) {
            
            Spectrum.stop();
            document.getElementById('btn-pause').value = 'Play';
            document.getElementById('btn-pause').id = 'btn-play';
            document.getElementById('icon').className = 'fa fa-play'
           
        };
        document.getElementById('audio-time').innerText = Math.round(remainingTime).toFixed(1);
    }; 
  });
  
// SOUND WAVE JS
var Spectrum2 = WaveSurfer.create({
    container: '#audio-spectrum2',
    progressColor: 'lightseagreen',
    //barWidth: 4,
    barHeight: 1.7,
    hideScrollbar: true,
    cursorWidth:0,
  });    
  
  
  window.addEventListener("resize", function(){
    var currentProgress = Spectrum2.getCurrentTime() / Spectrum2.getDuration();
  
    Spectrum2.empty();
    Spectrum2.drawBuffer();
  
    Spectrum2.seekTo(currentProgress);
  });
        
  Spectrum2.load("/static/audio/step-13000-audio.wav");
  
  Spectrum2.on('ready', function () {
    console.log('ready');
  });

  Spectrum2.on('audioprocess', function() {
    if(Spectrum2.isPlaying()) {
        var totalTime2 = Spectrum2.getDuration(),
        currentTime2 = Spectrum2.getCurrentTime(),
        remainingTime2 = totalTime2 - currentTime2;
        console.log(Math.round(remainingTime2));
        if(Math.round(remainingTime2)===0.0) {
            
            Spectrum2.stop();
            document.getElementById('btn-pause2').value = 'Play';
            document.getElementById('btn-pause2').id = 'btn-play2';
            document.getElementById('icon2').className = 'fa fa-play'
           
        };
        document.getElementById('audio-time2').innerText = Math.round(remainingTime2).toFixed(1);
    }; 
  });
  