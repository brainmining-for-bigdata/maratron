$(function (){

  function q(selector) { return document.querySelector(selector)}
  
  // select box js 기능 및 value 얻기
  var voiceType = [];
  $(".voice").heapbox({
    'onChange':function(value){voiceType=value}
  });

  $(function () {
      $("#button").click(function () {        
          
          // voice 빈 값 유무 확인 
          if (voiceType.length==0) {
            //alert("목소리 타입을 선택하세요");
            Swal.fire({
              type: 'warning',
              title: '"목소리 타입을 선택하세요!"',
              animation: false,
              customClass: {
                popup: 'animated tada'
              }
            })
            return false;
          }        
        
          // text 빈 값 유무 확인 
          if (!document.sentMessage.text.value) {
              //alert("내용을 입력하세요");
              Swal.fire({
                type: 'warning',
                title: '"텍스트를 입력하세요!"',
                animation: false,
                customClass: {
                  popup: 'animated tada'
                }
              })
              document.sentMessage.text.focus()
              return false;
          }

          // 영어 타입 voice에서 한글 입력여부 검출
          check = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;
          if (voiceType !=="ko_female" && check.test(document.sentMessage.text.value)) {
            Swal.fire({
              type: 'warning',
              title: '"Just write it in English please!"',
              animation: false,
              customClass: {
                popup: 'animated tada'
              }
            })
            document.getElementById("text").value='';
            document.sentMessage.text.focus()
            return false;
          }


          // 한글 타입 voice에서 영어 입력여부 검출
          check = /[a-z|A-Z]/;
          if (voiceType =="ko_female" && check.test(document.sentMessage.text.value)) {
            Swal.fire({
              type: 'warning',
              title: '"알파벳은 못 읽어요 ㅜㅜ"',
              animation: false,
              customClass: {
                popup: 'animated tada'
              }
            })
            document.getElementById("text").value='';
            document.sentMessage.text.focus()
            return false;
          }          


          // Synthesize 처리 과정
          text = q("#text").value.trim()

          if (text) {
            q('#button').hidden = true
            q('.loading-group').hidden = false
            q('#loading_bg').hidden = false
            q('#audio').hidden = true   
          }

          // 텍스트 값 views.py 전달
          var allData = {"voiceType": voiceType, "text": $("#text").val()};
            $.ajax({
              url: '/tts/synthesize/',
              datatype: "text",
              type: "POST",
              data: allData,
              success: function (result) {
                q('#button').hidden = false
                q('.loading-group').hidden = true
                q('#loading_bg').hidden = true
                q('#audio').hidden = false
                q('#audio').src = "data:audio/wav;base64," + result ;
              }
            });
      });
  });
});