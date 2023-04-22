function diminuirValor() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var tempoColuna = sheet.getRange("D:D").getValues(); // Coluna "Tempo"
  var ativadaColuna = sheet.getRange("F:F").getValues(); // Coluna "Ativada"
  var dataAtual = new Date();
  var umaHora = 60 * 60 * 1000;
  
  for (var i = 1; i < tempoColuna.length; i++) { // Começa a partir da linha 2
    var tempoAtual = tempoColuna[i][0];
    var ativadaAtual = ativadaColuna[i][0];
    
    if (ativadaAtual === 1 && tempoAtual > 0) {
      var lastUpdate = PropertiesService.getScriptProperties().getProperty(i);
      if (lastUpdate === null || (dataAtual - new Date(lastUpdate)) / umaHora >= 24) {
        sheet.getRange(i+1, 4).setValue(tempoAtual - 1);
        sheet.getRange(i+1, 4).setNumberFormat("0"); // Formata para número inteiro
        sheet.getRange(i+1, 4).setFontWeight("bold"); // Coloca em negrito
        sheet.getRange(i+1, 4).setBackground("#F4CCCC"); // Pinta de vermelho claro
        sheet.getRange(i+1, 4).activate();
        PropertiesService.getScriptProperties().setProperty(i, dataAtual);
      }
    }
  }
}
