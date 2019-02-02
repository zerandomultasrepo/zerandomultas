$("#lnkComoRecorrer").on('click', function() {
    $("#Principal").hide();
    $("#Cadastro").show();
    $("#Contato").hide();
    $("#Depoimentos").hide();
});

$("#lnkSobre").on('click', function() {
    $("#Principal").show();
    $("#Cadastro").hide();
    $("#Contato").hide();
    $("#Depoimentos").hide();
});

$("#lnkDepoimentos").on('click', function() {
    $("#Principal").hide();
    $("#Cadastro").hide();
    $("#Contato").hide();
    $("#Depoimentos").show();
});

$("#lnkFaleConosco").on('click', function() {
    $("#Principal").hide();
    $("#Cadastro").hide();
    $("#Contato").show();
    $("#Depoimentos").hide();
});

$("#btQueroOrcamento").on('click', function() {
    $("#Principal").hide();
    $("#Cadastro").show();
    $("#Contato").hide();
    $("#Depoimentos").hide();
});

$("#btQueroOrcamento2").on('click', function() {
    $("#Principal").hide();
    $("#Cadastro").show();
    $("#Contato").hide();
    $("#Depoimentos").hide();
});

$("#plainSelect").on('change', function() {
    var value = this.value;
    if(value == 0){
        $("#lb_planValue").text('0,00');
    }
    if(value == 1){
        $("#lb_planValue").text('88,38');
    }
    if(value == 2){
        $("#lb_planValue").text('130,16');
    }
    if(value == 3){
        $("#lb_planValue").text('195,23');
    }
    if(value == 4){
        $("#lb_planValue").text('293,47');
    }
    if(value == 5){
        $("#lb_planValue").text('293,47');
    }
});
