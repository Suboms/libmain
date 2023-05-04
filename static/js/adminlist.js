document.addEventListener("DOMContentLoaded", function () {
    let table = new DataTable("#adminList", {
      pageLength: 50,
      dom: "Bfrtip",
      buttons: [
        {
          text: "Export",
          className: "btn btn-outline-primary",
          extend: "collection",
          buttons: [
            {
              extend: "csvHtml5",
              title: "Admin List",
              className: "dropdown-item",
              exportOptions: {
                columns: [0, 1, 2, 3, 4],
              },
              text: "<span>CSV</span>",
            },
            {
              extend: "excelHtml5",
              title: "Admin List",
              className: "dropdown-item",
              exportOptions: {
                columns: [0, 1, 2, 3, 4],
              },
              text: "<span>Excel</span>",
            },
            {
              extend: "print",
              title: "Admin List",
              className: "dropdown-item",
              exportOptions: {
                columns: [0, 1, 2, 3, 4],
              },
              text: "<span>PDF</span>",
            },
          ],
          init: function (api, node, config) {
            $(node).removeClass("btn-default");
          },
        },
      ],
    });
  });
  