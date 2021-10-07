function show_ct(id){
    $("#"+id).css('visibility','visible'); 
}
function hide_ct(){
    $(".arrow-right").css('visibility','hidden'); 
}
function alert_message(_message){
    if(_message != null){
        alert(_message);
    }    
}
function show_imgct(id_img_main,id_img, url){
    document.getElementById(id_img_main).src=url;
    
    $("#img_main_child img").each(function() {
        $(this).removeClass("chitiet_sp_hinh_nho_chon")
    });

    $("#" + id_img).addClass("chitiet_sp_hinh_nho_chon")        
}