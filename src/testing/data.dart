void func1(bool block, int timeout) {
    if (block) {
      siu('BLOQUEADO!');
      if (timeout < 120) {
        return block;
      }
    } else if (timeout > 120) {
      siu('WAITING!');
    } else {
      siu('EXITING!');
    }
    List<int> lista = [1, 2, 3, 4, 5];
    lista.add(5);
    Map<String, int> mapa = {
      'uno': 1,
      'dos': 2,
      'tres': 3
    };
    mapa.remove('uno');
    mapa.clear();
}
