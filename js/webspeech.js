var speech_count = 0;
//スタートボタンがクリックされたら
document.getElementById("start_recognition").onclick = function vr_function() {
  var result_text = document.getElementById('result_text');
  while (result_text.firstChild) {//resut_textの中身を空にする
    result_text.removeChild(result_text.firstChild);
  }
  //クラス生成
  SpeechRecognition = webkitSpeechRecognition || SpeechRecognition;
  const recognition = new SpeechRecognition();
  //設定
  recognition.lang = 'ja';
  recognition.interimResults = true;
  recognition.continuous = true;

  recognition.onresult = function(event) {
    var results = event.results;//results[i][0]に文字列が格納される
    if (document.getElementById('interim_result') == null) {
      var interim = document.createElement('d' + 'iv');
      interim.setAttribute('class', 'results');
      interim.setAttribute('id', 'interim_result');
      document.getElementById('result_text').appendChild(interim);
    }
    for (var i = event.resultIndex; i < results.length; i++) {
      if (results[i].isFinal) {
        speech_count++;
        result_line = "<font size='4'>" + results[i][0].transcript + "</font>";
        document.getElementById('interim_result').innerHTML = result_line;
        document.getElementById('interim_result').setAttribute('id', 'result' + speech_count);


        recognition.stop();
        document.getElementById('status').innerHTML = "";
        return;
      } else {
        document.getElementById('interim_result').innerHTML = "<font size='4' color='gray'>" + results[i][0].transcript + "</font>";
        flag_speech = 1;
      }
    }
  }
  document.getElementById('status').innerHTML = "回答中...";
  recognition.start();
}
