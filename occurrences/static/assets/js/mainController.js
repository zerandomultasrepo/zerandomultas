// $("#lnkComoRecorrer").on('click', function() {
//     $("#Principal").hide();
//     $("#Cadastro").show();
//     //$("#Contato").hide();
//     $("#Depoimentos").hide();
// });

$("#lnkSobre").on('click', function() {
    $("#Principal").show();
  //  $("#Cadastro").hide();
  //  $("#Contato").hide();
    $("#Depoimentos").hide();
});

$("#lnkDepoimentos").on('click', function() {
    $("#Principal").hide();
  //  $("#Cadastro").hide();
  //  $("#Contato").hide();
    $("#Depoimentos").show();
});

// $("#lnkFaleConosco").on('click', function() {
//     $("#Principal").hide();
//     $("#Cadastro").hide();
//     $("#Contato").show();
//     $("#Depoimentos").hide();
// });

// $("#btQueroOrcamento").on('click', function() {
//     $("#Principal").hide();
//     $("#Cadastro").show();
//     //$("#Contato").hide();
//     $("#Depoimentos").hide();
// });

// $("#btQueroOrcamento2").on('click', function() {
//     $("#Principal").hide();
//     $("#Cadastro").show();
//     //$("#Contato").hide();
//     $("#Depoimentos").hide();
// });

$("#plainSelect").on('change', function() {
    var value = this.value;
    if(value == 0){
        $("#lb_planValue").text('0,00');
    }
    if(value == 1){
        $("#lb_planValue").text('40,00');
    }
    if(value == 2){
        $("#lb_planValue").text('60,00');
    }
    if(value == 3){
        $("#lb_planValue").text('100,00');
    }
    if(value == 4){
        $("#lb_planValue").text('140,00');
    }
    if(value == 5){
        $("#lb_planValue").text('250,00');
    }
    if(value == 6){
        $("#lb_planValue").text('300,00');
    }
    if(value == 7){
        $("#lb_planValue").text('500,00');
    }
    if(value == 8){
        $("#lb_planValue").text('1000,00');
    }
    if(value == 9){
        $("#lb_planValue").text('2500,00');
    }
    if(value == 10){
        $("#lb_planValue").text('5000,00');
    }
});
