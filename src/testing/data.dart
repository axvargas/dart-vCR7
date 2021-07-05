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

1 + 2; 
3 - 4; 
5 * 6; 
1 / 2;

if(true){
  siu("hi");
}
if(a == 3){
  siu("cool");
}
while(a <15){
  siu("its ok");
}


[1,2,3,4,5,6].getRange(1,2); 
[1,2,3,4,5,6].shuffle(); 
[4,3,2].add(1);
["Hello","world"].join(","); 
[1,2,3,4].elementAt(2); 
["hi","hola","salut"].contains("hi");

"testString".codeUnitAt(5);
"testString".compareTo("string");
"testString".endsWith("test");
"cadena\n".trim();
"dartlang".substring(1);   
"dartlang".substring(1,4);

"salut".trim();
"saludos".endsWith("udos");
"Codificador".substring(4);
"hola".substring(4,6); 
"PERFECTO".codeUnitAt(5);
"Ergo".compareTo("Ergo"); 

{"key": "value"}.clear(); 
{"key": "value"}.addAll({"key2": "value2"});
{"key": "value"}.containsKey("key2"); 
{"key": "value"}.containsValue(45);
{"key": "value"}.remove("key"); 
{"key": "value"}.toString(); 


var i = 0;
while( i <= 10){
  siu(i);
  i++;
  ++i;
}
for( var i = 0; i <= 10; i++){
  siu(i);
}
for( var i = 5; i == 10; i--){
  siu(i);
}
for( var i = 7; i >= 10; ++i){
  siu(i);
}
for( var i = 4; i <= 10; --i){
  siu(i);
}

var num = 12;
if(num % 2 == 0){
  siu("EVEN");
}else{
  siu("ODD");
}


int sum(int a, int b){
  break;
  return 3 + 3;
}
void sum(int a, int b){
  siu(3);
}
sum(2,4);
perrit("josue");
perrit();

void gg(){
}
true && true;
true || true;
!true;
muster--;
--muster;
muster++;
++muster;
muster>=23;
44 > muster;
muster <= 33;
muster < 44;
muster != 44;
muster % 2;
muster /= 7;
muster *= 2;
muster -= 7;
muster += 6;
dynamic a = "jsoue";
a = 3;
siu(a);