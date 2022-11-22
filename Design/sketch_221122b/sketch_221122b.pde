Boton b0;

void setup() {
  size(640, 360);
  noStroke();
  b0 = new Boton(250,  250, 50);
}

void draw(){
  fill(130);
  b0.Display();
}

class Boton{
  int x, y;
  int size;
  float angle = 0.0;
  
  Boton(int tx, int ty, int ts) {
    x = tx;
    y = ty;
    size = ts;
 }
 
 void Display(){
   translate(x, y);
   fill(100);
   ellipse(0,0, size, size);
 }
}
