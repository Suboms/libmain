document.addEventListener("DOMContentLoaded", function () {
    let table = new DataTable("#booksList", {
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
              title: "Book List",
              className: "dropdown-item",
              exportOptions: {
                columns: [0, 1, 2, 3, 4, 5, 6, 7],
              },
              text: "<span>CSV</span>",
            },
            {
              extend: "excelHtml5",
              title: "Book List",
              className: "dropdown-item",
              exportOptions: {
                columns: [0, 1, 2, 3, 4, 5, 6, 7],
              },
              text: "<span>Excel</span>",
            },
            {
              extend: "print",
              title: "Book List",
              className: "dropdown-item",
              exportOptions: {
                columns: [0, 1, 2, 3, 4, 5, 6, 7],
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
  