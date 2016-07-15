$(document).ready(function(){  
    CHOSEN='0'
    $("#friend_btn").click(function(){
        $("#group").css("display", "none");
        $("#friend").css("display", "block");
    });
    $("#group_btn").click(function(){
        $("#group").css("display", "block");
        $("#friend").css("display", "none");
    }); 
    $("img").click(function(){
        CHOSEN = $(this).attr("id");
        var id = "#"+CHOSEN;
        $("img").each(function(){
            $(this).css("border", "0px");
        });
        $(id).css("border", "3px solid green");
    });
    $("#next").click(function(){
        $("img").each(function(){
            $(this).css("border", "0px");
        });
        $.post("/ajax",{message:CHOSEN},function(data,status){
            if(status == "success")
            {
                alert(data);
                CHOSEN = '0';
            }
            else alert("ajax failure")
        });
        
    });

});   
