$(function (){
  function q(selector) { return document.querySelector(selector)}

  var voiceType = [];
 /*console.log("voiceType 값 :"+voiceType+"typeof voiceType :"+typeof voiceType);

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
  }); */

  $('select').on('change', function() {
    // alert( this.value );
    voiceType = this.value;
    // console.log(voiceType)
  });

  $(function () {
      $("#button").click(function () {
        
          // voice 빈 값 유무 확인 
          if (voiceType.length==0) {
            //alert("목소리 타입을 선택하세요");
            Swal.fire({
              type: 'warning',
              title: '목소리 타입을 선택하세요',
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
                title: '내용을 입력하세요',
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

          // Synthesize 처리 과정
          text = q("#text").value.trim()

          if (text) {
            // q("#message").textContent = "Synthesizing..."
            // q('#button').disabled = false
          
            //$('#button').replaceWith('<img src="/tts/img/loading.gif">');
            q('#button').hidden = true
            q('.loading-group').hidden = false
            q('#loading_bg').hidden = false
            q('#audio').hidden = true   
          }

          // 텍스트 값 views.py 전달
          //urls = '/tts/synthesize/';
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