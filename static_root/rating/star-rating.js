function myFunction() {
    var s1 = document.getElementById('1-star').checked;
    var s2 = document.getElementById('2-star').checked;
    var s3 = document.getElementById('3-star').checked;
    var s4 = document.getElementById('4-star').checked;
    var s5 = document.getElementById('5-star').checked;
    
    if (s1 == true)
        $("#id_sosao").val(1)
    if (s2 == true)
        $("#id_sosao").val(2)
    if (s3 == true)
        $("#id_sosao").val(3)
    if (s4 == true)
        $("#id_sosao").val(4)
    if (s5 == true)
        $("#id_sosao").val(5)
}