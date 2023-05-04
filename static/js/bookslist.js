// Get the button group element
const exportButtons = document.getElementById("export-buttons");

// Get the table element
const table = document.getElementById("booksList");

// Attach a click event listener to each export button
exportButtons.querySelectorAll(".dropdown-item").forEach(button => {
  button.addEventListener("click", () => {
    // Get the export format from the button's text
    const exportFormat = button.textContent.trim().toLowerCase();

    // Export the table in the specified format
    switch (exportFormat) {
      case "csv":
        exportTableToCSV(table);
        break;
      case "pdf":
        exportToPdf(table);
        break;
      case "excel":
        exportToExcel(table);
        break;
      case "print":
        window.print();
        break;
    }
  });
});

function exportTableToCSV() {
  const csv = [];
  const rows = document.querySelectorAll("table tr");

  // Loop through each row in the table
  for (let i = 0; i < rows.length; i++) {
    const row = [];
    const cells = rows[i].querySelectorAll("td, th");

    // Loop through the first six cells in the row
    for (let j = 0; j < Math.min(cells.length, 6); j++) {
      row.push(cells[j].innerText);
    }

    // Add the row to the CSV data
    csv.push(row.join(","));
  }

  // Download the CSV file
  downloadCSV(csv.join("\n"), "Books List.csv");
}

function downloadCSV(csv, filename) {
  const link = document.createElement("a");
  link.style.display = "none";
  link.setAttribute("href", "data:text/csv;charset=utf-8," + encodeURIComponent(csv));
  link.setAttribute("download", filename);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
function exportToPdf() {
  // Get the table element
  var table = document.getElementById("booksList");

  // Create a new jsPDF instance
  var doc = new jsPDF();

  // Define custom theme and color scheme
  var theme = {
    tableLineColor: [153, 153, 153], // Color of the table border
    textColor: [0, 0, 0], // Color of the text
    headStyles: { fillColor: [46, 128, 186], textColor: [255, 255, 255] }, // Style of the table header
    alternateRowStyles: { fillColor: [245, 245, 245] }, // Style of alternate rows
  };

  // Add a title to the PDF document
  doc.setFontSize(15);
  doc.text("Books List", doc.internal.pageSize.width / 2, 10, { align: "center" });
  doc.line(20, 20, doc.internal.pageSize.width - 20, 20); // Add line divider after title

  var columns = [];
  var ths = table.querySelectorAll("thead th");
  for (var i = 0; i < 6; i++) {
    columns.push({ header: ths[i].textContent.trim(), dataKey: ths[i].getAttribute("data-key") });
  }
  // Call the autoTable plugin with custom theme and color scheme
  doc.autoTable({
    html: table,
    startY: 30,
    theme: "striped",
    tableLineColor: theme.tableLineColor,
    tableLineWidth: theme.tableLineWidth,
    headStyles: theme.headStyles,
    bodyStyles: theme.bodyStyles,
    alternateRowStyles: theme.alternateRowStyles,
    columns: columns,
    columnStyles: {
      0: { halign: "center" },
      1: { halign: "center" },
      2: { halign: "center" },
      3: { halign: "center" },
      4: { halign: "center" },
      5: { halign: "center" },
    },
    styles: { textColor: theme.textColor, fontSize: 12 },
  });

  // Save the PDF document
  doc.save("Books List.pdf");
}
function exportToExcel() {
  // Get the HTML table element
  var table = document.getElementById("booksList");

  // Create a new workbook
  var workbook = XLSX.utils.book_new();

  // Extract the first 6 columns from the table
  var columns = [];
  for (var i = 0; i < table.rows.length; i++) {
    var row = [];
    for (var j = 0; j < 6; j++) {
      row.push(table.rows[i].cells[j].innerText);
    }
    columns.push(row);
  }

  // Create a new worksheet and add the columns to it
  var worksheet = XLSX.utils.aoa_to_sheet(columns);

  // Add the worksheet to the workbook
  XLSX.utils.book_append_sheet(workbook, worksheet, "Sheet1");

  // Save the workbook as an Excel file
  XLSX.writeFile(workbook, "Books List.xlsx");

}