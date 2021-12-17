$(function(){
    'use strict';
    const URL = 'https://lhaj6ye9la.execute-api.ap-northeast-1.amazonaws.com/getDataAPI/dynamodb-ctrl';
    var title = $('#ogiri-title').children('h1');
    $('#start-btn').click(function(){
      $.ajax({
          type: 'post' ,
          dataType: 'json' ,
          url: URL
      }).done(function(data){
          //成功時の処理
          console.log("ajax success!");
          console.log(data['Problem']);
          title.text(data['Problem']);
      }).fail(function(){
          //失敗時の処理
          console.log('ajax error');
      });
    });

});
