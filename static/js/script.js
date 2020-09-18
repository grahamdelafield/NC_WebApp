$(document).ready(function() {
  table = $('#example').DataTable();
});

function inputText(col, id) {
    table.destroy();
    var text = document.getElementById(id).value;
    text = text.trim();
    console.log(text);
    var elems = text.split("\n");
    elems = elems.join("|");
    console.log(elems);
    table = $('#example').DataTable({
        "search": {regex: true, smart: true}}).column(col).search(elems, true, false).draw();
}

function resetTable() {
  table.destroy();
  $(document).ready(function() {
    table = $('#example').DataTable();
  });
}
