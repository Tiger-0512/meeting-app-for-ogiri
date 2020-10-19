$(function(){
    'use strict';

    var answerbtn = $('#answer-btn');
    var audiencebtn = $('#audience-btn');

    answerbtn.click(function(){
        var user_name = $('#input_user_name').val();

        var ul = $('.answer-list').children('ul');
        var name_list = '<li>' + user_name + '</li>';
        ul.append(name_list);
        answerbtn.prop("disabled" , true);
        audiencebtn.prop("disabled" , true);
    });



    audiencebtn.click(function(){
        var user_name = $('#input_user_name').val();

        var ul = $('.audience-list').children('ul');
        var name_list = '<li>' + user_name + '</li>';
        ul.append(name_list);
        answerbtn.prop("disabled" , true);
        audiencebtn.prop("disabled" , true);
    });
});    
