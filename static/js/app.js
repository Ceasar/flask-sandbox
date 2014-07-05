$("form").on("submit", function(event) {
  console.log($(this).serialize());
});

$("button").click(function(event) {
    var $form = $("form");
    var data = {
        name: $form.find("input[name=name]").val(),
        animals: $form.find("select").val(),
    };
    console.log(data);
    $.ajax({
        url: "/",
        type: "POST",
        data: data,
        dataType: "json",
    });
});
