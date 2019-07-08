
// main用 JQuery
var duration = 300;

$(function(){
  $('.header li:nth-child(n+2):nth-child(-n+4)').on('mouseover', function(){
    $(this).stop(true).animate({
      'background-color': '#555',
      'color': '#999'
    }, duration, 'easeOutSine')
  })
  $('.header li:nth-child(n+2):nth-child(-n+4)').on('mouseout', function(){
    $(this).stop(true).animate({
      'background-color': '#000',
      'color': '#FFF'
    }, duration, 'easeOutSine')
  })
})

 //ハンバーガーメニュー　テスト
$(function(){
  $('.hamburger').on('mouseover', function(){
    $('.hamburger_line1').stop(true).animate({
      'background-color': '#AAA'
    }, 150);
  });
  $('.hamburger').on('mouseout', function(){
    $('.hamburger_line1').stop(true).animate({
      'background-color': '#FFF'
    }, 150);
  });
  $('.hamburger').on('mouseover', function(){
    $('.hamburger_line2').stop(true).animate({
      'background-color': '#AAA'
    }, 250);
  });
  $('.hamburger').on('mouseout', function(){
    $('.hamburger_line2').stop(true).animate({
      'background-color': '#FFF'
    }, 250);
  });
  $('.hamburger').on('mouseover', function(){
    $('.hamburger_line3').stop(true).animate({
      'background-color': '#AAA'
    }, 350);
  });
  $('.hamburger').on('mouseout', function(){
    $('.hamburger_line3').stop(true).animate({
      'background-color': '#FFF'
    }, 350);
  });
  $('.hamburger').on('click', function(){
    $('.back_black').animate({
      'opacity': 0.7,
      'z-index': 100
    }, duration);
    $('.hamburger_menu').animate({
      'right': 0,
      'z-index': 101
    }, duration);
  });
  $('.back_black').on('click', function(){
    $('.back_black').animate({
      'opacity': 0,
      'z-index': -1
    }, duration);
    $('.hamburger_menu').animate({
      'right': '-450px',
      'z-index': 0
    }, duration);
  });
});

$(function(){
  $('.hamburger_menu li a:nth-child(n+1)').on('mouseover', function(){
    $(this).stop(true).animate({
      'padding-left': '30px',
      'color': '#AAA'
    }, duration);
  });
  $('.hamburger_menu li a:nth-child(n+1)').on('mouseout', function(){
    $(this).stop(true).animate({
      'padding-left': '0',
      'color': '#FFF'
    }, duration);
  });
});
