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
  mapa.remove('uno');
  mapa.clear();
}