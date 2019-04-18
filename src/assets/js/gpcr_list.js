$(document).ready(function() {
  $("#table").DataTable({
      "ajax": {
          "processing": true,
          "url": "/gpcrs/json/",
          "dataSrc": ""
      },
    "deferRender": true,
    "columns": [
      { "data": "fields.pdb_id",
       "render": function(data, type, row, meta){
          if(type === 'display'){
              data = '<a href="' + data + '">' + data + '</a>';
          }
          return data;
       }
      },
      { "data": "fields.gpcr_class" },
      { "data": "fields.gpcr_name" },
      { "data": "fields.subfamily" },
      { "data": "fields.species" }
    ],
    dom: "Bfrtip",
    buttons: [
      "copy", "csv", "excel"
    ],
    responsive:  true,
    scrollY:     "50vh",
    deferRender: true,
    scroller:    true
  });

  $(".dt-buttons").addClass("float-left");
  $(".dataTables_filter").addClass("float-right");
  $("input").removeClass("form-control-sm");
});
