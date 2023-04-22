function onEdit(e) {
  var range = e.range;
  var sheet = range.getSheet();
  
  if (range.getColumn() == 2) {
    var row = range.getRow();
    var value = sheet.getRange(row, 2).getValue();
    
    if (value != "") {
      var randomString = generateRandomString(20);
      var formattedString = formatString(randomString);
      sheet.getRange(row, 3).setValue(formattedString);
    }
  }
    // Verifica se a coluna editada é a coluna 1 (a coluna de clientes)
  if (e.range.getColumn() == 1 && e.range.getRow() > 1) { // adiciona condição extra aqui
    // Pega a linha editada
    var row = e.range.getRow();
    
  // Verifica se a data de cadastro já foi preenchida
  if (sheet.getRange(row, 5).getValue() == "") {
    // Se a data de cadastro não foi preenchida, adiciona a data atual na terceira coluna
    sheet.getRange(row, 5).setValue(new Date()).setNumberFormat('dd/mm/yyyy h:mm:ss');
    // Define a cor do texto da célula como preto
    sheet.getRange(row, 5).setFontColor("#000000");
  }
}
}

function generateRandomString(length) {
  var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  var result = "";
  
  for (var i = 0; i < length; i++) {
    var randomIndex = Math.floor(Math.random() * chars.length);
    result += chars.charAt(randomIndex);
  }
  
  return result;
}

function formatString(str) {
  var formatted = "";
  
  for (var i = 0; i < str.length; i++) {
    if (i % 5 == 0 && i != 0) {
      formatted += "-";
    }
    
    formatted += str.charAt(i);
  }
  
  return formatted;
}
