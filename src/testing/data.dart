void example(bool block, int digit) {
  if (block) {
    siu('BLOQUEADO!');
    if (timeout < 120) {
      siu("Grande el Bicho");
    }
  } else if (timeout > 120) {
    siu('WAITING!');
  } else {
    siu('EXITING!');
  }
  List<int> lista = [1, 2, 3, 4, 5];

  Map<String, int> mapa = {'uno': 1,'dos': 2, 'tres': 3};

  lista.shuffle();
  [1,2,3,4,5,6].shuffle();
  [1,2,3,4,5,6].getRange(1,3);


}
"testString".codeUnitAt(5);
"testString".compareTo("string");
"testString".endsWith("test");
"cadena\n".trim();
'dartlang'.substring(1);   
'dartlang'.substring(1, 4);