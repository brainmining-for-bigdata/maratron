$(function (){

  function q(selector) { return document.querySelector(selector)}

  var voiceType = [];
  console.log("voiceType 값 :"+voiceType+"typeof voiceType :"+typeof voiceType);

  $("#male").click(function (){
      $("#female").removeClass("female_change");
      $("#male").addClass("male_change");
      voiceType = $(this).attr("id");
      alert(voiceType);
  });

  $("#female").click(function (){
      $("#male").removeClass("male_change");
      $("#female").addClass("female_change");
      voiceType = $(this).attr("id");
      alert(voiceType);
  });

  $(function () {
      $("#button").click(function () {
        
          // voice 빈 값 유무 확인 
          if (voiceType.length==0) {
            alert("목소리 타입을 선택하세요");
            return false;
        }        
        
          // text 빈 값 유무 확인 
          if (!document.sentMessage.text.value) {
              alert("내용을 입력하세요");
              document.sentMessage.text.focus()
              return false;
          }

          // Synthesize 처리 과정
          text = q("#text").value.trim()

          if (text) {
            q("#message").textContent = "Synthesizing..."
            q('#button').disabled = false
            q('#audio').hidden = true  
          }

          // 텍스트 값 views.py 전달
          urls = '/tts/synthesize/';
          var allData = {"voiceType": voiceType, "text": $("#text").val()};
            $.ajax({
              url: urls,
              datatype: "text",
              type: "POST",
              data: allData,
              success: function (result) {
                audio = result["audio"]
                q('#audio').hidden = false
                q('#audio').src = audio
              }
            });
      });
  });
});

